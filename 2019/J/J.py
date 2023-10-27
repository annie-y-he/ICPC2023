import math

n = int(input())
# n n n*3 n*3*3 n*2*3 n*2*2*3

def compute(n, i):
  if i == 0 or i == 1:
    return n
  else:
    return n*(3**(i-1))-n*(i-2)*3
result = 0
for i in range(0, n):
  result += compute(n, i)
print(result%100007)