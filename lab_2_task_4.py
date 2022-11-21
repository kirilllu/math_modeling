f = int(input())
f0 = 1
f1 = 1
f2 = f0 + f1
f3 = f2 + f1
print(1)
for i in range(0, 6, 1):
  f2 = f0 + f1
  f0 = f1
  f1 = f2
  f2 = f0
  print(f2)