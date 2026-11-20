# DLD · Unit 1 — Complete Question Bank (1 → 10 marks) with Model Answers
> Covers **every** Unit-1 question in the material + likely end-sem questions on syllabus topics.
> Source tags: **[ASG Qn]** = `DLD Assignment_1.pdf` · **[PPT sN]** = `Unit-1 ppt.pdf` slide · **[HW pN]** = `Unit 1 Solved Examples.pdf` page ·
> **[SYL]** = syllabus topic (no source question, likely to be asked) · ⭐ = high probability.
> All numerical answers were **checked with Python**.
> Marks are not printed in the assignment, so they're inferred from the question verb (DECISION_ENGINE §6). Long answers give short versions for fewer marks.

---
## SECTION A — 1 mark (one line)
| # | Question | Answer |
|---|----------|--------|
| 1 | What is the radix of the hexadecimal system? [SYL] | 16 |
| 2 | How many rows does a truth table with 4 variables have? [PPT s20] | 2⁴ = 16 |
| 3 | Name the universal gates. [PPT s12] | NAND and NOR |
| 4 | Which gate gives output 1 only when all inputs are 0? | NOR |
| 5 | Which gate is called the equality detector? | XNOR |
| 6 | IC number of the quad 2-input NAND gate? | 7400 |
| 7 | IC number of the XOR gate? | 7486 |
| 8 | Define tautology. [PPT s22] | A Boolean expression whose output is always 1 |
| 9 | Define fallacy. [PPT s22] | A Boolean expression whose output is always 0 |
| 10 | 2×10¹ + 8×10⁰ = ? (a)10 (b)280 (c)2.8 (d)28 [PPT s76] | (d) 28 |
| 11 | (1101)₂ = ? (a)13 (b)49 (c)11 (d)3 [PPT s76] | (a) 13 |
| 12 | (17)₁₀ = ? (a)10010 (b)11000 (c)10001 (d)01001 [PPT s76] | (c) 10001 |
| 13 | 11010 + 01111 = ? (a)101001 (b)101010 (c)110101 (d)101000 [PPT s76] | (a) 101001 (26+15 = 41) |
| 14 | How many bits are in a nibble? | 4 |
| 15 | ASCII is a ___-bit code. [PPT s75] | 7-bit |
| 16 | EBCDIC is a ___-bit code. [PPT s75] | 8-bit |
| 17 | Largest valid BCD digit code? [PPT s72] | 1001 |
| 18 | 1's complement of 1010? | 0101 |
| 19 | 2's complement of 0001? | 1111 |
| 20 | State the absorption law. [PPT s31] | A + AB = A ; A(A+B) = A |
| 21 | Who developed Boolean algebra? [PPT s18] | George Boole |
| 22 | A + A' = ? | 1 |
| 23 | Range of 8-bit 2's complement numbers? [SYL] | −128 to +127 |
| 24 | Which code changes only one bit between successive numbers? [SYL] | Gray code |

---
## SECTION B — 2 marks (2–3 lines + keyword)

**B1. Differentiate analog and digital signals. [PPT s5-6]**
Analog: continuous in value and time, noise-sensitive (e.g., microphone output). Digital: discrete (two levels, 0/1), noise-immune, easy to store and process (e.g., computer data).

**B2. Differentiate combinational and sequential systems. [PPT s3]**
Combinational: no memory, output = f(present inputs), e.g., adder. Sequential: has memory/state, output = f(inputs, present state), e.g., counter. Sequential can be synchronous (clocked) or asynchronous.

**B3. State De Morgan's theorems. ⭐ [ASG Q3]**
(A·B)' = A' + B' (complement of a product = sum of complements); (A+B)' = A'·B' (complement of a sum = product of complements).

**B4. Why are NAND and NOR called universal gates? ⭐ [PPT s12]**
Because NOT, AND and OR — and therefore any Boolean function — can be built using only NAND gates (or only NOR gates).

**B5. Define 1's and 2's complement with an example.**
1's complement = invert every bit: 1011 → 0100. 2's complement = 1's complement + 1: 0100 + 1 = 0101.

