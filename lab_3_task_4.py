from math import sin
n = 3
m = 4
mtx = []
for i in range(n):
    a = []
    for j in range(m):
        a.append(sin(n*(i+1) + m *(j+1)))
    mtx.append(a)
for i in range(n):
    for j in range(m):
        if mtx[i][j] < 0:
            mtx[i][j] = 0
            print("%7.0f" % mtx[i][j], end='')
        else:
            print("%7.2f" % mtx[i][j], end='')
    print()