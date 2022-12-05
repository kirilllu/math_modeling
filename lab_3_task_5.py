from random import random
m = 10
n = 5
a = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(round(random()*2))
    a.append(b)
    print(b)
c1 = int(input("Один столбец: ")) - 1
c2 = int(input("Другой столбец: ")) - 1
for i in range(n):
    a[i][c1], a[i][c2] = a[i][c2], a[i][c1]
    print(a[i])