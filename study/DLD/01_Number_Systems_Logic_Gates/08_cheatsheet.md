# ⚡ DLD Unit 1 — One-page cheat-sheet (read 10 min before the exam)

**Gates** · AND all-1 (7408) · OR any-1 (7432) · NOT (7404) · NAND 0 only at 11 (7400) · NOR 1 only at 00 (7402) · XOR differ (7486) · XNOR same (74266)
**Universal:** NAND → NOT 1, AND 2, OR 3 · NOR → NOT 1, OR 2, AND 3 · XOR = 4 NAND

**Laws** · A+0=A, A·1=A, A+1=1, A·0=0 · A+A=A · A+A'=1, AA'=0 · A+AB=A, A(A+B)=A · A+BC=(A+B)(A+C) · A+A'B=A+B · (A')'=A
**De Morgan** · (AB)'=A'+B' · (A+B)'=A'B' — “break the bar, change the sign” · **Duality:** + ↔ ·, 0 ↔ 1

**Conversions**
| From → To | Method |
|---|---|
| Dec → r | integer ÷r (remainders ↑), fraction ×r (carries ↓) |
| r → Dec | Σ digit × rᵏ |
| Bin ↔ Oct / Hex | 3-bit / 4-bit groups from the point |
Powers: 2⁰…2¹⁰ = 1 2 4 8 16 32 64 128 256 512 1024 · 8² = 64, 8³ = 512 · 16² = 256, 16³ = 4096

**Arithmetic** · 1+1 = 10 · 1+1+1 = 11 · 0−1 = 1 borrow 1 · check in decimal!

**Complements** · 1's = flip · 2's = flip + 1 · r's = rⁿ − N · (r−1)'s = rⁿ − 1 − N (9's of 2468 = 7531, 10's = 7532)
| A − B with | carry → | no carry → |
|---|---|---|
| 1's comp | add carry to LSB (+) | −(1's of sum) |
| 2's comp | discard carry (+) | −(2's of sum) |

**Signed (n bits)** · S-M & 1's: ±(2ⁿ⁻¹−1), two zeros · 2's: −2ⁿ⁻¹ … 2ⁿ⁻¹−1 (8-bit −128…127) · −25 = 10011001 / 11100110 / 11100111
Overflow: same-sign inputs → opposite-sign result

**Codes** · BCD valid 0000–1001; sum > 9 or carry → +0110 · XS-3 = BCD + 0011 · Gray: Gᵢ = Bᵢ₊₁ ⊕ Bᵢ (1011 → 1110) · ASCII 7-bit (A = 65), EBCDIC 8-bit

**Error codes** · Parity: even/odd, detect 1-bit only · Checksum: 1's comp of sum; receiver result 0 → OK · Hamming: 2ᵖ ≥ m+p+1; P1(1,3,5,7) P2(2,3,6,7) P4(4,5,6,7); 1011 → 0110011; syndrome = error position

**Answer frame (7 m):** Define → Diagram → Truth table/Explanation → Example → Conclusion
