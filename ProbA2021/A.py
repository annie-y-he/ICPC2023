# in
# T F S P C (non-neg int) (<=10)

# T * 6 + F * 3 + S * 2 + P * 1 + C * 2
s = input()
T1 = int(s.split()[0])
F1 = int(s.split()[1])
S1 = int(s.split()[2])
P1 = int(s.split()[3])
C1 = int(s.split()[4])
s = input()
T2 = int(s.split()[0])
F2 = int(s.split()[1])
S2 = int(s.split()[2])
P2 = int(s.split()[3])
C2 = int(s.split()[4])

pt1 = T1 * 6 + F1 * 3 + S1 * 2 + P1 * 1 + C1 * 2
pt2 = T2 * 6 + F2 * 3 + S2 * 2 + P2 * 1 + C2 * 2

print(pt1, pt2)