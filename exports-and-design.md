# Draft exports and design profiles

The chapter and its figure sources stay editable in Markdown and source assets. Export an instructor-review proof from a named revision. After the expert edits it, rebuild the formats from that revised source. Producing a file or serving a draft through MCP does not publish anything or sign a gate.

| Target | What exists now |
| --- | --- |
| Markdown | Native chapter source; the current build also combines chapter Markdown. |
| EPUB and standalone HTML | The [current book build](https://github.com/nikbearbrown/ai1-cli/blob/main/build.sh) targets EPUB 3 and HTML5 through Pandoc and supplies Kindle CSS. HTML can be opened as a web page without deploying a site. |
| LaTeX | Pandoc generated standalone LaTeX from the synthetic chapter. The current book build does not include LaTeX as a default target. This test did not compile a PDF. |
| IMSCC | [AI+1’s Canvas build](https://github.com/nikbearbrown/ai1-cli/blob/main/build-canvas.sh) calls [the Common Cartridge 1.3 builder](https://github.com/nikbearbrown/ai1-cli/blob/main/build-imscc-standard.py). A one-module, one-page synthetic package had a readable root manifest and HTML resource. No Canvas import or feature parity was tested. |
| Multi-page React/Next.js site | [The wrapper](https://github.com/nikbearbrown/ai1-cli/blob/main/build-site.sh) points to [a stub](https://github.com/nikbearbrown/ai1-cli/blob/main/build-react-site.py). Keep this distinct from existing standalone HTML output. |

Local smoke test: used the identical [synthetic chapter](pilot-chapter.md) as Markdown and produced EPUB, HTML and LaTeX with existing Pandoc format writers plus IMSCC with the current Canvas build. Checked that all five outputs existed, that the EPUB and IMSCC ZIPs passed integrity checks, and that the IMSCC manifest parsed. The outputs were scratch proofs, not reviewed editions, deployed pages or a Canvas readiness claim.

## Default design and custom design

AI+1's default is the existing Brutalist visual system: [brutalist/DESIGN.md](https://github.com/nikbearbrown/ai1-cli/blob/main/brutalist/DESIGN.md) defines palette, typography, layout, and contrast, with a [Conductor design copy](https://github.com/nikbearbrown/ai1-cli/blob/main/conductor/design/DESIGN.md) used for figure work. The proposed workflow accepts an instructor-provided design profile containing typography, color roles, spacing, and figure rules. Apply it to the export or course workspace, not the canonical textbook or global defaults. Record the selected profile and the target-specific settings used to translate it.

The profile is a design contract, not a universal theme switch. Today the book build points to specific stylesheets; a `DESIGN.md` change alone is not proof that EPUB, web, LaTeX, or Canvas will inherit it. Apply compatible CSS or templates per target, check readability and contrast, and report what the target cannot preserve. Each figure needs a readable static fallback, a caption and alt text. Web may offer a checked interactive version; the export should remain useful without it. Keep instructor-only materials out of student-facing packages.
