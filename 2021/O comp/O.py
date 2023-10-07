# in
# A B C D (int)
# (0 < A <= 100) (0 < B <= 20) (0 <= C <= 100) (0 <= D <= 100)
# A: Mi -> Me
# B: Me -> Ve
# C: Ve req >= C
# D: Me req = D
#
# out
# "We need t trucks and b boats."
# ...t truck and b boat.
# "No solution."
# t b

# A * t - D = B * b = V
# V >= C
# loop t from 0 to N
#   V = A * t - D
#   b = V / B
#   if b is int and V >= C
#     return t, b

s = input()

A = int(s.split()[0])
B = int(s.split()[1])
C = int(s.split()[2])
D = int(s.split()[3])

for t in range(0, 1000):
  V = A * t - D
  b = int(V / B)
  if not V % B == 0:
    continue
  elif V >= C:
    st = "trucks" if t != 1 else "truck"
    sb = "boats." if b != 1 else "boat."
    print("We need", t, st, "and", b, sb)
    exit(0)
print("No solution.")