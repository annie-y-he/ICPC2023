# if k%2 == 0
# b(k) = b(k//2)
# else
# b(k) = b(k+1) + b(k-1)

# p, q = map(int, input().split())
p = int(input())

def compute(n):
  s = [-99]
  for k in range(1, (n + 1) * 2):
    if k == 1:
      s.append(1)
    elif k % 2 == 0 and s[k//2] != -1:
      s.append(s[k//2])
    elif k % 2 == 0 and s[k//2] == -1:
      s[k//2] = s[k//2 - 1] + s[k//2 + 1]
      s.append(s[k//2])
    elif k % 2 == 1:
      s.append(-1)
  print(n, max(s))
  return s[n]

for i in range(1, p+1):
  compute(i)
# print(compute(p))

