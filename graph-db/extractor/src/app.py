import argparse
import logging
import logging.handlers
import sys
from pathlib import Path

import coloredlogs

import biocyc.biocyc_parser as biocyc_parser
import chebi.chebi_parser as chebi_parser
import enzyme.enzyme_parser as enzyme_parser
import go.go_parser as go_parser
import kegg.kegg_parser as kegg_parser
import mesh.mesh_parser as mesh_parser
import mesh.add_disease_synonyms_by_pruning_disease as add_disease_synonyms_by_pruning_disease
import mesh.mesh_annotations as mesh_annotations
import ncbi.ncbi_gene_parser as ncbi_gene_parser
import ncbi.ncbi_taxonomy_parser as ncbi_taxonomy_parser
import literature.literature_data_parser as literature_data_parser
import regulondb.regulondb_parser as regulondb_parser
import stringdb.stringdb_parser as stringdb_parser
import uniprot.uniprot_parser as uniprot_parser

import enzyme.enzyme_liquibase as enzyme_liquibase
import go.go_liquibase as go_liquibase
import kegg.kegg_liquibase as kegg_liquibase
import literature.literature_liquibase as literature_liquibase
import mesh.mesh_liquibase as mesh_liquibase
import ncbi.ncbi_gene_liquibase as ncbi_gene_liquibase
import ncbi.ncbi_taxonomy_liquibase as ncbi_taxonomy_liquibase
import regulondb.regulondb_liquibase as regulondb_liquibase
import stringdb.stringdb_liquibase as stringdb_liquibase
import uniprot.uniprot_liquibase as uniprot_liquibase

_LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
_LOG_MAX_SIZE = 1024 * 1024
_LOG_MAX_FILES = 5

# graph-db root is 3 levels up from this file (src -> extractor -> graph-db)
GRAPH_DB_DIR = Path(__file__).resolve().parent.parent.parent

DOMAIN_PARSERS = {
    'biocyc': biocyc_parser,
    'chebi': chebi_parser,
    'enzyme': enzyme_parser,
    'go': go_parser,
    'kegg': kegg_parser,
    'mesh': mesh_parser,
    'mesh-add-disease-synonyms': add_disease_synonyms_by_pruning_disease,
    'mesh-annotations': mesh_annotations,
    'ncbi-gene': ncbi_gene_parser,
    'ncbi-taxonomy': ncbi_taxonomy_parser,
    'regulondb': regulondb_parser,
    'stringdb': stringdb_parser,
    'uniprot': uniprot_parser,
    'zenodo-literature': literature_data_parser,
}

DOMAIN_CHANGELOG_GENERATORS = {
    'enzyme': enzyme_liquibase,
    'go': go_liquibase,
    'kegg': kegg_liquibase,
    'mesh': mesh_liquibase,
    'ncbi-gene': ncbi_gene_liquibase,
    'ncbi-taxonomy': ncbi_taxonomy_liquibase,
    'regulondb': regulondb_liquibase,
    'stringdb': stringdb_liquibase,
    'uniprot': uniprot_liquibase,
    'zenodo-literature': literature_liquibase,
}

_CHANGELOG_DIRS = [
    'lifelike-graph',
    'new-lifelike-graph',
    'small-test-graph',
    'ecocyc-plus',
    'reactome-gds',
]


def _add_changelog_args(p):
    """Attach the shared generate-changelog / full-load arguments to *p*."""
    p.add_argument('domain', choices=sorted(DOMAIN_CHANGELOG_GENERATORS))
    p.add_argument('--author', required=True, help='Author name recorded in each changeset')
    p.add_argument(
        '--changelog-dir',
        default='lifelike-graph',
        choices=_CHANGELOG_DIRS,
        help='Target sub-directory under graph-db/changelog/ (default: lifelike-graph)',
    )
    p.add_argument(
        '--output-dir',
        type=Path,
        default=None,
        help='Explicit output directory; overrides --changelog-dir auto-placement',
    )
    p.add_argument(
        '--initial-load',
        action='store_true',
        default=False,
        help='Include index/constraint changesets (use for a fresh database)',
    )


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description='Graph-DB extractor: parse domain data and/or generate Liquibase changelogs'
    )

    parser.add_argument(
        '--log-file',
        help='Append log messages to file; files are rotated at 1 MB',
        type=Path,
    )
    parser.add_argument(
        '--log-level',
        default='INFO',
        choices=('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'),
    )
    parser.add_argument(
        '--prefix',
        default='',
        help='Optional prefix tag added to change IDs and data file names',
    )

    subparser = parser.add_subparsers(dest='command', required=True)

    # ── extract subcommands (original domain parsers) ──────────────────────
    biocyc_sub = subparser.add_parser('biocyc', help='Extract BioCyc data')
    biocyc_sub.add_argument(
        '--data-sources',
        nargs='*',
        help='Specific BioCyc data sources, e.g. EcoCyc YeastCyc MetaCyc',
    )
    for name in (
        'chebi', 'enzyme', 'go', 'kegg', 'mesh',
        'mesh-add-disease-synonyms', 'mesh-annotations',
        'ncbi-gene', 'ncbi-taxonomy', 'regulondb', 'stringdb',
        'uniprot', 'zenodo-literature',
    ):
        subparser.add_parser(name, help=f'Extract {name} data')

    # ── generate-changelog subcommand ──────────────────────────────────────
    gc_parser = subparser.add_parser(
        'generate-changelog',
        help='Generate a Liquibase changelog XML and place it in graph-db/changelog/',
    )
    _add_changelog_args(gc_parser)

    # ── full-load subcommand ───────────────────────────────────────────────
    fl_parser = subparser.add_parser(
        'full-load',
        help='Extract + upload TSVs then generate the Liquibase changelog in one step',
    )
    _add_changelog_args(fl_parser)
    fl_parser.add_argument(
        '--data-sources',
        nargs='*',
        help='BioCyc only: specific data sources to load',
    )

    return parser.parse_args(argv)


def setup_logging(args):
    coloredlogs.install(fmt=_LOG_FORMAT, level=args.log_level)

    root_log = logging.getLogger()
    if args.log_file is not None:
        handler = logging.handlers.RotatingFileHandler(
            filename=args.log_file, maxBytes=_LOG_MAX_SIZE, backupCount=_LOG_MAX_FILES
        )
        handler.setFormatter(logging.Formatter(_LOG_FORMAT))
        root_log.addHandler(handler)


def _resolve_output_dir(args) -> Path:
    """Return the directory the changelog XML will be written to."""
    if args.output_dir:
        return Path(args.output_dir)
    return GRAPH_DB_DIR / 'changelog' / args.changelog_dir / 'changelogs'


def main(argv):
    args = parse_args(argv)

    setup_logging(args)

    logger = logging.getLogger('main')
    logger.info(
        'Executing '
        + __file__
        + ' with arguments: '
        + ', '.join(['%s=%s' % (key, value) for (key, value) in args.__dict__.items()])
    )

    if args.command == 'generate-changelog':
        output_dir = _resolve_output_dir(args)
        DOMAIN_CHANGELOG_GENERATORS[args.domain].generate(args, output_dir)

    elif args.command == 'full-load':
        # 1. extract data and upload TSVs
        DOMAIN_PARSERS[args.domain].main(args)
        # 2. generate and auto-place the changelog
        output_dir = _resolve_output_dir(args)
        DOMAIN_CHANGELOG_GENERATORS[args.domain].generate(args, output_dir)

    else:
        # original extract-only path (domain name is the command)
        DOMAIN_PARSERS[args.command].main(args)


if __name__ == '__main__':
    main(sys.argv[1:])
