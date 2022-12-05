from random import random
N = 10
arr = [0] * N
mx = 0
for i in range(N):
    arr[i] = random() * 100
    print("%.2f" % arr[i], end='; ')
    if arr[i] > arr[mx]:
        mx = i
print("\narr[%d] = %.2f" % (mx, arr[mx]))