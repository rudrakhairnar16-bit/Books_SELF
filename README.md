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
- `build_practice.py SUBJ` – build `study/SUBJ/practice.html` (offline flashcards + MCQ quiz with weak-topic report)
- `build_lesson.py lesson.md` – lesson markdown → one self-contained HTML page with all diagrams + handwritten pages embedded
- `tracker.py dashboard | due | next | log | status | exam | addsubject | addunit` – progress, weak areas, spaced revision

## Per-unit study package
`study/<SUBJECT>/<NN>_<Unit>/` → lesson plan · class notes · handwritten pages · diagrams · flashcards (Anki CSV) ·
all MCQs · all questions by marks (1/2/3/4/5/7/10) with model answers · practical/viva · cheat-sheet · revision tests.

## 📝 Original brief (the student's prompt that started this system)
> *Reconstructed from the session record; the student can replace it with the exact wording.*

Act as my **professional mentor and professor**. Analyse this repo, fork it, and **teach me from scratch, subject by subject** (I'll name the subjects and add the remaining ones later).
- Use **ALL modules / material EXCEPT books**: PPTs / unit notes, assignments, MCQs, question banks.
- When starting a topic, cover **all MCQs and all questions from 1 to 10 marks** drawn from all of that subject's material.
- Provide **class notes, handwritten-notes images, flashcards** and more.
- **Schedule and manage timely revision tests and sessions**, and focus on my **weak areas**. My exams are very near.
- Create a **"brain" file** for yourself that saves all the rules, plus a file that helps you **make decisions and rules** (combined or separate).
- Use the best models / tools for study.

**My answers to the mentor (2026-11-19):** start with **DLD** · preparing for **end-semester theory exams + viva** · **4–5 hours/day** · I attended classes but I'm weak → fast basics, then heavy exam practice.
**2026-11-20:** "Teach me in this chat, topic by topic, from start to end."
