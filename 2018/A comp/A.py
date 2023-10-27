for i in range(0, int(input())):
  s = input().split()
  K = int(s.pop(0))
  C = int(s.pop(0))
  cur = 0
  p = [int(n) for n in s]
  p.sort()
  p.reverse()
  for ptt in p:
    if cur + ptt > C:
      continue
    else:
      cur += ptt
  if cur != C:
    print(K, "NO")
  else:
    print(K, "YES")
