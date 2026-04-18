import importlib.resources as resources
import json

import fastjsonschema

from .. import formats

with resources.open_text(formats, 'annotations_v1.json') as f:
    _schema = json.load(f)

# Use this to validate the content of a .annotations config file
validate_annotations = fastjsonschema.compile(_schema)
# Schema version — increment when annotations_v1.json is superseded
current_version = '1'
