import math
def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False

  sqrt_n = int(math.floor(math.sqrt(n)))
  for i in range(3, sqrt_n + 1, 2):
    if n % i == 0:
      return False
  return True

M = int(input())

prm = []

for i in range(0, M):
  pub = int(input())
  for j in range(2, pub):
    if is_prime(j) and pub/j == pub//j and is_prime(pub//j):
      prm.append(j)
      prm.append(pub//j)
      break

prm = list(set(prm))
prm.sort()

for i, item in enumerate(prm):
  if (i+1) % 5 == 0 or i == len(prm) - 1:
    print(item)
  else:
    print(item, end=" ")