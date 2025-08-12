T = int(input())
for case in range(T):
    size = int(input())

    arr = []
    for i in range(size):
        oneLine = list(map(int, input().split()))
        arr.append(oneLine)

    arr90 = list(map(list, zip(*arr[::-1])))
    arr180 = list(map(list, zip(*arr90[::-1])))
    arr270 = list(map(list, zip(*arr180[::-1])))

    print(f'#{case + 1}')
    for i in range(size):
        for j in range(size):
            print(arr90[i][j], end='')
        print(end=' ')
        for j in range(size):
            print(arr180[i][j], end='')
        print(end=' ')
        for j in range(size):
            print(arr270[i][j], end='')
        print(end=' ')
        print()
