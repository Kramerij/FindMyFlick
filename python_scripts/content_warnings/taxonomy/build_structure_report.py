"""
build_structure_report.py

Builds a human-readable Markdown report confirming the taxonomy structure.

Inputs (relative to this script's folder):
- ../data/dtdd/dtdd_topics_catalog.json
- ./umbrellas.json
- ./claude_taxonomy.yml

Output:
- ./structure_report.md
"""
import json
from pathlib import Path
from collections import defaultdict

try:
    import yaml  # pip install pyyaml
except Exception:
    raise SystemExit("Missing dependency: PyYAML. Install with: pip install pyyaml")

ROOT = Path(__file__).resolve().parent          # .../content_warnings/taxonomy
CATALOG   = ROOT.parent / "data" / "dtdd" / "dtdd_topics_catalog.json"
UMBRELLAS = ROOT / "umbrellas.json"
YAML_MAP  = ROOT / "claude_taxonomy.yml"
OUT_MD    = ROOT / "structure_report.md"

def main():
    if not CATALOG.exists():
        raise FileNotFoundError(f"Missing {CATALOG}")
    if not UMBRELLAS.exists():
        raise FileNotFoundError(f"Missing {UMBRELLAS}")
    if not YAML_MAP.exists():
        raise FileNotFoundError(f"Missing {YAML_MAP}")

    topics_data = json.loads(CATALOG.read_text(encoding="utf-8"))
    topics = {int(t["topic_id"]): t for t in topics_data["topics"]}
    all_topic_ids = set(topics.keys())

    umbrellas = json.loads(UMBRELLAS.read_text(encoding="utf-8"))
    umbrella_name_by_id = {u["umbrella_id"]: u["name"] for u in umbrellas}

    y = yaml.safe_load(YAML_MAP.read_text(encoding="utf-8")) or {}

    seen_topic_ids, yaml_topic_ids = set(), set()
    per_umbrella = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for umbrella_id, groups in (y or {}).items():
        if not isinstance(groups, dict):
            continue
        for subcat, mapping in groups.items():
            if isinstance(mapping, dict):
                for item_label, ids in mapping.items():
                    for tid in (ids or []):
                        tid = int(tid)
                        yaml_topic_ids.add(tid)
                        per_umbrella[umbrella_id][subcat][item_label].append(tid)
                        seen_topic_ids.add(tid)
            else:
                for tid in (mapping or []):
                    tid = int(tid)
                    yaml_topic_ids.add(tid)
                    per_umbrella[umbrella_id][subcat]["(items)"].append(tid)
                    seen_topic_ids.add(tid)

    unmapped = sorted(all_topic_ids - seen_topic_ids)
    unknown  = sorted(yaml_topic_ids - all_topic_ids)

    umbrella_counts = {}
    for uid, subcats in per_umbrella.items():
        count = 0
        for _, items in subcats.items():
            for _, ids in items.items():
                count += len(ids)
        umbrella_counts[uid] = count

    lines = []
    lines.append("# Content Warning Taxonomy — Structure Report\n")
    lines.append(f"- **Total catalog topics**: {len(all_topic_ids)}")
    lines.append(f"- **Unique mapped topic_ids**: {len(seen_topic_ids)}")
    lines.append("")
    lines.append("## Tier 1 — Umbrellas")
    for u in umbrellas:
        uid = u["umbrella_id"]
        uname = u["name"]
        lines.append(f"- **{uid} — {uname}**  _(mapped items: {umbrella_counts.get(uid,0)})_")
    lines.append("")

    for u in umbrellas:
        uid = u["umbrella_id"]
        uname = u["name"]
        lines.append(f"---\n\n## {uid} — {uname}")
        if uid not in per_umbrella:
            lines.append("_No items mapped yet._\n")
            continue
        for subcat, items in per_umbrella[uid].items():
            lines.append(f"### {subcat}")
            for item_label, ids in items.items():
                ids_sorted = sorted(set(ids))
                name_list = [topics[i]["topic_name"] if i in topics else "(unknown)" for i in ids_sorted]
                pretty = ", ".join(f"{i} — {n}" for i, n in zip(ids_sorted, name_list))
                lines.append(f"- **{item_label}**: {pretty}")
            lines.append("")

    lines.append("\n---\n\n## Validation")
    lines.append(f"- Unique mapped topic_ids: **{len(seen_topic_ids)}** / {len(all_topic_ids)}")
    if unmapped:
        lines.append(f"- Unmapped topic_ids (in catalog, missing from YAML): {len(unmapped)}")
        for tid in unmapped[:100]:
            lines.append(f"  - {tid} — {topics.get(tid,{}).get('topic_name','(unknown)')}")
        if len(unmapped) > 100:
            lines.append(f"  - ... and {len(unmapped)-100} more")
    else:
        lines.append("- Unmapped topic_ids: **none**")

    if unknown:
        lines.append(f"- Unknown topic_ids (in YAML, not in catalog): {len(unknown)}")
        for tid in unknown[:100]:
            lines.append(f"  - {tid}")
        if len(unknown) > 100:
            lines.append(f"  - ... and {len(unknown)-100} more")
    else:
        lines.append("- Unknown topic_ids: **none**")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote report: {OUT_MD}")

if __name__ == "__main__":
    main()