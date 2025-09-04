while True:
    oneLine = list(map(int, input().split()))

    if oneLine[0] == 0:
        break

    oneLine.sort()
    tmpSum = 0
    for i in range(2):
        tmpSum += oneLine[i] ** 2

    if tmpSum == oneLine[2] ** 2:
        print('right')
    else:
        print('wrong')
