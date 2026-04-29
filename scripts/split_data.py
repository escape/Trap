#!/usr/bin/env python3
"""Split monolithic DATA/*.md files into one-file-per-entity."""

import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "DATA")


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def split_by_h2(filepath):
    """Split a markdown file by ## headings. Returns list of (slug, content)."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Split on ## headings (not ### or deeper)
    parts = re.split(r"(?=^## )", text, flags=re.MULTILINE)
    results = []
    for part in parts:
        match = re.match(r"^## (\S+)\s*\n", part)
        if match:
            slug = match.group(1)
            # Strip the ## heading line itself — the slug becomes the filename
            content = part[match.end():]
            # Strip leading/trailing whitespace but keep internal structure
            content = content.strip()
            results.append((slug, content))
    return results


def split_nodes():
    src = os.path.join(DATA, "nodes.md")
    dest = os.path.join(DATA, "nodes")
    ensure_dir(dest)

    with open(src, "r", encoding="utf-8") as f:
        text = f.read()

    # Split on ## headings
    parts = re.split(r"(?=^## \w)", text, flags=re.MULTILINE)
    count = 0
    for part in parts:
        match = re.match(r"^## (\S+)\s*\n", part)
        if not match:
            continue
        slug = match.group(1)
        content = part.strip()
        # Remove trailing --- separator if present
        content = re.sub(r"\n---\s*$", "", content)
        # Remove cluster comment lines that precede nodes
        content = re.sub(r"^<!--.*?-->\s*\n*", "", content)

        outpath = os.path.join(dest, f"{slug}.md")
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(content + "\n")
        count += 1
    print(f"  nodes: {count} files written to DATA/nodes/")


def split_edges():
    src = os.path.join(DATA, "edges.md")
    dest = os.path.join(DATA, "edges")
    ensure_dir(dest)

    with open(src, "r", encoding="utf-8") as f:
        text = f.read()

    parts = re.split(r"(?=^## \w)", text, flags=re.MULTILINE)
    count = 0
    for part in parts:
        match = re.match(r"^## (\S+)\s*\n", part)
        if not match:
            continue
        slug = match.group(1)
        content = part.strip()
        content = re.sub(r"^<!--.*?-->\s*\n*", "", content)

        outpath = os.path.join(dest, f"{slug}.md")
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(content + "\n")
        count += 1
    print(f"  edges: {count} files written to DATA/edges/")


def split_clusters():
    src = os.path.join(DATA, "clusters.md")
    dest = os.path.join(DATA, "clusters")
    ensure_dir(dest)

    with open(src, "r", encoding="utf-8") as f:
        text = f.read()

    parts = re.split(r"(?=^## \w)", text, flags=re.MULTILINE)
    count = 0
    for part in parts:
        match = re.match(r"^## (\S+)\s*\n", part)
        if not match:
            continue
        slug = match.group(1)
        content = part.strip()
        content = re.sub(r"\n---\s*$", "", content)

        outpath = os.path.join(dest, f"{slug}.md")
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(content + "\n")
        count += 1
    print(f"  clusters: {count} files written to DATA/clusters/")


def create_tactics():
    """Create tactic files from the SCHEMA.md vocabulary."""
    dest = os.path.join(DATA, "tactics")
    ensure_dir(dest)

    tactics = {
        "parental_anxiety_exploitation": {
            "name": "Parental anxiety exploitation",
            "description": "Weaponises fear for children's safety or future to bypass critical thinking.",
        },
        "wellness_to_conspiracy_pipeline": {
            "name": "Wellness-to-conspiracy pipeline",
            "description": "Uses legitimate health concern as gateway to medical and institutional distrust.",
        },
        "conspiracy_thinking": {
            "name": "Conspiracy thinking",
            "description": "Presents unfalsifiable hidden-knowledge framework as superior insight.",
        },
        "identity_fusion": {
            "name": "Identity fusion",
            "description": "Merges personal identity with group identity so that questioning the group feels like self-destruction.",
        },
        "fear_monetization": {
            "name": "Fear monetization",
            "description": "Converts ongoing threat anxiety into product sales, subscriptions, or donations.",
        },
        "pseudo_intellectual_cover": {
            "name": "Pseudo-intellectual cover",
            "description": "Uses dense or academic-sounding language to make extreme positions feel like rigorous analysis.",
        },
        "dehumanization": {
            "name": "Dehumanization",
            "description": "Progressively strips out-group members of individuality or humanity to lower inhibition against harm.",
        },
        "us_vs_them_framing": {
            "name": "Us vs. them framing",
            "description": "Reduces complex social reality to a binary of in-group (enlightened) vs. out-group (enemy or dupe).",
        },
        "isolation_from_support_networks": {
            "name": "Isolation from support networks",
            "description": "Systematically separates target from friends, family, or institutions that might provide counter-perspective.",
        },
        "magical_thinking": {
            "name": "Magical thinking",
            "description": "Frames belief or spiritual alignment as a causal mechanism for material or social outcomes.",
        },
        "irony_shield": {
            "name": "Irony shield",
            "description": "Deploys humour, memes, and plausible deniability to circulate genuinely harmful content without accountability.",
        },
        "manufactured_urgency": {
            "name": "Manufactured urgency",
            "description": "Creates artificial time pressure or crisis framing to prevent deliberate evaluation.",
        },
        "sunk_cost_entrenchment": {
            "name": "Sunk-cost entrenchment",
            "description": "Deepens commitment by ensuring the target has already sacrificed relationships, money, or reputation for the identity.",
        },
        "parasocial_replacement": {
            "name": "Parasocial replacement",
            "description": "Substitutes algorithmically mediated relationship with an influencer or anonymous figure for real community.",
        },
    }

    count = 0
    for slug, data in tactics.items():
        content = f"## {slug}\n\n- **Name:** {data['name']}\n- **Description:** {data['description']}\n"
        outpath = os.path.join(dest, f"{slug}.md")
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
    print(f"  tactics: {count} files written to DATA/tactics/")


if __name__ == "__main__":
    print("Splitting DATA files...")
    split_nodes()
    split_edges()
    split_clusters()
    create_tactics()
    print("Done.")
