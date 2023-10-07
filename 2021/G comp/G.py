n = int(input())
# n <= 40000

# import copy

# myList = [1]

# for i in range(1, n):
#   tmp = []
#   for m in myList:
#     tmp.append(m * 2)
#     if (m + 1) % 2 == 1:
#       tmp.append(m - 1)
#   print(tmp)
#   myList = copy.deepcopy(tmp)

# print(len(myList))

fib0 = 0
fib1 = 1
for i in range(0, n - 1):
  fib = fib1
  fib1 = fib0 + fib1
  fib0 = fib
  # if fib0 > 1000007:
    # fib0 = fib0 % 1000007
    # fib1 = fib1 % 1000007
print(fib1 % 1000007, end='\n')