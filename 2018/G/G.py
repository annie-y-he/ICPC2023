import fractions as fr

for i in range(0, int(input())):
  K, n = map(int, input().split())
  num = fr.Fraction(4, n)
  for c in range(2, 10000):
    for b in range(2, c):
      for a in range(2, b):
        if num == fr.Fraction(1, a) + fr.Fraction(1, b) + fr.Fraction(1, c):
          print(a, b, c)