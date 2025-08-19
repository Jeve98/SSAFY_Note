T = int(input())
for k in range(T):
    size = int(input())
    arr = [[0] * size for _ in range(size)]

    num = 1
    top = 0
    bottom = size - 1
    left = 0
    right = size - 1
    while num <= size * size:
        for i in range(left, right + 1):
            arr[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            arr[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            arr[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            arr[i][left] = num
            num += 1
        left += 1

    print(f'#{k+1}')
    for i in range(size):
        for j in range(size):
            print(arr[i][j], end=' ')
        print()