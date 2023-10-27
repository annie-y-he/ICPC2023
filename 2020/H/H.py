import sys

class Team:
  def __init__(self, T):
    self.T = T
    self.solved = []
    self.probs = {}

  def ptTeam(self):
    print(self.T, self.solved, self.probs)

NT, NP, NS, NR = map(int, input().split())
teams = {}

rank = []
ties = {}

for i in range(1, NS + 1):
  T, P, t, D = map(int, input().split())
  if T not in teams:
    teams[T] = Team(T)
    rank.append(T)
    # print(rank, file=sys.stderr)
  if P in teams[T].solved:
    continue
  if P not in teams[T].probs:
    teams[T].probs[P] = 0
  if D == 0:
    teams[T].probs[P] += 20
  elif D == 1 and P not in teams[T].solved:
    teams[T].probs[P] += t
    teams[T].solved.append(P)
    dbrk = 0
    for i, r in enumerate(rank):
      if T == r:
        break
      elif len(teams[T].solved) > len(teams[r].solved):
        rank.remove(T)
        rank.insert(i, T)
        # print(T, rank, file=sys.stderr)
        break
      elif len(teams[T].solved) == len(teams[r].solved):
        for j in range(len(teams[r].solved) - 1, -1, -1):
          if teams[T].probs[teams[T].solved[j]] < teams[r].probs[teams[r].solved[j]]:
            rank.remove(T)
            rank.insert(i, T)
            # print(rank, file=sys.stderr)
            dbrk = 1
            break
          elif j == 0 and teams[T].probs[teams[T].solved[j]] == teams[r].probs[teams[r].solved[j]]:
            print(T, len(teams[T].solved), r, len(teams[r].solved))
            rank.remove(T)
            rank.insert(i, T)
            if i not in ties:
              ties[i] = 2
            else:
              ties[i] += 1
            dbrk = 1
            break
        if dbrk == 1:
          dbrk = 0
          break

tiedTeams = []
curTie = 0
tieLeft = 0

print(rank)
print(ties)
for i in range(0, NR):
  print(i, i in ties)
  if i in ties:
    curTie = i+1
    tieLeft = ties[i]-1
    tiedTeams.append(rank[i])
  elif curTie != 0 and tieLeft != 0:
    tieLeft -= 1
    tiedTeams.append(rank[i])
    if tieLeft == 0:
      tiedTeams.sort()
      for tt in tiedTeams:
        print(str(curTie).ljust(4), str(tt).ljust(4), str(len(teams[tt].solved)).rjust(3))
      curTie = 0
  else:
    print(str(i+1).ljust(4), str(rank[i]).ljust(4), str(len(teams[rank[i]].solved)).rjust(3))
