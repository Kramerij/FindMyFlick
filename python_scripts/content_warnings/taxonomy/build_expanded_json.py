"""
build_expanded_json.py

Creates taxonomy/expanded.json for backend or API use.

Inputs:
- ../data/dtdd/dtdd_topics_catalog.json
- ./umbrellas.json
- ./claude_taxonomy.yml

Output:
- ./expanded.json

Structure:
{
  "umbrellas": [...],
  "topics": { "<id>": {"topic_id": ..., "topic_name": ...}, ... },
  "umbrella_to_topic_ids": {"U01":[153,...], ...},
  "topic_id_to_umbrellas": {"153":["U01",...], ...}
}
"""
import json, csv
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    raise SystemExit("Please install PyYAML: pip install pyyaml")

ROOT = Path(__file__).resolve().parent          # .../content_warnings/taxonomy
CATALOG   = ROOT.parent / "data" / "dtdd" / "dtdd_topics_catalog.json"
UMBRELLAS = ROOT / "umbrellas.json"
YAML_MAP  = ROOT / "claude_taxonomy.yml"
OUT       = ROOT / "expanded.json"

def main():
    if not CATALOG.exists():
        raise FileNotFoundError(f"Missing {CATALOG}")
    if not UMBRELLAS.exists():
        raise FileNotFoundError(f"Missing {UMBRELLAS}")
    if not YAML_MAP.exists():
        raise FileNotFoundError(f"Missing {YAML_MAP}")

    # Load data
    topics_list = json.loads(CATALOG.read_text(encoding="utf-8"))["topics"]
    topics = {t["topic_id"]: {"topic_id": t["topic_id"], "topic_name": t["topic_name"]} for t in topics_list}
    umbrellas = json.loads(UMBRELLAS.read_text(encoding="utf-8"))
    y = yaml.safe_load(YAML_MAP.read_text(encoding="utf-8")) or {}

    umbrella_to_topic_ids = defaultdict(list)
    topic_id_to_umbrellas = defaultdict(list)

    for umbrella_id, groups in y.items():
        if not isinstance(groups, dict):
            continue
        for subcat, mapping in groups.items():
            if isinstance(mapping, dict):
                for _, ids in mapping.items():
                    for tid in (ids or []):
                        umbrella_to_topic_ids[umbrella_id].append(int(tid))
                        topic_id_to_umbrellas[str(tid)].append(umbrella_id)
            else:
                for tid in (mapping or []):
                    umbrella_to_topic_ids[umbrella_id].append(int(tid))
                    topic_id_to_umbrellas[str(tid)].append(umbrella_id)

    data = {
        "umbrellas": umbrellas,
        "topics": topics,
        "umbrella_to_topic_ids": {k: sorted(set(v)) for k, v in umbrella_to_topic_ids.items()},
        "topic_id_to_umbrellas": topic_id_to_umbrellas
    }

    OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Wrote backend taxonomy JSON: {OUT}")

if __name__ == "__main__":
    main()