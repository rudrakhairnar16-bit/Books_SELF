# DLD · Unit 1 — MCQs (all from material + exam-style extras)
> There is no separate Unit-1 MCQ file in the repo → included: the PPT exercise MCQs [PPT s76] + MCQs built from every slide/assignment topic.
> Format (used by the practice app): `### Qn.` question · options A–D · `**Ans: X**` — reason · `[source]` `#topic`

### Q1. 2×10¹ + 8×10⁰ is equal to
- A) 10
- B) 280
- C) 2.8
- D) 28
**Ans: D** — 20 + 8 = 28. `[PPT s76]` `#number-systems`

### Q2. The binary number 1101 is equal to the decimal number
- A) 13
- B) 49
- C) 11
- D) 3
**Ans: A** — 8 + 4 + 0 + 1 = 13. `[PPT s76]` `#conversion`

### Q3. The decimal 17 is equal to the binary number
- A) 10010
- B) 11000
- C) 10001
- D) 01001
**Ans: C** — 16 + 1. `[PPT s76]` `#conversion`

### Q4. The sum of 11010 + 01111 equals
- A) 101001
- B) 101010
- C) 110101
- D) 101000
**Ans: A** — 26 + 15 = 41 = 101001. `[PPT s76]` `#binary-arithmetic`

### Q5. Which gates are called universal gates?
- A) AND, OR
- B) NAND, NOR
- C) XOR, XNOR
- D) NOT, AND
**Ans: B** — any function can be built from NAND alone or NOR alone. `[PPT s12]` `#gates`

### Q6. The output of a NAND gate is 0 when
- A) all inputs are 0
- B) any input is 0
- C) all inputs are 1
- D) inputs are different
**Ans: C** — NAND = NOT(AND). `[PPT s15]` `#gates`

### Q7. The output of a NOR gate is 1 when
- A) all inputs are 0
- B) all inputs are 1
- C) any input is 1
- D) inputs are different
**Ans: A** — NOR = NOT(OR). `[PPT s15]` `#gates`

### Q8. The gate whose output is 1 only when its inputs are different is
- A) XNOR
- B) NAND
- C) XOR
- D) AND
**Ans: C** — A ⊕ B. `[PPT s15]` `#gates`

### Q9. The XNOR gate is also known as
- A) inverter
- B) equality (coincidence) detector
- C) parity generator for odd parity
- D) universal gate
**Ans: B** — output 1 when A = B. `[PPT s16]` `#gates`

### Q10. IC 7400 contains
- A) quad 2-input AND gates
- B) quad 2-input NAND gates
- C) hex inverters
- D) quad 2-input NOR gates
**Ans: B** — 7408 AND, 7404 NOT, 7402 NOR, 7432 OR, 7486 XOR. `[SYL: examples of IC gates]` `#gates`

### Q11. How many NAND gates are required to make an OR gate?
- A) 1
- B) 2
- C) 3
- D) 4
**Ans: C** — invert both inputs (2) + one NAND. `[notes §2]` `#universal`

### Q12. How many NOR gates are required to make an AND gate?
- A) 1
- B) 2
- C) 3
- D) 4
**Ans: C** — invert both inputs (2) + one NOR. `#universal`

### Q13. How many NAND gates are needed to build an XOR gate (minimum)?
- A) 2
- B) 3
- C) 4
- D) 5
**Ans: C** — the standard 4-NAND XOR. `#universal`

### Q14. A truth table for a 4-input gate has how many rows?
- A) 4
- B) 8
- C) 16
- D) 32
**Ans: C** — 2⁴. `[PPT s17, s20]` `#boolean`

### Q15. According to De Morgan's theorem, (A·B)' =
- A) A'·B'
- B) A' + B'
- C) A + B
- D) (A + B)'
**Ans: B** — break the bar, change the sign. `[PPT s32-33]` `#boolean`

### Q16. A + AB simplifies to
- A) B
- B) AB
- C) A
- D) A + B
**Ans: C** — absorption law. `[PPT s31]` `#boolean`

