# DLD — Digital Logic Design · Subject Master Plan
**Exam:** End-semester theory 70 m (3 h) + viva · **Internal:** Att 5 + Asg 5 + Mid 20 · **Student time:** 4–5 h/day
**Exam date:** ❓ *not given yet* → tell the mentor; it switches the mode automatically (DECISION_ENGINE §1).

## Units, weightage & material strength
| Unit | Topic | Wt | Material in repo | Source Qs to cover | Status |
|------|-------|----|------------------|--------------------|--------|
| 1 | Number systems & logic gates | 15 % | PPT 76 sl + 18 HW pages + Asg | Asg Q1–13 (50+ numericals), PPT exercises | ✅ package ready |
| 2 | Boolean simplification (K-map, VEM, NAND/NOR) | 20 % | PPT 36 sl + 13 HW pages + Asg M2 | Asg M2 Q1–6 (13 K-maps) | ⏭ next |
| 3 | Combinational circuits | 15 % | PPT 62 sl + 27 HW pages + CLA | **QB 10 Qs + 51 MCQs** + Asg M3 Q1–6 | ⏳ |
| 4 | Sequential circuits (flip-flops) | 20 % | PPT 52 sl + 20 HW pages | **QB 7 Qs + 46 MCQs** | ⏳ |
| 5 | Registers & counters | 15 % | notes 22 p + 19 HW pages | **QB 6 Qs + 55 MCQs** | ⏳ |
| 6 | A/D & D/A converters | 15 % | ⚠ **nothing in repo** | syllabus only | ⏳ (mentor notes from standard knowledge) |

## Teaching order (prerequisite chain) & time budget
`U1 → U2 → U3 → U4 → U5 → U6` (each builds on the previous one: gates → simplification → circuits → memory → registers/counters).
| Day | Block 1 (2 h) | Block 2 (2 h) | 30 min |
|-----|---------------|---------------|--------|
| D1 | U1 §1–5 | U1 §6–9 + MCQs | U1 Test 1 |
| D2 | U2 K-maps (SOP/POS, 2–5 var) | U2 don't-care, VEM, NAND/NOR + Asg M2 | U1 revision (+1 day) |
| D3 | U3 MUX/DEMUX/decoder/encoder | U3 adders/subtractors/CLA/parity/code conv/QM | U2 test |
| D4 | U4 latches/FF/excitation tables | U4 race-around, M-S JK, FF conversion, design | U3 test + U1 rev (+3) |
| D5 | U5 shift registers | U5 ripple/sync counters, ring/Johnson, design | U4 test |
| D6 | U6 DAC/ADC | Full mock paper (70 m, 3 h) | U5/U6 test |
| D7+ | Weak-area drill (tracker `next`) | 2nd mock | flashcards |
*If the exam is closer than 7 days → CRASH mode: cheat-sheets + ⭐ questions + all MCQs first.*

## ⭐ Most-repeated / must-do questions (from QB + assignments)
- U1: gates + universal realizations (7 m), error detecting & correcting codes (7 m), complement subtraction, conversions
- U2: K-map SOP/POS with don't cares, NAND/NOR-only implementation, VEM
- U3: MUX/DEMUX, encoder/decoder/priority encoder, HA/FA/HS/FS, CLA, parity generator/checker, QM method
- U4: SR/JK/D/T with characteristic tables & equations, race-around + master-slave JK, FF conversions (JK→T, SR→D)
- U5: SISO, bidirectional shift register, Johnson counter, ripple counter, sync down counter with T-FF, ripple up counter with JK

## Viva
Every unit's `07_practicals_viva.md` + IC pin-outs (7400/02/04/08/32/86, 74153 MUX, 74138 decoder, 7476 JK, 7474 D, 7490/7493 counters, 7495 shift register).

## Files
`practice.html` (all units' MCQs + flashcards, rebuild: `python3 study_engine/tools/build_practice.py DLD`) · `MISTAKE_BOOK.md` · unit folders `NN_*`.
