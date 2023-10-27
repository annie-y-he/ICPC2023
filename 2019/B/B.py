N, P = map(int, input().split())

ps = []

for n in range(1, N+1):
  l = input().split()
  l.pop(0)
  ps.append([int(s) for s in l])
print(ps)
for n in range(1, P+1):
  p = [0 for i in ps]
  i, s, w = map(int, input().split())
  p[s-1] = 1/len(ps[s-1])
  for nb in ps[s-1]:
    p[nb-1] = 1/len(ps[s-1]) 
  print(p)

def buck(i):
  p[i] += p[i] * len(ps[i])
