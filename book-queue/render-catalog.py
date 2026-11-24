"""Render the reading catalog from the course, blueprint, and other-format indexes.

Run: python3 book-queue/render-catalog.py
Check without writing: python3 book-queue/render-catalog.py --check
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BLUEPRINTS = ROOT / "syllabus-track" / "blueprints"

# Human-assigned subjects, not inherited from production tracks. Mapped
# blueprints inherit the canonical queue title's subject and get no extra row.
TOPICS = {
    "AI and agent systems": (
        "2 3 11 57 58 61 62 63 80 109 139",
        "1 3 4 5 17 28 36 37 38 56 63 65 66 71 72 74 75 78",
    ),
    "Biology, medicine, and health": (
        "93 94 95 124 125 126 127 128 129 130 131 132 133 134 135 136",
        "73 80 86",
    ),
    "Business, economics, and law": (
        "16 18 25 46 47 83 84 97 98 103 104",
        "29 32 33 53",
    ),
    "Computer science and software engineering": (
        "4 7 24 59 60",
        "6 16 18 19 23 24 30 31 54 55 68 77 81 82 83",
    ),
    "Data, statistics, and research methods": (
        "6 39 55 72 73 78 79 82 116",
        "2 22 25 26 27 42 59 61 70 76 85",
    ),
    "Design and visualization": (
        "12 26 38 66 69 71",
        "57 62 67",
    ),
    "Education and learning": (
        "27 28 29 30 31 32 33 34 35 36 37 75 76 77 110 111 112 113 114",
        "",
    ),
    "Engineering, networks, and security": (
        "74 96",
        "20 34 35 43 44 45 46 47 48 49 50 51 52",
    ),
    "Finance and accounting": (
        "1 5 9 15 48 49 99",
        "64 79 84",
    ),
    "Games, animation, film, and music": (
        "8 13 14 64 65 68 107 108 121",
        "",
    ),
    "Humanities and social sciences": (
        "81 115 117 118 119 120",
        "",
    ),
    "Marketing and branding": (
        "17 50 51 52 53 54 67 102",
        "",
    ),
    "Mathematics": (
        "10 19 20 21 22 23 56 106",
        "15 39 41",
    ),
    "Physics, chemistry, and quantum science": (
        "40 41 42 43 44 45 85 86 87 88 89 90 91 92 122 123 137 138",
        "60",
    ),
}

BRIEFS = {
    "9": ("Consolidated scope", "computational-finance.md"),
    "31": ("Revised opening and plan", "gemini-notebook-for-education.md"),
    "37": ("Consolidated scope", "designing-educational-slide-decks-with-ai.md"),
    "139": ("Popular-book plan", "computational-skepticism.md"),
}
QUEUE_STATUS = {"ready": "Ready to scope", "compare": "Compare sources", "hold": "On hold"}
BLUEPRINT_STATUS = {
    "ready-for-draft-review": "Blueprint; candidate for drafting",
    "compare-scope": "Blueprint; compare scope",
    "hold-source": "Blueprint; on hold",
    "reuse-private-pilot": "Blueprint; private local pilot",
}


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file, delimiter="\t"))


def anchor(text):
    return re.sub(r"[^\w -]", "", text.lower()).replace(" ", "-")


def cell(text):
    return text.replace("|", r"\|")


def repo_links(value):
    links = []
    local = False
    for item in value.split("; "):
        if item.startswith("local:"):
            local = True
            continue
        if item:
            full_name = item if "/" in item else f"nikbearbrown/{item}"
            assert re.fullmatch(r"[\w.-]+/[\w.-]+", full_name), item
            links.append(f"[{cell(item.split('/')[-1])}](https://github.com/{full_name})")
    if local:
        links.append("Local material (no GitHub copy linked)")
    return links


def blueprint_link(row, label="Blueprint"):
    path = BLUEPRINTS / row["directory"]
    assert (path / "README.md").is_file(), path
    return f"[{label}]({path.relative_to(ROOT).as_posix()}/)"


def catalog():
    queue = {row["Order"]: row for row in read_tsv(ROOT / "queue.tsv")}
    other = {row["Order"]: row for row in read_tsv(ROOT / "other-formats.tsv")}
    assert not set(queue) & set(other)
    entries = queue | other
    blueprints = {row["blueprint id"]: row for row in read_tsv(BLUEPRINTS / "index.tsv")}
    mapped = {}
    for row in blueprints.values():
        parent = row["canonical book queue row"]
        if parent:
            assert entries[parent]["Book title"] == row["title"], row
            assert (parent in other) == (row["draft route"] == "workshop-reference"), row
            mapped.setdefault(parent, []).append(row)

    used_q, used_b, sections = set(), set(), []
    for topic, (q_ids, b_ids) in TOPICS.items():
        rows = []
        for key in q_ids.split():
            assert key not in used_q, key
            used_q.add(key)
            q = entries[key]
            links = []
            if key in BRIEFS:
                label, link = BRIEFS[key]
                assert (ROOT / link).is_file(), link
                links.append(f"[{label}]({link})")
            links.extend(blueprint_link(b, "Blueprint reference" if key in other else "Blueprint") for b in mapped.get(key, []))
            links.extend(repo_links(q["Primary source(s)"]))
            assert links, key
            rows.append((q["Book title"], QUEUE_STATUS[q["Plan stage"]], links, q.get("Format", "Course")))
        for key in b_ids.split():
            assert key not in used_b, key
            used_b.add(key)
            b = blueprints[key]
            assert not b["canonical book queue row"], key
            rows.append((b["title"], BLUEPRINT_STATUS[b["draft route"]], [blueprint_link(b)], "Course"))
        sections.append((topic, sorted(rows, key=lambda row: row[0].casefold())))

    assert used_q == set(entries), (set(entries) - used_q, used_q - set(entries))
    assert used_b == {key for key, row in blueprints.items() if not row["canonical book queue row"]}
    titles = [x[0].casefold() for _, rows in sections for x in rows]
    assert len(titles) == len(set(titles)), "Unexpected duplicate display title"
    formats = [
        ("Popular books", "Popular book", "General-audience books. No course structure or AI Plus One branding."),
        ("Courses and textbooks", "Course", "Full courses with substantial learning material, including AI Plus One textbooks and syllabus-based blueprints."),
        ("Workshops", "Workshop", "Short, practical sessions or series. Some are self-study, often without credit; these are not full courses."),
    ]
    totals = {fmt: sum(r[3] == fmt for _, rows in sections for r in rows) for _, fmt, _ in formats}
    assert sum(totals.values()) == len(titles)
    out = [
        "# Books, courses, and workshops",
        "",
        "Browse by format. Within each format, titles are alphabetized by topic. Links point to available sources or plans, not promised releases. Some sources require GitHub access. Local material is labeled.",
        "",
    ]
    out.extend(f"- [{name}](#{anchor(name)}) ({totals[fmt]})" for name, fmt, _ in formats)
    out += [
        "",
        "For production: [course and textbook queue](queue.tsv) · [syllabus blueprint index](syllabus-track/blueprints/) · [popular book and workshop inventory](other-formats.tsv) · [source triage](source-triage.tsv) · [Codex handoff](../codex-handoff.md). A hold is planning only; no row implies rights clearance, publication, or enrollment.",
        "",
    ]
    for name, fmt, description in formats:
        out += [f"## {name}", "", description, ""]
        active = [(topic, [r for r in rows if r[3] == fmt]) for topic, rows in sections]
        active = [(topic, rows) for topic, rows in active if rows]
        prefix = {"Course": "", "Popular book": "Books: ", "Workshop": "Workshops: "}[fmt]
        out.extend(f"- [{topic}](#{anchor(prefix + topic)}) ({len(rows)})" for topic, rows in active)
        out.append("")
        for topic, rows in active:
            out += [f"### {prefix}{topic}", "", "| Title | Status | Available material |", "| --- | --- | --- |"]
            for title, status, links, _ in rows:
                out.append(f"| {cell(title)} | {status} | {' · '.join(links)} |")
            out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    result = catalog()
    path = ROOT / "README.md"
    if sys.argv[1:] == ["--check"]:
        if path.read_text(encoding="utf-8") != result:
            raise SystemExit("Catalog is stale. Run render-catalog.py.")
    elif not sys.argv[1:]:
        path.write_text(result, encoding="utf-8")
    else:
        raise SystemExit("Usage: render-catalog.py [--check]")
