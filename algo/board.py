sq = []
for i in range(4):
    oneLine = list(map(int, input().split()))
    sq.append([(oneLine[0], oneLine[1]), (oneLine[2], oneLine[3])])

board = [[0] * 100 for _ in range(100)]
for one in sq:
    for i in range(one[0][0], one[1][0]):
        for j in range(one[0][1], one[1][1]):
            board[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            count += 1

print(count)
