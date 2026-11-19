# ⚙️ DECISION ENGINE — How the mentor decides *what*, *when* and *how*
> Companion to `BRAIN.md`. BRAIN = rules. This file = decision procedures. Follow top-to-bottom.

---

## 1. Mode selection — based on days left to the subject's exam
| Days left | Mode | What we do |
|-----------|------|------------|
| > 21 | **DEEP LEARN** | Full protocol per unit, all deliverables, 1 unit/day/subject. |
| 8 – 21 | **EXAM FOCUS** | Full package but answers prioritised by ⭐ frequency; tests every 2 units. |
| 3 – 7 | **CRASH** | Cheat-sheets + ⭐ questions + all MCQs + 1 full mock paper/subject. Skip low-weight theory. |
| 1 – 2 | **LAST MOMENT** | Only cheat-sheets, flashcards, formula sheets, weak-area drill, 1 timed mock. No new topics unless weightage ≥ 15 %. |
| Exam day | **CALM** | 30-min flashcard skim + answer-writing guide. Nothing new. |

## 2. Which subject / unit next? (priority score)
For every not-mastered unit compute:
```
priority = 3*urgency + 2*weightage + 2*weakness + 1*frequency − 1*mastery
urgency   = 5 if exam ≤3 days, 4 if ≤7, 3 if ≤14, 2 if ≤21, else 1
weightage = syllabus % / 5        (e.g. 20 % → 4)       (unknown → 3)
weakness  = 5 − confidence (0-5) from progress.json
frequency = number of sources asking questions on this unit (cap 5)
mastery   = 5 if last test ≥ 80 %, 3 if 60-79 %, 0 otherwise
```
Pick the highest score. Ties → the unit that is a **prerequisite** for others (e.g. DLD U1 before U2, DBMS U2 before U5, DS arrays before linked lists, Maths probability before distributions).
`tracker.py next` prints this ranking automatically.

## 3. Weak-area rules
- Test score **< 60 %** → topic = **WEAK** → re-teach with a different method (more examples / diagrams / analogy) → retest next day.
- **60–79 %** → **SHAKY** → targeted drill on the missed questions, retest in 3 days.
- **≥ 80 %** → **STRONG** → spaced revision only.
- Same mistake twice → add to the “Mistake Book” (`study/<SUBJECT>/MISTAKE_BOOK.md`) and to flashcards.
- Every session: ≥ 20 % of time on WEAK topics (if any exist).

## 4. Revision schedule (spaced repetition)
After a unit is first learned: revise on **Day +1, +3, +7, +14** (compressed to +1, +2, +4 if the exam is < 10 days away).
Each revision = 10 flashcards + 5 MCQs + 1 long question, from the due unit. Score decides the next interval:
`≥80 % → next step` · `60–79 % → repeat same interval` · `<60 % → reset to +1 and mark WEAK`.
Full-length **mock paper** per subject 2–4 days before its exam.

## 5. Tool / model selection (use the best tool for each job)
| Job | Tool | Why |
|-----|------|-----|
| Teaching, notes, model answers, grading | Mentor's own reasoning (verified) | Accuracy + exam-style language |
| Reading text PDFs | `tools/extract.py` (PyMuPDF) → `study_engine/extracted/` | Fast, exact |
| Reading scanned/handwritten PDFs | `tools/render_pages.py` → view PNG pages | Many Maths & DLD files are scans |
| Handwritten-style notes | `tools/handwritten.py` | Real handwriting look with exact text |
| Circuits / K-maps / trees / ER / graphs / plots | Python: matplotlib (+ schemdraw for logic gates) | Precise diagrams |
| Verify SQL | sqlite3 in Python | Run every query that is runnable |
| Verify Python / C code | run it in sandbox | Zero code errors in notes |
| Verify Maths numericals | Python (fractions/scipy-style calc) | No arithmetic slips |
| Concept illustrations / mnemonic pictures | `generate_image` (no text-heavy content) | Memory aids only |
| Audio revision ("listen while travelling") | `generate_speech` (optional, on request) | Passive revision |
| Flashcards | CSV (Anki import, `;` separator) + markdown | Works on phone with Anki/AnkiDroid |
| Interactive practice | self-contained HTML quiz/flashcard page per subject | Self-testing with score |

## 6. Coverage decision (Rule R3) — how to guarantee “every question”
1. Grep all extracted text + visually read scans for the unit → build the **coverage checklist** in `00_lesson_plan.md`.
2. Classify marks: use the marks printed in the source; if missing → infer by verb:
   `Define/List/State/full-form → 1–2 m` · `Explain/Differentiate/short note → 3–5 m` ·
   `Explain with diagram/example, Design, Derive, Algorithm, numericals with multiple parts → 7 m` · `Discuss in detail / complete design / long numericals → 10 m`.
   Important questions also get a short 3-mark version, so the student can answer them for any number of marks.
3. Tick each checklist item only when its model answer exists in `06_question_bank.md` / `05_mcqs.md`.
4. Unit is “done” only when the checklist is 100 % ticked.

## 7. Session time-boxing (default 2-hr block, scale as needed)
`10 min due revision → 70 min teach + practice → 25 min test → 10 min log + next plan` · 5-min break every 25–30 min (Pomodoro).

## 8. When something is unclear
- Ambiguous syllabus/unit numbering (e.g. DS units renumbered vs. old syllabus) → follow the **latest** syllabus/mid-sem sheet.
- Missing exam dates/time → ask the student once, record in `progress.json`.
- Conflicting answers between sources → use the standard textbook-correct answer, note it in BRAIN §8.
