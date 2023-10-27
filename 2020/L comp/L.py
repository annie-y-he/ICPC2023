line = {}
for i, c in enumerate(input()):

  if not c in line:
    line[c] = i
  elif line[c] == -1:
    print("NO")
    exit(0)
  elif (i - line[c])%2 == 1:
    line[c] = -1
  else:
    print("NO")
    exit(0)
print("YES")

# print(line)