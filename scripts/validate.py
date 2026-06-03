import os
import yaml
import json
import sys
from jsonschema import validate, ValidationError

SCHEMA_PATH = "schema/paper.schema.json"
DATA_DIR = "data"

with open(SCHEMA_PATH) as f:
    schema = json.load(f)

errors = []
ids_seen = set()

for filename in os.listdir(DATA_DIR):
    if not filename.endswith(".yaml"):
        continue
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath) as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            errors.append(f"{filename}: Invalid YAML - {e}")
            continue
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        errors.append(f"{filename}: Schema error - {e.message}")
        continue
    for section in ["mcq", "cq"]:
        for q in data.get(section, []):
            qid = q.get("id")
            if qid in ids_seen:
                errors.append(f"{filename}: Duplicate ID - {qid}")
            ids_seen.add(qid)

if errors:
    print("Validation failed:")
    for e in errors:
        print(f"  x {e}")
    sys.exit(1)
else:
    print(f"All files valid. {len(ids_seen)} questions checked.")