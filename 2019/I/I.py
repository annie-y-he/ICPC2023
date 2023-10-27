import fractions as fr
import math
p, q, n = map(int, input().split())
base = fr.Fraction(p, q)


# poly = [0 for i in range(int(math.log(n, base)), -1, -1)]
# for ex in range(int(math.log(n, base)), -1, -1):
#   tmp = poly
#   tmpn = n
#   for i in range(0, len(tmp)):
#     j = len(tmp) - i - 1
#     for k in range(0, p):
#       if k*base**j <= n:
#         tmp[]

print(float(2*base**5))