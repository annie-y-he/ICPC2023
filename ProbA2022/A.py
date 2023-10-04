#!/c/Program Files/Python312/python

# in
# H1 B1 (H1 + B1 <= 4)
# H2 B2
#
# out
# P N / "NO SCORE" (1 <= N <= 12)

s = input()
h1 = s.split()[0]
b1 = s.split()[1]

s = input()
h2 = s.split()[0]
b2 = s.split()[1]

pt1 = h1 * 3 + b1
pt2 = h2 * 3 + b2

p = 1 if pt1 > pt2 else 2
n = abs(pt1 - pt2)

print(p, " ", n)