T = int(input())
for i in range(T):
    area = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]
    count = 0
    for j in range(area):
        oneLine = list(map(int, input().split()))   # [0], [1]: start pos, [2], [3]: end pos, [4]: color
        for row in range(oneLine[0], oneLine[2] + 1):
            for col in range(oneLine[1], oneLine[3] + 1):
                if arr[row][col] == 0:
                    arr[row][col] = oneLine[4]
                else:
                    arr[row][col] = 3
                    count += 1

    print(f'#{i+1} {count}')