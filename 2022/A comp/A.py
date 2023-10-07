# in
# H1 B1 (H1 + B1 <= 4)
# H2 B2
#
# out
# P N / "NO SCORE" (1 <= N <= 12)

s = input()
h1 = int(s.split()[0])
b1 = int(s.split()[1])

s = input()
h2 = int(s.split()[0])
b2 = int(s.split()[1])

pt1 = h1 * 3 + b1
pt2 = h2 * 3 + b2

n = abs(pt1 - pt2)

if pt1 > pt2:
  print(1, n)
elif pt1 == pt2:
  print("NO SCORE")
else:
  print(2, n)