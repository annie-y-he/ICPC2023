# in
# S I
# (3 <= S <=19) (0 <= I <= N = (S * (S + 1)) / 2)
# r c cc
# (1 <= r <= s) (1 <= c <= r) (0 <= cc <= 2; rgb)
#
# out
# num of solution
#

# pass
#   for each in group
#     if 2
#       fill
#       filled += 1
#     if 3 and wrong
#        return
#   if full
#     s += 1
#   else
#     from r to b
#       push
#       guess
#       pass
#       pop
import copy

s = input()
S = int(s.split()[0])
I = int(s.split()[1])
N = int((S * (S + 1)) / 2)
stack = []
T = [[-1 for j in range(1, i + 1)] for i in range(1, S + 1)]
F = I
sol = 0

for i in range(0, I):
  s = input()
  r = int(s.split()[0])
  c = int(s.split()[1])
  cc = int(s.split()[2])
  T[r-1][c-1] = cc

def go(S, I, N, T, sol, stack, F):
  for i in range(0, len(T) - 1):
    for j in range(0, len(T[i])):
      group = [T[i][j], T[i+1][j], T[i+1][j+1]]
      if group.count(-1) == 0:
        if len(set(group)) == 2:
          return sol
      elif group.count(-1) == 1:
        rest = set(group) - {-1}
        if len(rest) == 1:
          if group[0] == -1:
            T[i][j] = rest.pop()
          elif group[1] == -1:
            T[i+1][j] = rest.pop()
          elif group[2] == -1:
            T[i+1][j+1] = rest.pop()
        elif len(rest) == 2:
          other = {0, 1, 2} - rest
          if group[0] == -1:
            T[i][j] = other.pop()
          elif group[1] == -1:
            T[i+1][j] = other.pop()
          elif group[2] == -1:
            T[i+1][j+1] = other.pop()
        F += 1
        for t in T:
          print(t)
        print()
  print(F, N)
  if F == N:
    sol += 1
    print("solution", sol)
    F = I
  else:
    tmpF = F
    tmp = copy.deepcopy(T)
    for k in range(0, 3):
      try:
        for i in range(0, len(T)):
          for j in range(0, i + 1):
            if T[i][j] == -1:
              print("guess", k)
              T[i][j] = k
              for t in T:
                print(t)
              print()
              raise
      except:
        F += 1
        sol = go(S, I, N, T, sol, stack, F)
        print("revert")
        F = tmpF
        T = copy.deepcopy(tmp)
  return sol


for t in T:
  print(t)
print()

sol = go(S, I, N, T, sol, stack, F)
for t in T:
  print(t)
print()

print(sol)