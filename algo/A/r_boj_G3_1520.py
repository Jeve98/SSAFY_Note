import sys
sys.setrecursionlimit(10**6)

row, col = map(int, input().split())

table = []
for i in range(row):
    oneLine = list(map(int, input().split()))
    table.append(oneLine)

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# tabulation
dp = [[0] * col for _ in range(row)]
dp[row - 1][col - 1] = 1

index = []
for i in range(row):
    for j in range(col):
        index.append([table[i][j], i, j])

index.sort()

for i in range(row * col):
    if index[i][0] >= table[row - 1][col - 1] and index[i][0] <= table[0][0]:
        for addI, addJ in zip(di, dj):
            ni = index[i][1] + addI
            nj = index[i][2] + addJ

            if 0 <= ni < row and 0 <= nj < col and table[index[i][1]][index[i][2]] > table[ni][nj]:
                dp[index[i][1]][index[i][2]] += dp[ni][nj]

print(dp[0][0])

# memoization
# dp = [[-1] * col for _ in range(row)]
#
#
# def dfs(start):
#     if start[0] == row - 1 and start[1] == col - 1:
#         return 1
#
#     if dp[start[0]][start[1]] == -1:
#         dp[start[0]][start[1]] = 0
#         for addI, addJ in zip(di, dj):
#             ni = start[0] + addI
#             nj = start[1] + addJ
#
#             if 0 <= ni < row and 0 <= nj < col and table[start[0]][start[1]] > table[ni][nj]:
#                 dp[start[0]][start[1]] += dfs([ni, nj])
#
#     return dp[start[0]][start[1]]
#
#
# dfs([0, 0])
# print(dp[0][0])

# BFS - 시간초과
# queue = [0] * (row * col)
# front = 0
# rear = 0
# queue[rear] = [0, 0]
# rear = (rear + 1) % (row * col)
#
# count = 0
# while front != rear:
#     for addI, addJ in zip(di, dj):
#         ni = addI + queue[front][0]
#         nj = addJ + queue[front][1]
#
#         if 0 <= ni < row and 0 <= nj < col and table[queue[front][0]][queue[front][1]] > table[ni][nj]:
#             if ni == row - 1 and nj == col - 1:
#                 count += 1
#             else:
#                 queue[rear] = [ni, nj]
#                 rear = (rear + 1) % (row * col)
#
#     front = (front + 1) % (row * col)
#
# print(count)
