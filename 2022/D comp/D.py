n = int(input())

pt1 = []
pt2 = []
pt3 = []
pt4 = []

for a in range(1, n + 1):
  for b in range(1, a + 1):
    if a**2 + b**2 == n**2:
      pt1.append([int(a), int(b), int(n)])
c = n + 1
b = (c**2 - n**2)**0.5

while c >= b+1:
  if b % 1 == 0:
    pt3.append([int(n), int(b), int(c)])
  c += 1
  b = (c**2 - n**2)**0.5

for j, pt in enumerate(pt1):
  for i in range(2, min(*pt)):
    if pt[0]%i == 0 and pt[1]%i == 0 and pt[2]%i == 0:
      pt1[j] = None
      pt2.append(pt)
      break

for j, pt in enumerate(pt3):
  for i in range(2, min(*pt) + 1):
    if pt[0]%i == 0 and pt[1]%i == 0 and pt[2]%i == 0:
      pt4.append(pt)
      pt3[j] = None
      break

print(len([pt for pt in pt1 if pt is not None]), len(pt2), len([pt for pt in pt3 if pt is not None]), len(pt4))




