fac = int(input())

num = 1
for i in range(1, fac + 1):
    num *= i

num = str(num)
find = False
count = 0
for i in range(len(num) - 1, -1, -1):
    if num[i] == '0':
        count += 1
        find = True
    elif find:
        break

print(count)
