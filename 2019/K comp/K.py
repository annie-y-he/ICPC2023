s = input()

if s.find('-') > 8 or s.find('-') < 2:
  print("NO")
elif len(s) - s.find('-') - 1 < 1 or len(s) - s.find('-') - 1 > 24:
  print("NO")
else:
  print("YES")
