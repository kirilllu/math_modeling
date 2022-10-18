year = int(input())

if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
    print("високосный")
else:
    print("обычный")