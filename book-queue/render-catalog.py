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
EDITORIAL_BLUEPRINTS = ROOT / "editorial-blueprints"

# Human-assigned subjects, not inherited from production tracks. Mapped
# blueprints inherit the canonical queue title's subject and get no extra row.
TOPICS = {
    "AI and agent systems": (
        "2 3 11 57 58 61 63 80 109",
        "1 3 4 5 17 28 36 37 38 56 63 65 66 71 72 74 75 78",
    ),
    "Artificial intelligence and real intelligence": ("62 81 93 139", ""),
    "Biology, medicine, and health": (
        "94 95 124 125 126 127 128 129 130 131 132 133 134 135 136",
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
        "115 117 118 119 120",
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
    "139": ("Editorial brief", "computational-skepticism.md"),
}
# Existing complete plans (or verified handoffs to complete local plans).
# These are distinct from source briefs and reference-only syllabus blueprints.
EXISTING_PLANS = {
    "13": "local-blueprints/13-game-ai/",
    "14": "local-blueprints/14-game-reinforcement-learning/",
    "55": "local-blueprints/55-bayesian-probability.md",
    "64": "local-blueprints/64-generative-ai-for-game-development/",
    "65": "local-blueprints/65-agentic-filmmaking.md",
    "66": "local-blueprints/66-creative-engineering.md",
    "75": "workshop-blueprints/75-ai-readiness/",
    "107": "local-blueprints/107-animation-with-blender/",
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


def plan_link(path, label="Blueprint"):
    assert (ROOT / path).is_file() or (ROOT / path / "README.md").is_file(), path
    return f"[{label}]({path})"


def blueprint_link(row, label="Blueprint"):
    path = BLUEPRINTS / row["directory"]
    for required in ("README.md", "vision.md", "architecture.md", "outline.md",
                     "chapters-spec.md", "risks.md", "sources.tsv"):
        assert (path / required).is_file(), (path, required)
    return plan_link(path.relative_to(ROOT).as_posix() + "/", label)


def editorial_plan_path(key, row, legacy_name=False):
    slug = row.get("Public target repo slug") or row.get("Legacy source-family key")
    if not slug and key == "139":
        slug = "computational-skepticism"
    if row.get("Format") and not legacy_name:
        slug = re.sub(r"[^a-z0-9]+", "-", row["Book title"].lower()).strip("-")
    assert slug and re.fullmatch(r"[a-z0-9-]+", slug), (key, slug)
    return EDITORIAL_BLUEPRINTS / f"{int(key):02d}-{slug}.md"


def indexed_tsv(path, key):
    rows = read_tsv(path)
    result = {row[key]: row for row in rows}
    assert len(rows) == len(result) and "" not in result, (path, "Missing or duplicate identifier")
    return result


def verified_draft_links(queue, blueprints):
    # Explicit publication receipts only. A proposed target or verified
    # private seed in the migration register must not make a public link.
    drafts = indexed_tsv(ROOT / "public-drafts.tsv", "id")
    if not drafts:
        return {}, []
    targets = indexed_tsv(ROOT / "repo-migration" / "catalog-migration-plan.tsv", "id")
    allowed = {f"queue:{key}": queue[key]["Book title"] for key in queue}
    allowed.update({
        f"syllabus:{key}": row["title"]
        for key, row in blueprints.items()
        if not row["canonical book queue row"] and row["draft route"] != "workshop-reference"
    })
    labels = {"excerpt": "Public draft excerpt", "compact": "Public compact rough draft", "manuscript": "Public rough draft"}
    links, used_slugs, reading_rows = {}, set(), []
    for key, row in drafts.items():
        slug = row["repo_slug"]
        assert key in allowed and key in targets, f"Not a canonical course draft: {key}"
        assert targets[key]["title"] == allowed[key], f"Wrong draft title for: {key}"
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*-ai-one", slug), f"Invalid draft slug: {slug}"
        assert slug == targets[key]["destination_slug"], f"Wrong draft slug for: {key}"
        assert slug not in used_slugs, f"Draft repository listed twice: {slug}"
        assert re.fullmatch(r"[0-9a-f]{40}", row["verified_commit"]), f"Invalid verified commit for: {key}"
        assert row["coverage"] in labels, f"Unknown draft coverage for: {key}"
        used_slugs.add(slug)
        base = f"https://github.com/nikbearbrown/{slug}"
        links[key] = f"[{labels[row['coverage']]}]({base})"
        chapter = row.get("start_path", "")
        assert re.fullmatch(r"chapters/[0-9]+-[a-z0-9]+(?:-[a-z0-9]+)*[.]md", chapter), f"Missing or invalid first chapter for: {key}"
        chapter_title = row.get("start_title", "").strip()
        focus = row.get("reader_focus", "").strip()
        assert chapter_title and focus, f"Missing reader metadata for: {key}"
        assert not re.match(r"Chapter\s+\d+[ :]", chapter_title, re.I), f"Repeated chapter number for: {key}"
        assert all(not re.search(r"[\[\]<>|\r\n]", value) for value in (chapter_title, focus)), f"Invalid reading list text for: {key}"
        reading_rows.append((allowed[key], base, chapter, chapter_title, focus))
    return links, reading_rows


def catalog():
    queue = indexed_tsv(ROOT / "queue.tsv", "Order")
    other = indexed_tsv(ROOT / "other-formats.tsv", "Order")
    assert not set(queue) & set(other)
    entries = queue | other
    blueprints = indexed_tsv(BLUEPRINTS / "index.tsv", "blueprint id")
    draft_links, reading_rows = verified_draft_links(queue, blueprints)
    mapped = {}
    for row in blueprints.values():
        parent = row["canonical book queue row"]
        if parent:
            assert entries[parent]["Book title"] == row["title"], row
            assert (parent in other) == (row["draft route"] == "workshop-reference"), row
            mapped.setdefault(parent, []).append(row)

    assert EXISTING_PLANS.keys() <= entries.keys()
    used_editorial = set()
    used_q, used_b, sections = set(), set(), []
    for topic, (q_ids, b_ids) in TOPICS.items():
        rows = []
        for key in q_ids.split():
            assert key not in used_q, key
            used_q.add(key)
            q = entries[key]
            full_plans = [b for b in mapped.get(key, []) if b["draft route"] != "workshop-reference"]
            if key in EXISTING_PLANS:
                assert not full_plans, key
                links = [plan_link(EXISTING_PLANS[key])]
            elif full_plans:
                links = [blueprint_link(b) for b in full_plans]
            else:
                path = editorial_plan_path(key, q)
                assert path.is_file(), f"Missing editorial blueprint: #{key} {path.name}"
                contents = path.read_text(encoding="utf-8")
                assert contents.startswith(f"# {q['Book title']}\n"), f"Wrong title: {path.name}"
                assert len(contents) > 500, f"Blueprint is too short to be useful: {path.name}"
                used_editorial.add(path)
                links = [plan_link(path.relative_to(ROOT).as_posix())]
            if key in BRIEFS:
                label, link = BRIEFS[key]
                links.append(plan_link(link, label))
            links.extend(blueprint_link(b, "Course reference") for b in mapped.get(key, [])
                         if b["draft route"] == "workshop-reference")
            links.extend(["[AI Readiness skill](https://github.com/nikbearbrown/ai-readiness)"] if key == "75" else repo_links(q["Primary source(s)"]))
            if f"queue:{key}" in draft_links:
                links.insert(0, draft_links[f"queue:{key}"])
            assert links, key
            rows.append((q["Book title"], QUEUE_STATUS[q["Plan stage"]], links, q.get("Format", "Course")))
        for key in b_ids.split():
            assert key not in used_b, key
            used_b.add(key)
            b = blueprints[key]
            assert not b["canonical book queue row"], key
            links = [blueprint_link(b)]
            if f"syllabus:{key}" in draft_links:
                links.insert(0, draft_links[f"syllabus:{key}"])
            rows.append((b["title"], BLUEPRINT_STATUS[b["draft route"]], links, "Course"))
        sections.append((topic, sorted(rows, key=lambda row: row[0].casefold())))

    assert used_editorial == set(EDITORIAL_BLUEPRINTS.glob("[0-9]*.md")), (
        "Unlinked editorial blueprints", set(EDITORIAL_BLUEPRINTS.glob("[0-9]*.md")) - used_editorial
    )
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
        "Browse by format. Within each format, titles are alphabetized by topic. Every entry has a Blueprint. Source links and planning status do not imply a promised release. Some sources require GitHub access. Local material is labeled.",
        "",
    ]
    if reading_rows:
        out.append(f"- [Read the public drafts](#read-the-public-drafts) ({len(reading_rows)})")
    out.extend(f"- [{name}](#{anchor(name)}) ({totals[fmt]})" for name, fmt, _ in formats)
    out += [
        "",
        "For production: [course and textbook queue](queue.tsv) · [syllabus blueprint index](syllabus-track/blueprints/) · [popular book and workshop inventory](other-formats.tsv) · [editorial blueprints](editorial-blueprints/) · [local Blueprint inventory](local-blueprints/) · [title repo migration](repo-migration/) · [source triage](source-triage.tsv) · [Codex handoff](../codex-handoff.md). A hold is planning only; no row implies rights clearance, publication, or enrollment.",
        "",
    ]
    if reading_rows:
        out += [
            "## Read the public drafts",
            "",
            "Start with a chapter or open the book for its full contents. These are working drafts; the planning statuses below describe source and production decisions.",
            "",
            "| Book | Start reading | What you will work on |",
            "| --- | --- | --- |",
        ]
        for title, base, chapter, chapter_title, focus in reading_rows:
            out.append(f"| [{cell(title)}]({base}) | [{chapter_title}]({base}/blob/main/{chapter}) | {focus} |")
        out.append("")
    for name, fmt, description in formats:
        out += [f"## {name}", "", description, ""]
        active = [(topic, [r for r in rows if r[3] == fmt]) for topic, rows in sections]
        active = [(topic, rows) for topic, rows in active if rows]
        prefix = {"Course": "", "Popular book": "Books: ", "Workshop": "Workshops: "}[fmt]
        out.extend(f"- [{topic}](#{anchor(prefix + topic)}) ({len(rows)})" for topic, rows in active)
        out.append("")
        for topic, rows in active:
            out += [f"### {prefix}{topic}", "", "| Title | Status | Blueprint and source material |", "| --- | --- | --- |"]
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
