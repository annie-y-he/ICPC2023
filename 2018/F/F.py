for i in range(0, int(input())):
  K, n, k, pl, pr= map(float, input().split())
  K = int(K)
  n = int(n)
  k = int(k)
  tb = [0 for j in range(0, n)]
  tmp = tb
  tb[0] = 1 - pl - pr + pr * tb[n-1] + pl * tb[1]
  for p in range(1, n):
    tb[p] = pr * tb[p-1] + pl * tb[p+1]
  print(tmp, tb)