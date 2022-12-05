a = []
N = 5
for i in range(N):
    num = int(input())
    a.append(num)
print(a)
num = int(input("Число: "))
j = int(input("Позиция: "))
a.append(num)
while N > j-1:
    a[N], a[N-1] = a[N-1], a[N]
    N -= 1
print(a)