### Q17. A + A'B simplifies to
- A) A
- B) A + B
- C) AB
- D) A'B
**Ans: B** — (A + A')(A + B) = A + B. `#boolean`

### Q18. Which law states A + BC = (A + B)(A + C)?
- A) Associative
- B) Commutative
- C) Distributive
- D) Absorption
**Ans: C** — distributive law (b) form. `[PPT s30]` `#boolean`

### Q19. A Boolean expression that is always true is called
- A) fallacy
- B) tautology
- C) duality
- D) contradiction
**Ans: B** — always 1. `[PPT s22]` `#boolean`

### Q20. The dual of A + 0 = A is
- A) A·0 = 0
- B) A·1 = A
- C) A + 1 = 1
- D) A·A' = 0
**Ans: B** — swap + ↔ · and 0 ↔ 1. `#boolean`

### Q21. P + (PQ)' is a
- A) fallacy
- B) tautology
- C) neither
- D) contingency equal to P
**Ans: B** — = P + P' + Q' = 1. `[PPT s23]` `#boolean`

### Q22. The radix of the octal number system is
- A) 2
- B) 8
- C) 10
- D) 16
**Ans: B** — digits 0–7. `[PPT s47]` `#number-systems`

### Q23. (101011)₂ in decimal is
- A) 41
- B) 43
- C) 45
- D) 53
**Ans: B** — 32 + 8 + 2 + 1. `[HW p1]` `#conversion`

### Q24. (145)₁₀ in binary is
- A) 10010001
- B) 10001001
- C) 10100001
- D) 11000001
**Ans: A** — 128 + 16 + 1. `[HW p1]` `#conversion`

### Q25. (1032)₁₀ in octal is
- A) (2001)₈
- B) (2010)₈
- C) (1020)₈
- D) (2100)₈
**Ans: B** — 2×512 + 0 + 1×8 + 0. `[HW p4]` `#conversion`

### Q26. (5BC)₁₆ in decimal is
- A) 1468
- B) 1486
- C) 1648
- D) 1386
**Ans: A** — 5×256 + 11×16 + 12. `[HW p10]` `#conversion`

### Q27. (3674)₈ in binary is
- A) 011 110 111 100
- B) 011 110 110 100
- C) 111 110 111 100
- D) 011 111 110 100
**Ans: A** — each octal digit → 3 bits. `[HW p7]` `#conversion`

### Q28. (1111101110101111)₂ in hexadecimal is
- A) FBAF
- B) FABF
- C) FBBF
- D) EBAF
**Ans: A** — 1111 1011 1010 1111. `[HW p12]` `#conversion`

### Q29. (0.6875)₁₀ in octal is
- A) 0.45
- B) 0.54
- C) 0.55
- D) 0.64
**Ans: B** — .6875×8 = 5.5 → 5; .5×8 = 4.0 → 4. `[HW p5]` `#conversion`

### Q30. (81.21)₁₆ in decimal is
- A) 129.1328
- B) 129.12890625
- C) 129.21
- D) 81.13
**Ans: B** — 128 + 1 + 2/16 + 1/256. (The handwritten notes wrongly show 129.1328.) `[HW p9]` `#conversion`

### Q31. 1's complement of 11011010 is
- A) 00100110
- B) 00100101
- C) 11011011
- D) 00100100
**Ans: B** — flip every bit. `[ASG Q10]` `#complements`

### Q32. 2's complement of 10000101 is
- A) 01111010
- B) 01111011
- C) 10000110
- D) 01111100
**Ans: B** — 1's (01111010) + 1. `[ASG Q10]` `#complements`

### Q33. In 2's complement subtraction, if a final carry is produced, the result is
- A) negative; re-complement it
- B) positive; discard the carry
- C) positive; add the carry to the LSB
- D) an overflow
**Ans: B** — the end-around carry belongs to 1's complement, not 2's. `[PPT s67]` `#complements`

### Q34. In 1's complement subtraction, the end-around carry is
- A) discarded
- B) added to the LSB of the result
- C) the sign bit
- D) ignored only for negative results
**Ans: B** — then the result is positive. `[PPT s63-65]` `#complements`

