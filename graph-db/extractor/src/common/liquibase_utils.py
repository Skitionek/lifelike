import os
import re
import logging
import sys
from pathlib import Path

from mako.template import Template
from common.utils import *

template_dir = os.path.join(get_data_dir(), 'templates')
sql_template = 'sql_changeset.template'
custom_template = 'custom_changeset.template'
changelog_template = 'changelog.template'


def get_next_changelog_filename(directory: Path) -> str:
    """Return the next changelog-NNNN.xml filename (increments by 10)."""
    pattern = re.compile(r'^changelog-(\d{4})\.xml$')
    directory = Path(directory)
    existing = [
        int(m.group(1))
        for f in directory.iterdir()
        if (m := pattern.match(f.name))
    ]
    next_n = (max(existing) + 10) if existing else 0
    return f'changelog-{next_n:04d}.xml'

CUSTOM_PARAMS = """
      neo4jHost="${neo4jHost}"
      neo4jCredentials="${neo4jCredentials}"
      neo4jDatabase="${neo4jDatabase}"
      azureStorageName="${azureStorageName}"
      azureStorageKey="${azureStorageKey}"
      localSaveFileDir="${localSaveFileDir}"
"""


def get_template(templatefilename):
    return Template(filename=os.path.join(template_dir, templatefilename))


def get_changelog_template():
    return get_template(changelog_template)


class ChangeLog:
    def __init__(self, author: str, change_id_prefix: str = ''):
        self.author = author
        self.id_prefix = change_id_prefix
        self.file_prefix = f'{change_id_prefix}-' if change_id_prefix else ''

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        _handler = logging.StreamHandler(stream=sys.stdout)
        self.logger.addHandler(_handler)

    def generate_liquibase_changelog_file(self, output_dir: Path, outfile: str = None) -> Path:
        """Write the changelog XML to *output_dir*.

        Args:
            output_dir: Directory to write into (created if absent).
            outfile: Filename to use.  When *None* the next available
                     ``changelog-NNNN.xml`` sequence number is chosen
                     automatically.

        Returns:
            The path of the file that was written.
        """
        if not self.change_sets:
            self.logger.error('Need to call create_change_logs first')
            return None
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        if outfile is None:
            outfile = get_next_changelog_filename(output_dir)
        template = get_changelog_template()
        changes = []
        for cs in self.change_sets:
            s = cs.create_changelog_str()
            self.logger.info(s)
            changes.append(s)
        change_str = '\n\n'.join(changes)
        out_path = output_dir / outfile
        with open(out_path, 'w') as f:
            f.write(template.render(change_sets_str=change_str))
        self.logger.info(f'Wrote changelog to {out_path}')
        return out_path


class ChangeSet:
    def __init__(self, id, author: str, comment: str, cypher: str):
        self.id = id
        self.author = author
        self.comment = comment
        self.cypher = cypher

    def create_changelog_str(self):
        template = get_template(sql_template)
        # liquibase doesn't like the `<` character
        self.cypher = self.cypher.replace('<', '&lt;')
        return template.render(change_id=self.id, author=self.author, change_comment=self.comment, cypher_query=self.cypher)


class CustomChangeSet(ChangeSet):
    def __init__(self, id, author, comment, cypher,
                 filename:str,
                 handler="edu.ucsd.sbrg.FileQueryHandler",
                 filetype='TSV',
                 startrow=1):
        ChangeSet.__init__(self, id, author, comment, cypher)
        self.handler = handler
        self.filename = filename.replace('.tsv', '.zip')
        self.filetype = filetype
        self.start_at = startrow

    def create_changelog_str(self):
        template = get_template(custom_template)
        return template.render(change_id=self.id, change_comment=self.comment, author=self.author,
                               handler_class=self.handler, cypher_query=self.cypher, data_file=self.filename,
                               start_at=self.start_at, file_type=self.filetype, params=CUSTOM_PARAMS)


def generate_sql_changelog_file(id, author, comment, cypher, outfile):
    changeset = ChangeSet(id, author, comment, cypher)
    temp = get_changelog_template()
    with open(outfile, 'w') as f:
        f.write(temp.render(change_sets_str=changeset.create_changelog_str()))


if __name__ == '__main__':
    cypher = 'match(n:Gene)-[r]-(:Gene) where r.score < 0.4 delete r;'
    comment = 'Remove ecocyc-plus string relationships with 0.4 threshold.'
    outfile = 'ecocyc-plus-changelog-0010.xml'
    generate_sql_changelog_file('cut-string-rels-threshold', 'robin cai', comment, cypher, outfile)
