inStr = input()
S = [int(c) for c in inStr]
S.reverse()

N = 0
K = 0
M = 2

T = 0

for i in range(0, len(S)):
  T = int(T * 2 + S[i] * pow(3, i))
  M = pow(2, i)

  N = int(T/M)
  K = T % M

while K % 2 != 1 and K != 0:
  K = int(K / 2)
  M = int(M / 2)

print(N, str(K)+"/"+str(M) if K != 0 else "")