### Q35. The 9's complement of 2468 is
- A) 7532
- B) 7531
- C) 8642
- D) 7542
**Ans: B** — 9999 − 2468; the 10's complement is 7532. `[SYL r's/(r−1)'s]` `#complements`

### Q36. The range of an 8-bit 2's complement number is
- A) −127 to +127
- B) −128 to +127
- C) −128 to +128
- D) 0 to 255
**Ans: B** — −2⁷ to 2⁷ − 1. `[SYL signed binary]` `#signed`

### Q37. −25 in 8-bit 2's complement is
- A) 10011001
- B) 11100110
- C) 11100111
- D) 11100101
**Ans: C** — 25 = 00011001 → flip 11100110 → +1. `#signed`

### Q38. Which representation has two zeros (+0 and −0)?
- A) only 2's complement
- B) sign-magnitude and 1's complement
- C) only sign-magnitude
- D) none
**Ans: B** — 2's complement has a single zero. `#signed`

### Q39. Which of the following is an invalid (forbidden) BCD code?
- A) 1001
- B) 0111
- C) 1010
- D) 0000
**Ans: C** — 1010–1111 are invalid. `[PPT s72]` `#codes`

### Q40. In BCD addition, a correction of ___ is added when the sum exceeds 9 or produces a carry.
- A) 0011
- B) 0110
- C) 1001
- D) 1010
**Ans: B** — add 6. `[PPT s73]` `#codes`

### Q41. (59)₁₀ in BCD is
- A) 111011
- B) 0101 1001
- C) 1000 1100
- D) 0101 1010
**Ans: B** — C is Excess-3, A is pure binary. `#codes`

### Q42. Gray code of binary 1011 is
- A) 1101
- B) 1110
- C) 1010
- D) 1111
**Ans: B** — 1, 1⊕0, 0⊕1, 1⊕1. `[SYL codes]` `#codes`

### Q43. Excess-3 code of decimal 5 is
- A) 0101
- B) 1000
- C) 0110
- D) 1011
**Ans: B** — 5 + 3 = 8. `#codes`

### Q44. ASCII is a ___ code.
- A) 6-bit
- B) 7-bit
- C) 8-bit
- D) 16-bit
**Ans: B** — EBCDIC is 8-bit. `[PPT s75]` `#codes`

### Q45. A parity bit can
- A) detect and correct single-bit errors
- B) detect single-bit errors only
- C) detect all 2-bit errors
- D) correct burst errors
**Ans: B** — no correction. `[ASG Q4]` `#error-codes`

### Q46. Hamming code can
- A) only detect errors
- B) detect and correct single-bit errors
- C) correct 2-bit errors
- D) not detect any error
**Ans: B** — the syndrome gives the error position. `[ASG Q4]` `#error-codes`

### Q47. Minimum number of parity bits for 4 data bits in Hamming code is
- A) 2
- B) 3
- C) 4
- D) 5
**Ans: B** — 2ᵖ ≥ m + p + 1 → 8 ≥ 8. `#error-codes`

### Q48. In the checksum method, the receiver detects no error when the complemented sum is
- A) all 1s
- B) all 0s
- C) equal to the data
- D) odd
**Ans: B** — sum is 1111 → complement 0000. `[HW p18]` `#error-codes`

### Q49. A digital system whose state is updated at discrete clock times is
- A) combinational
- B) synchronous sequential
- C) asynchronous sequential
- D) analog
**Ans: B** `[PPT s3]` `#digital-systems`

### Q50. A signal that is continuous in both value and time is
- A) digital
- B) analog
- C) synchronous
- D) binary
**Ans: B** `[PPT s6]` `#digital-systems`

### Q51. 1011 × 110 equals
- A) 1000010
- B) 1000110
- C) 1100010
- D) 1000011
**Ans: A** — 11 × 6 = 66. `[PPT s70]` `#binary-arithmetic`

### Q52. 10010 ÷ 10 equals
- A) 1010
- B) 1001
- C) 0110
- D) 1100
**Ans: B** — 18 ÷ 2 = 9. `[HW p17, ASG Q8]` `#binary-arithmetic`
