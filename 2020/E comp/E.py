# r/(r+g) * g/(r+g-1)
# g/(r+g) * r/(r+g-1)
# = p/q

import fractions as fr

p, q, N, M = map(int, input().split())

for marb in range(N, M + 1):
  for r in range(1, marb//2+1):
    g = marb - r
    prob = fr.Fraction(r, r+g) * fr.Fraction(g, r+g-1) + fr.Fraction(g, r+g) * fr.Fraction(r, r+g-1)
    if prob == fr.Fraction(p, q):
      print(r, g)
      exit(0)
print("NO SOLUTION")