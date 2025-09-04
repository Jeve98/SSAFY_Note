num = int(input())
for i in range(1, num):
    participate = i
    tmp = i
    while i > 0:
        tmp += i % 10
        i //= 10

    if tmp == num:
        print(participate)
        break
else:
    print(0)
