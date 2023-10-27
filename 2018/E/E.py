P = int(input())
for i in range(0, P):
  clock = []
  offset = []
  K, N = map(int, input().split())
  for j in range(0, N):
    clock.append(input())
  for j in range(0, N):
    offset.append(input())
  clock = [(int(c.split(':')[0]) * 60 + int(c.split(':')[1])) % 720 + 1440 for c in clock]
  offset = [int(o.split(':')[0]) * 60 + int(o.split(':')[1]) if o[0] == '+' else int(o.split(':')[0]) * 60 - int(o.split(':')[1]) for o in offset]
  tmpOff = offset
  clock.sort()
  offset.sort()

  cnt = 0
  clk = 0
  for k in range(0, len(clock)):
    clock.append(clock.pop(0)+720)
    offset = [o + clock[0] - offset[0] for o in offset]
    bctn = 0
    for x, y in zip(clock, offset):
      if x%720 != y%720:
        bctn = 1
        break
    if bctn == 1:
      continue
    cnt += 1
    clk = clock[0]
  if cnt == 0:
    print(K, "none")
  elif cnt == 1:
    print(K, f"{(clk+720-tmpOff[0])%720//60}:{str((clk+720-tmpOff[0])%720%60).rjust(2, '0')}")

  else:
    print(K, cnt)