**B6. What are forbidden codes in BCD? [PPT s72]**
The 4-bit groups 1010, 1011, 1100, 1101, 1110, 1111 (decimal 10–15) are not valid BCD digits.

**B7. What is a parity bit? [SYL/ASG Q4]**
An extra bit added to data so that the total number of 1s is even (even parity) or odd (odd parity); used to detect single-bit errors.

**B8. Convert (25)₁₆ and (1D9)₁₆ to decimal. [HW p10]**
(25)₁₆ = 2×16 + 5 = **37** ; (1D9)₁₆ = 256 + 13×16 + 9 = **473**.

**B9. Convert (10011011101)₂ to hexadecimal. [HW p11]**
Group 4 bits from the right: 0100 1101 1101 → 4 D D → **(4DD)₁₆**.

**B10. State the duality principle.**
Any Boolean identity stays true if we interchange + with · and 0 with 1 (variables unchanged). E.g., A + 0 = A ↔ A·1 = A.

---
## SECTION C — 3 marks (definition + 2 points / short numerical)

**C1. Explain Digital Logic Design. [ASG Q1] ⭐**
*Definition:* DLD is the study of designing and analysing circuits that process **binary (discrete 0/1) signals** using logic gates.
- A **digital system** takes discrete inputs and an internal state and produces discrete outputs (block diagram: inputs → processing system ↔ state → outputs).
- Two classes: **combinational** (no memory: adders, MUX, decoders) and **sequential** (memory: flip-flops, registers, counters — synchronous or asynchronous).
- Basis: Boolean algebra, number systems, logic gates. *Applications:* computers, mobiles, digital watches, controllers.
*(For 5 marks add the analog-vs-digital table and the digital computer example: Input → CPU (control + datapath) ↔ memory → output.)*

**C2. Verify that P + (PQ)' is a tautology. [PPT s23]**
P + (PQ)' = P + P' + Q' (De Morgan) = 1 + Q' (complement law) = **1** (property of 1). Truth table:

| P | Q | PQ | (PQ)' | P+(PQ)' |
|---|---|----|-------|---------|
| 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 1 |
All 1s → tautology ✔

**C3. Evaluate using a truth table: (a) X'Y' + X'Y (b) X'YZ' + XY' (c) XY'(Z + YZ') + Z'. [PPT s23]**

| X | Y | Z | (a) X'Y'+X'Y | (b) X'YZ'+XY' | (c) XY'(Z+YZ')+Z' |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 | 1 |
| 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 |
(a) simplifies to X' · (c) simplifies to Z' + XY'.

