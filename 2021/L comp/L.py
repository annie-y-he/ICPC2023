letterel = list(input())

for i in range(0, 7):
  guess = list(input())
  feedback = ""
  for j, k in zip(letterel, guess):
    if j == k:
      feedback += 'G'
    elif k in letterel:
      feedback += 'Y'
    else:
      feedback += 'X'
  if feedback == "GGGGG":
    print("WINNER")
    exit(0)
  elif i == 6:
    print("LOSER")
    exit(0)
  else:
    print(feedback)
print("LOSER")