# P = (1 - p) ^ N
# E = P + N * (1 - P)

p = float(input())

bestN = 1
bestE = 1
minimized = 16

for N in range(1, 17):
  P = (1 - p)**N
  E = P + N * (1 - P)
  if E / N < minimized:
    bestE = E
    bestN = N
    minimized = E / N

print(bestN)