row, col = map(int, input().split())

board = [0] * row
for i in range(row):
    oneLine = input()
    board[i] = oneLine

minCount = 2100000000
for i in range(row - 7):
    for j in range(col - 7):
        for case in range(2):
            if case % 2 == 0:
                now = 'W'
            else:
                now = 'B'
            count = 0
            for r in range(8):
                for c in range(8):
                    if now != board[i + r][j + c]:
                        count += 1

                    if now == 'W' and c != 7:
                        now = 'B'
                    elif now == 'B' and c != 7:
                        now = 'W'

            minCount = min(minCount, count)

print(minCount)
