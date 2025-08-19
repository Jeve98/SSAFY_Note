T = int(input())
for case in range(T):
    row, time = map(int, input().split())

    display = [[-1] * row for _ in range(4)]
    for t in range(1, time + 1):
        for i in range(4):
            for j in range(row):
                if (i + j + 1) % t == 0:
                    display[i][j] *= -1

    count = 0
    for i in range(4):
        for j in range(row):
            if display[i][j] == 1:
                count += 1

    print(f'#{case + 1} {count}')