**C4. Verify (X+Y)' = X'Y'. [PPT s23]** — 4-row truth table: (X+Y)' column = 1,0,0,0 and X'Y' column = 1,0,0,0 → equal ✔ (De Morgan's 2nd theorem).

**C5. Do as directed (octal addition). [ASG Q7]** *Rule: add in decimal per column; if ≥ 8, write (sum − 8) and carry 1.*
- (a) (162)₈ + (537)₈: 2+7 = 9 → 1 carry 1; 6+3+1 = 10 → 2 carry 1; 1+5+1 = 7 → **(721)₈**
- (b) (67.5)₈ + (45.6)₈: 5+6 = 11 → 3 c1; 7+5+1 = 13 → 5 c1; 6+4+1 = 11 → 3 c1 → **(135.3)₈**
- (c) (256)₈ + (565)₈: 6+5 = 11 → 3 c1; 5+6+1 = 12 → 4 c1; 2+5+1 = 8 → 0 c1 → **(1043)₈**

**C6. Obtain 1's and 2's complements. [ASG Q10]**

| Number | 1's complement | 2's complement |
|--------|---------------|----------------|
| (a) 00010000 | 11101111 | 11110000 |
| (b) 00000000 | 11111111 | 00000000 (carry discarded) |
| (c) 11011010 | 00100101 | 00100110 |
| (d) 10101010 | 01010101 | 01010110 |
| (e) 10000101 | 01111010 | 01111011 |
| (f) 11111111 | 00000000 | 00000001 |

**C7. Convert (19.11)₁₀ to octal. [HW p4]**
19 = 2×8 + 3 → (23)₈. Fraction: .11×8 = 0.88→0, .88×8 = 7.04→7, .04×8 = 0.32→0, .32×8 = 2.56→2, .56×8 = 4.48→4 → **(23.07024)₈**
*(The handwritten copy shows “0.4×8”; it should be 0.04×8 — the answer is still correct.)*

**C8. Convert (63.362)₁₀ to binary. [HW p2]** 63 = 111111; .362→0 (.724), 1 (.448), 0 (.896), 1 (.792), 1 (.584) → **(111111.01011)₂**

**C9. Convert (5386)₁₀ and (18.765625)₁₀ to hex. [HW p9]**
5386 ÷ 16 = 336 r10(A); 336 ÷ 16 = 21 r0; 21 ÷ 16 = 1 r5; 1 → **(150A)₁₆**.
18 = (12)₁₆; .765625×16 = 12.25→C; .25×16 = 4.0→4 → **(12.C4)₁₆**

---
## SECTION D — 4 marks (method + full working)

**D1. Add the binary numbers. [ASG Q5]** *(rule: 1+1 = 0 carry 1; 1+1+1 = 1 carry 1)*

| # | Sum | Answer | Check |
|---|-----|--------|-------|
| 1 | 1011 + 1101 | **11000** | 11 + 13 = 24 |
| 2 | 10101 + 11011 | **110000** | 21 + 27 = 48 |
| 3 | 110101 + 101011 | **1100000** | 53 + 43 = 96 |
| 4 | 1011011 + 1100110 | **11000001** | 91 + 102 = 193 |
| 5 | 11011010 + 10110111 | **110010001** | 218 + 183 = 401 |
| 6 | 111001 + 101111 | **1101000** | 57 + 47 = 104 |
| 7 | 1001101 + 1110101 | **11000010** | 77 + 117 = 194 |
| 8 | 11010110 + 10101101 | **110000011** | 214 + 173 = 387 |

Worked column method for #1:
```
  carry 1 1 1 1
        1 0 1 1
      + 1 1 0 1
      ---------
      1 1 0 0 0
```

**D2. Hexadecimal additions. [ASG Q13]** *(add per column in decimal; if ≥ 16, write sum − 16 and carry 1)*

| # | Sum | Answer |
|---|-----|--------|
| 1 | 2A5F + 1B3C | **459B** |
| 2 | 4C7A + 2D1F | **7999** |
| 3 | 7B26 + 15A9 | **90CF** |
| 4 | A35C + 2F47 | **D2A3** |
| 5 | 6D8B + 3A25 | **A7B0** |
| 6 | B4F2 + 1C7D | **D16F** |
| 7 | 8E3A + 2B6F | **B9A9** |
| 8 | D5A7 + 19C8 | **EF6F** |
Worked #1: F+C = 15+12 = 27 = 16+**11(B)** c1 · 5+3+1 = **9** · A+B = 21 = 16+**5** c1 · 2+1+1 = **4** → 459B.

**D3. Binary division. [ASG Q8]**
(a) 101101 ÷ 110 = 45 ÷ 6 = **111.1** (7.5) — long division: 110 into 1011 → 1 rem 101; bring 0 → 1010 → 1 rem 100; bring 1 → 1001 → 1 rem 11; bring 0 (fraction) → 110 → 1 rem 0.
(b) 10010 ÷ 11 = 18 ÷ 3 = **110** (6).

**D4. Binary multiplication. [ASG Q9]**
(a) 1011 × 1010 = **1101110** (11 × 10 = 110)
```
      1011
    × 1010
    ------
      0000
     1011
    0000
   1011
   -------
   1101110
```
(b) 101101 × 1100 = **1000011100** (45 × 12 = 540)

**D5. BCD addition: 8 + 7 and 18 + 2. [PPT s74]** — see notes §8.1 → 0001 0101 and 0010 0000 (add 0110 when > 9 or carry).

**D6. Explain the checksum method with an example. [HW p18]** — sender: add words, 1's complement = checksum; receiver: add all + checksum, complement = 0 → no error. Example data 0111, 0011 → checksum 0101; receiver sum 1111 → 0000 ✔ (full answer in notes §9.2).

**D7. Convert binary ↔ octal/hex. [HW p7, p11-12]**
(111110111110101)₂ = 011 111 011 110 101 = **(37365)₈** · (1101101.11001)₂ = **(155.62)₈** ·
(1111101110101111)₂ = **(FBAF)₁₆** · (9BC8)₁₆ = 1001 1011 1100 1000 · (6F.2F)₁₆ = 0110 1111 . 0010 1111.

**D8. Convert binary/octal to decimal. [HW p3, p6, p7]**
(101.11)₂ = 5.75 · (10101.0101)₂ = 21.3125 · (47)₈ = 39 · (2671)₈ = 1465 · (1534)₈ = 860 · (761.12)₈ = 497.15625.

---
## SECTION E — 5 marks

**E1. List the Boolean algebra laws. Explain De Morgan's laws. [ASG Q3] ⭐⭐**
1. *Boolean algebra* — the algebra of two values (0/1) by George Boole with the operators AND, OR, NOT.
2. Write the **T1–T10 table** (notes §3): 0 and 1 properties, commutative, associative, distributive, idempotence, absorption, complement, involution, De Morgan.
3. **De Morgan:** Th-1 (AB)' = A' + B'; Th-2 (A+B)' = A'B'. Give the **truth-table proof** (notes §3).
4. Gate meaning: NAND ≡ bubbled-OR, NOR ≡ bubbled-AND (draw both).
5. Use: simplification, converting circuits to NAND/NOR only. Example: (A + BC)' = A'(BC)' = A'(B' + C').

**E2. Binary subtraction. [ASG Q6]** *(“X from Y” means Y − X)*
- (a) 1111011.11 − 1010101.10 = **100110.01** (123.75 − 85.5 = 38.25)
- (b) 100 − 101 = **−1** (4 − 5): subtrahend is larger → compute 101 − 100 = 001 and put a minus sign
- (c) 1000 − 111 = **1** (8 − 7)
- (d) 101100.011 − 11010.101 = **10001.11** (44.375 − 26.625 = 17.75)

**E3. Subtract unsigned numbers using the 2's complement of the subtrahend. [ASG Q11] ⭐**
(pad both numbers to the same length first)

| | Problem | 2's of subtrahend | Sum | Carry? | Result |
|-|---------|-------------------|-----|--------|--------|
| a | 10011 − 10010 | 01110 | **1**00001 | yes → discard | **00001** (+1) |
| b | 100010 − 100110 | 011010 | 111100 | no → negative | −(2's of 111100) = **−000100** (−4) |
| c | 01001 − 11010 | 00110 | 01111 | no → negative | −(2's of 01111) = **−10001** (−17) |
| d | 101000 − 010101 | 101011 | **1**010011 | yes → discard | **010011** (+19) |

**E4. 1's complement subtraction. [ASG Q12]**
- (a) 10101 − 00101: 1's of 00101 = 11010; 10101 + 11010 = **1**01111 → end-around carry: 01111 + 1 = **10000** (21 − 5 = 16 ✔)
- (b) 11110 − 11100: 1's of 11100 = 00011; 11110 + 00011 = **1**00001 → 00001 + 1 = **00010** (30 − 28 = 2 ✔)

**E5. Explain r's and (r−1)'s complements with examples. [SYL] ⭐**
Definitions + formulas (rⁿ − N and rⁿ − 1 − N) + the 4-base table from notes §6.1 + one subtraction example in base 10 (72532 − 3250 using 10's complement = 69282) and one in base 2.

**E6. Explain signed-number representations. [SYL]** — sign-magnitude / 1's / 2's for −25, ranges, why 2's is preferred (single zero, simple adder), and the overflow example (notes §7).

**E7. Explain Gray code with binary↔Gray conversion. [SYL]** — notes §8.3 (1011 → 1110 → 1011, unit distance, applications).

---
## SECTION F — 7 marks

**F1. Demonstrate all basic and universal logic gates with their truth tables. [ASG Q2] ⭐⭐⭐**
*Answer plan (≈ 1.5 pages):*
1. **Definition** of a logic gate (1 output, ≥1 inputs, made of transistors/diodes, positive logic).
2. **Basic gates** — for AND, OR, NOT: symbol, expression, truth table, IC number, one application (alarm / doorbell / heater).
3. **Universal gates** — NAND, NOR: symbol, expression, truth table, IC.
4. **Why universal** + the realization diagrams of NOT, AND, OR using NAND only and NOR only (draw from `03_diagrams/universal_*.png`).
5. Mention **XOR/XNOR** (special gates) with truth tables for completeness.
6. Conclusion: NAND/NOR used to build any digital circuit → simpler manufacturing.

**F2. Explain error detecting and correcting codes in detail. [ASG Q4] ⭐⭐⭐**
1. Need: noise flips bits during transmission/storage → add redundancy.
2. **Parity (even/odd)** with an example + limitation (cannot detect even-count errors, no correction) + XOR generator.
3. **Checksum** with a full sender/receiver example.
4. **Hamming code**: formula 2ᵖ ≥ m + p + 1, positions 1/2/4, coverage sets, encode 1011 → 0110011, an error at bit 6 → syndrome 110 → corrected.
5. Comparison table (detect vs. correct).
*(For a 10-mark question add CRC basics: the sender appends the remainder of modulo-2 division by a generator polynomial; the receiver gets remainder 0 → no error.)*

**F3. Number-system conversions (any set of 4–6 conversions). [HW pages / SYL] ⭐⭐**
Typical paper question: “Convert (i) (163.362)₁₀ → binary, (ii) (2010.54)₈ ← (1032.6875)₁₀, (iii) (7CA3)₁₆ → decimal, (iv) (1101101.11001)₂ → octal & hex …”
Method + steps exactly like notes §4.1–4.3; final answers boxed.

---
## SECTION G — 10 marks (combination questions)

**G1. (a) Explain number systems and conversions with examples. (b) Perform 2's complement subtraction 5 − 12 and 10 − 8.** → notes §4 + §6.4.

**G2. (a) What are universal gates? Implement AND, OR, NOT, XOR using NAND only. (b) State and prove De Morgan's theorems.**
XOR using 4 NAND gates: let P = (AB)'; Y = ( (A·P)' · (B·P)' )' = A ⊕ B. (Draw: gate 1 makes P; gates 2 and 3 make (AP)' and (BP)'; gate 4 combines them.)

**G3. (a) Explain complements: r's and (r−1)'s. (b) Perform 1's and 2's complement subtraction (Assignment Q11/Q12 type). (c) Explain signed numbers and overflow.**

**G4. (a) Explain BCD, Excess-3 and Gray codes. (b) Explain parity and Hamming code with an example.**

---
## ✅ Coverage proof — every source question is answered above
| Source item | Where answered |
|-------------|----------------|
| ASG Q1 Explain DLD | C1 |
| ASG Q2 gates + truth tables | F1 |
| ASG Q3 laws + De Morgan | B3, E1 |
| ASG Q4 error detecting/correcting codes | B7, D6, F2 |
| ASG Q5 (8 additions) | D1 |
| ASG Q6 (a–d) binary subtraction | E2 |
| ASG Q7 (a–c) octal addition | C5 |
| ASG Q8 (a,b) division | D3 |
| ASG Q9 (a,b) multiplication | D4 |
| ASG Q10 (a–f) complements | C6 |
| ASG Q11 (a–d) 2's comp subtraction | E3 |
| ASG Q12 (a,b) 1's comp subtraction | E4 |
| ASG Q13 (8 hex additions) | D2 |
| PPT s23 exercise 1(a,b,c), 2, 3 | C3, C2, C4 |
| PPT s76 exercise MCQ 1–4 | A10–A13 |
| PPT examples (51, 217, 8023 → binary; 2479.859 → hex; BCD 8+7, 18+2) | notes §4, §8; 05_mcqs |
| HW pp1–18 all conversions, arithmetic, complements, checksum | C7–C9, D7, D8, notes §4–§9 |
