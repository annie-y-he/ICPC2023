myDict = {
  '1110111': [
    'XXX',
    'X X',
    'X X',
    '   ',
    'X X',
    'X X',
    'XXX'
  ],
  '0100100': [
    '   ',
    '  X',
    '  X',
    '   ',
    '  X',
    '  X',
    '   '
  ],
  '1011101': [
    'XXX',
    '  X',
    '  X',
    'XXX',
    'X  ',
    'X  ',
    'XXX'
  ],
  '1101101': [
    'XXX',
    '  X',
    '  X',
    'XXX',
    '  X',
    '  X',
    'XXX'
  ],
  '0101110': [
    '   ',
    'X X',
    'X X',
    'XXX',
    '  X',
    '  X',
    '   '
  ],
  '1101011': [
    'XXX',
    'X  ',
    'X  ',
    'XXX',
    '  X',
    '  X',
    'XXX'
  ],
  '1111011': [
    'XXX',
    'X  ',
    'X  ',
    'XXX',
    'X X',
    'X X',
    'XXX'
  ],
  '0100101': [
    'XXX',
    '  X',
    '  X',
    '   ',
    '  X',
    '  X',
    '   '
  ],
  '1111111': [
    'XXX',
    'X X',
    'X X',
    'XXX',
    'X X',
    'X X',
    'XXX'
  ],
  '1101111': [
    'XXX',
    'X X',
    'X X',
    'XXX',
    '  X',
    '  X',
    'XXX'
  ],
  '0111111': [
    'XXX',
    'X X',
    'X X',
    'XXX',
    'X X',
    'X X',
    '   '
  ],
  '1111010': [
    '   ',
    'X  ',
    'X  ',
    'XXX',
    'X X',
    'X X',
    'XXX'
  ],
  '1010011': [
    'XXX',
    'X  ',
    'X  ',
    '   ',
    'X  ',
    'X  ',
    'XXX'
  ],
  '1111100': [
    '   ',
    '  X',
    '  X',
    'XXX',
    'X X',
    'X X',
    'XXX'
  ],
  '1011011': [
    'XXX',
    'X  ',
    'X  ',
    'XXX',
    'X  ',
    'X  ',
    'XXX'
  ],
  '0011011': [
    'XXX',
    'X  ',
    'X  ',
    'XXX',
    'X  ',
    'X  ',
    '   '
  ],
}

myStr = input()
S = int(myStr.split()[0])
char = myStr.split()[1]
char = char.rjust((len(char)//7 + 1) * 7 if len(char)%7 != 0 else len(char), '0')
char = [char[i*7:i*7+7] for i in range(0, len(char)//7)]
char = [c if c in myDict else '0000000' for c in char]
lines = []

myDict['0000000'] = [
    '   ',
    '   ',
    '   ',
    '   ',
    '   ',
    '   ',
    '   '
  ]

pos = 0
tmp = []
for i, c in enumerate(char):
  if pos != 0:
    pos += 2 * S
  if pos + S * 3 <= 80:
    tmp.append(c)
    pos += S * 3
  else:
    lines.append(tmp)
    tmp = []
    tmp.append(c)
    pos = S * 3
if len(tmp) != 0:
  lines.append(tmp)

for word in myDict:
  tmp = []
  for line in myDict[word]:
    tmp.append("".join([letter * S for letter in line]))
  myDict[word] = tmp

for l, line in enumerate(lines):
  for j in range(0, 7):
    for k in range(0, S):
      for i, c in enumerate(line):
        if i != 0:
          print("  " * S, end="")
        print(myDict[c][j], end="")
      print()
  if l != len(lines) - 1:
    for i in range(0, S):
      print()