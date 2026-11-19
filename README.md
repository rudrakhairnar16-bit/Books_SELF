# Books_SELF — Semester 3 study material + Personal Mentor System

`SEM3/` = original college material (DBMS, DLD, DS, Maths-III, Python). **Never modified.**
`study_engine/` = the mentor's brain & tools. `study/` = everything produced for the student.

## Start here
| File | Purpose |
|---|---|
| [`study_engine/BRAIN.md`](study_engine/BRAIN.md) | 🧠 Master rules — the mentor reads this first every session |
| [`study_engine/DECISION_ENGINE.md`](study_engine/DECISION_ENGINE.md) | ⚙️ How to decide what to study, when to revise, which tool to use |
| [`study_engine/SOURCE_MAP.md`](study_engine/SOURCE_MAP.md) | 🗂️ Every material file mapped to subject → unit (books excluded) |
| [`study_engine/PROGRESS.md`](study_engine/PROGRESS.md) | 📊 Dashboard: exam countdown, scores, weak units, due revisions |
| [`study/00_GENERAL/`](study/00_GENERAL) | How to write answers for 1–10 marks (notes + handwritten pages) |

## Tools (`python3 study_engine/tools/...`, run from repo root; `pip install -r study_engine/requirements.txt`)
- `extract.py` – extract text from all non-book PDFs → `study_engine/extracted/`
- `render_pages.py <pdf> [3-7]` – render scanned pages to PNG for reading
- `handwritten.py notes.hw out/prefix` – make notebook-style handwritten note images
- `tracker.py dashboard | due | next | log | status | exam | addsubject | addunit` – progress, weak areas, spaced revision

## Per-unit study package
`study/<SUBJECT>/<NN>_<Unit>/` → lesson plan · class notes · handwritten pages · diagrams · flashcards (Anki CSV) ·
all MCQs · all questions by marks (1/2/3/4/5/7/10) with model answers · practical/viva · cheat-sheet · revision tests.
