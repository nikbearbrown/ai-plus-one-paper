# Game Reinforcement Learning (AI Plus One)

**Queue #14 · Route: `hold` · Existing local Blueprint · Repository handoff only**

The full Phase 0 Blueprint already exists under the local source root
`game-reinforcement-learning`, in `manuscript/`. This entry locates it; it
does not replace, republish, or approve the author’s plan. The
[planning-file fingerprints](sources.tsv) identify the inspected snapshot.

## What already exists

| Source-root relative path | Role |
|---|---|
| `manuscript/BLUEPRINT.md` | Governing local summary and the author's recorded two-volume decisions |
| `manuscript/vision.md` and `manuscript/architecture.md` | Reader, thesis, prerequisites, learning progression and assessment plan |
| `manuscript/chapters-spec.md` and `manuscript/outline.md` | Planned chapters and activities, with the older draft-to-outline crosswalk |
| `manuscript/risks.md` and `manuscript/STATUS.md` | Scope limits and authoritative gate state |
| `manuscript/planning/chapter-playability-map.md` | Delivery inventory for the earlier twenty-chapter draft sequence |

**Planned:** 25 numbered chapters, in two volumes (13 foundations, 12 deep and
applied), plus the separate imitation-learning Appendix F. The foundations
volume moves from bandits, finite MDPs and exact planning to learning from
play, approximation and policy gradients. The second volume has its own
bridge and proceeds through neural methods, control, search, cooperation,
player modeling, deployment, and a capstone. The book tests when learning is
worth using instead of a simpler scripted game opponent or policy.

**Present:** 20 earlier draft Markdown chapters; these do not equal 25 revised
chapters. The existing crosswalk accounts for proposed merges, splits and
new chapters. The earlier chapter map reports 12 implemented activities,
only one with recorded actual browser visual and interaction QA (Pixel
Courier). Its record distinguishes the trained courier from precomputed
policy lookup in the browser. A tested headless algorithm, future engine
port, or a shared game shell is not equivalent to a playable chapter. These
are source-reported statuses; no games, training, or browser checks were rerun
for this handoff.

## Keep on hold

- Read the existing plan as a unit and preserve its two-volume decisions.
  Planning was back-filled after the drafts; `manuscript/STATUS.md` leaves
  Gate 0 unsigned. Queue placement and file hashes are not sign-off.
- Preserve one meaningful game activity per chapter. Use familiar, original
  examples to introduce the problem before the mathematics, work the update by
  hand, compare against an explicit scripted or exact baseline, and report
  independent checks. Keep learning cost separate from inference, memory and
  game-tick costs; label precomputation and test on target hardware before
  promising live performance. Record reward incentives, bounded behavior
  and a safe fallback where the game requires them.
- Keep distinct from **Game AI in Godot**, which covers broader game behavior
  design, and the **Game Artificial Intelligence** planning skill. Reuse only
  clearly permissioned shared scaffolding where it serves a tested RL learning
  objective. Do not infer a single new book from overlapping course or
  reference titles.
- Use existing course material only as privately documented provenance,
  not as transferable content. No course export, third-party text, student
  material, draft prose, original media, or game assets are included in this
  handoff. Confirm selected text/code and contributor rights separately
  before any transfer. Player examples are synthetic unless independently
  authorized; simulations are not evidence of human behavior. The recorded
  eventual release intent does not authorize any release now.
