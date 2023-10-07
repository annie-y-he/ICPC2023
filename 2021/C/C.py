import random

S = 6

class Board:
  def __init__(self, S, n):
    self.board = [[[0] for i in range(1, S + 1)] for j in range(1, S + 1)]
    self.C = [Checker() for i in range(1, n + 1)]
    for c in self.C:
      c.add(self)
    print("Initial:")
    self.print()
  def print(self):
    for b in self.board:
      print(" ".join([str(i[0]) for i in b]))
    print()
  def move(self, start, finish):
    self.board[start[0]][start[1]][0] = 0
    self.board[finish[0]][finish[1]][0] = 1
  def moveRand(self, rep):
    for i in range(1, rep + 1):
      self.C[random.randint(0, len(self.C) - 1)].moveRand(self)

class Checker:
  def __init__(self):
    self.x = -1
    self.y = -1
  def add(self, B):
    tX = random.randint(0, len(B.board) - 1)
    tY = random.randint(0, len(B.board) - 1)
    while B.board[tX][tY][0] != 0:
      tX = random.randint(0, len(B.board) - 1)
      tY = random.randint(0, len(B.board) - 1)
    self.x = tX
    self.y = tY
    B.board[self.x][self.y][0] = 1
  def moveU(self, B):
    tX = 0
    for c in B.C:
      if c.y == self.y and c.x < self.x and c.x >= tX:
        tX = c.x + 1
    if tX != self.x:
      print("MU:", [self.x, self.y], "to", [tX, self.y])
      B.move([self.x, self.y], [tX, self.y])
      self.x = tX
      B.print()
      return 1
    else:
      print("MU:", [self.x, self.y], "No Change")
      B.print()
      return 0
  def moveD(self, B):
    tX = len(B.board) - 1
    for c in B.C:
      if c.y == self.y and c.x > self.x and c.x <= tX:
        tX = c.x - 1
    if tX != self.x:
      print("MD:", [self.x, self.y], "to", [tX, self.y])
      B.move([self.x, self.y], [tX, self.y])
      self.x = tX
      B.print()
      return 1
    else:
      print("MD:", [self.x, self.y], "No Change")
      B.print()
      return 0

  def moveL(self, B):
    tY = 0
    for c in B.C:
      if c.x == self.x and c.y < self.y and c.y >= tY:
        tY = c.y + 1
    if tY != self.y:
      print("ML:", [self.x, self.y], "to", [self.x, tY])
      B.move([self.x, self.y], [self.x, tY])
      self.y = tY
      B.print()
      return 1
    else:
      print("ML:", [self.x, self.y], "No Change")
      B.print()
      return 0

  def moveR(self, B):
    tY = len(B.board) - 1
    for c in B.C:
      if c.x == self.x and c.y > self.y and c.y <= tY:
        tY = c.y - 1
    if tY != self.y:
      print("MR:", [self.x, self.y], "to", [self.x, tY])
      B.move([self.x, self.y], [self.x, tY])
      self.y = tY
      B.print()
      return 1
    else:
      print("MR:", [self.x, self.y], "No Change")
      B.print()
      return 0
  def moveRand(self, B):
    r = random.randint(0, 3)
    if r == 0:
      self.moveU(B)
    elif r == 1:
      self.moveD(B)
    elif r == 2:
      self.moveL(B)
    else:
      self.moveR(B)

B = Board(S, 4)
# B.moveRand(5000)
B.C[0].moveU(B)
B.C[0].moveL(B)
B.C[0].moveU(B)
B.C[0].moveL(B)

B.C[1].moveU(B)
B.C[1].moveL(B)
B.C[1].moveU(B)
B.C[1].moveL(B)

B.C[2].moveU(B)
B.C[2].moveL(B)
B.C[2].moveU(B)
B.C[2].moveL(B)

B.C[3].moveU(B)
B.C[3].moveL(B)
B.C[3].moveU(B)
B.C[3].moveL(B)




