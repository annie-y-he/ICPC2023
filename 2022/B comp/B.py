N = int(input())
S = []
for i in range(0, N//10+1 if N%10!=0 else N//10):
  S += [int(n) for n in input().split()]

m = S[0]
K = []
for i in range(2, N+1):  
  K += [i for j in range(0, ((m - len(K)) * i + sum(i%v for v in K) - S[i-1]) // i)]

print(m, end=" ")
print(" ".join([str(k) for k in K]))