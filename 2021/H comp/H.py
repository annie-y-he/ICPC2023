N = int(input())
ip = []
mask = 0
for i in range(0, N):
  tmp = list("".join([bin(int(n))[2::1].rjust(8, "0") for n in input().split(".")]))
  ip.append(tmp)

for j in zip(*ip):
  if len(set(j)) == 1:
    mask += 1
  else:
    if mask == 0:
      print(32)
    else:
      print(mask)
    exit(0)
print(mask)