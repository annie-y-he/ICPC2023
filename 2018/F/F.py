def compute(inp, tb, i, pl, pr, n, cnt):
  cnt[0] += 1
  print(tb)
  tb[i] += inp * (1-pl-pr)
  compute(inp*pl, tb, (i+1)%n, pl, pr, n, cnt)
  compute(inp*pr, tb, (i-1+n)%n, pl, pr, n, cnt)
  if cnt > 2**n:
    print(tb)
    return

for i in range(0, int(input())):
  K, n, k, pl, pr= map(float, input().split())
  K = int(K)
  n = int(n)
  k = int(k)
  tb = [0 for j in range(0, n)]
  cnt = [0]
  compute(1, tb, 0, pl, pr, n, cnt)
  # compute(1, tb, 0, 0.5, 0.4, 6, cnt)

  print(tb)