# DLD · Unit 1 — Viva Questions (+ lab link)
> DLD has no separate lab file in the repo. The common lab experiment for this unit is **“Verify the truth tables of logic gates using ICs 7400/7402/7404/7408/7432/7486”**
> and **“Realize basic gates using universal gates”**. These viva questions cover the experiment + theory.

## Lab procedure (say this if asked “How did you verify the gates?”)
1. Place the IC on the breadboard/trainer kit; connect **pin 14 = Vcc (+5 V)** and **pin 7 = GND** (all 14-pin 74xx gate ICs).
2. Apply inputs through switches (logic 1 = +5 V, 0 = GND); observe the output on an LED.
3. Record the output for all 2ⁿ input combinations → compare with the truth table.
4. ⚠ In the 7402 (NOR) the pinout is reversed — the output is on pin 1 and the inputs on pins 2 and 3 (in other ICs, inputs are on 1 and 2, output on 3).

## Rapid-fire viva (answer in 1 line)
1. What is a logic gate? → A circuit with one or more inputs and one output performing a logical operation.
2. Why are NAND/NOR universal? → Any Boolean function can be built using only them.
3. Which IC is a hex inverter? → 7404 (6 NOT gates).
4. How many gates are in a 7400? → 4 two-input NAND gates (quad).
5. Vcc and GND pins of 74xx gate ICs? → 14 and 7.
6. What is TTL? → Transistor–Transistor Logic, the 74xx family, 5 V supply.
7. Logic levels for TTL? → 0: 0–0.8 V, 1: 2–5 V.
8. Which gate is used as a parity generator? → XOR.
9. Which gate is an equality comparator? → XNOR.
10. What happens if a TTL input is left open? → It behaves as logic 1 (floating HIGH) — bad practice.
11. State De Morgan's theorems. → (AB)' = A' + B', (A+B)' = A'B'.
12. What is a bubbled OR? → An OR with inverted inputs = NAND.
13. Define radix. → The number of digits in a number system.
14. Why do computers use binary? → Two stable states are easy to build with transistors (ON/OFF) and are noise-immune.
15. Why use hexadecimal? → Compact way to write binary (1 hex digit = 4 bits).
16. 1's vs 2's complement? → Flip bits vs. flip + 1; 2's has a single zero.
17. Why is 2's complement used in computers? → Subtraction becomes addition; single zero; no end-around carry.
18. What is overflow? → The result exceeds the range of the available bits.
19. What is BCD? → Each decimal digit coded in 4-bit binary.
20. Difference between BCD and binary? → BCD codes each digit separately; binary codes the whole number.
21. Why is Gray code used? → Only one bit changes → no false intermediate states (encoders).
22. What is Excess-3? → BCD + 3; self-complementing.
23. ASCII full form and bits? → American Standard Code for Information Interchange, 7 bits.
24. What is parity? → An extra bit to make the count of 1s even/odd for error detection.
25. Can parity correct an error? → No, it only detects odd-count errors.
26. Which code corrects errors? → Hamming code (single-bit).
27. What is a nibble? A byte? → 4 bits, 8 bits.
28. MSB / LSB? → Most / least significant bit (leftmost / rightmost).
29. Analog vs digital? → Continuous vs discrete.
30. What is a tautology? → An expression that is always 1.
31. Positive vs negative logic? → Positive: HIGH = 1; negative: HIGH = 0.
32. What is the fan-out of a gate? → The number of gate inputs one output can drive (≈10 for standard TTL).
33. What is propagation delay? → The time between an input change and the output change (~10 ns for TTL).
34. Can XOR be universal? → No — it cannot produce constant outputs/AND from itself alone.
35. Minimum NAND gates for XOR? → 4.
