n = int(input())
A = 0

def compute(n, A):
  if n == 1:
    print(A)
    exit(0)
  elif n % 2 == 1:
    A+=1
    compute(n+1, A)
  elif n % 2 == 0:
    A+=1
    compute(n//2, A)

compute(n, A)
