
def isValid(puzzle, row, col, color):
  print(row, col)
  neighbors = [color]
  if col > 0 :
    neighbors.append(puzzle[row-1][col-1])
    neighbors.append(puzzle[row][col-1])
  if len(set(neighbors)) == 2:
    return False
  neighbors = []
  if col < len(puzzle[row]) and row != 0:
    neighbors.append(puzzle[row-1][col])
    neighbors.append(puzzle[row][col+1])
  if len(set(neighbors)) == 2:
    return False
  neighbors = []
  if row+1 < len(puzzle):
    neighbors.append(puzzle[row+1][col])
    neighbors.append(puzzle[row+1][col+1])
  if len(set(neighbors)) == 2:
    return False
  return True
def solve(puzzle, row, col):
  solutions = 0
  for color in range(3):
    if isValid(puzzle, row, col, color):
      puzzle[row][col] = color
      if row == len(puzzle) - 1 and col == len(puzzle[row]) - 1:
        solutions += 1
        return solutions
      solutions += solve(puzzle, row+1 if col+1 > len(puzzle[row]) else row, 0 if col+1 > len(puzzle[row]) else col+1)
      puzzle[row][col] = -1
  return solutions

def main():
  S, I = map(int, input().split())
  N = int((S * (S + 1)) / 2)

  puzzle = [[-1 for j in range(1, i + 1)] for i in range(1, S + 1)]

  for _ in range(I):
    r, c, cc = map(int, input().split())
    puzzle[r - 1][c - 1] = cc



  solutions = solve(puzzle, 0, 0)
  # print([item for sublist in puzzle for item in sublist])

if __name__ == "__main__":
  main()