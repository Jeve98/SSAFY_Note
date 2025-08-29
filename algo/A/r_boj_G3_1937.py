import sys
sys.setrecursionlimit(10**6)

size = int(input())

forest = []
for i in range(size):
    oneLine = list(map(int, input().split()))
    forest.append(oneLine)

#상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# tabulation
dp = [[1] * size for _ in range(size)]

index = []
for i in range(size):
    for j in range(size):
        index.append([forest[i][j], i, j])
index.sort()

maxCount = 0
for i in range(len(index)):
    for addI, addJ in zip(di, dj):
        ni = index[i][1] + addI
        nj = index[i][2] + addJ

        if 0 <= ni < size and 0 <= nj < size and index[i][0] < forest[ni][nj]:
            dp[ni][nj] = max(dp[ni][nj], dp[index[i][1]][index[i][2]] + 1)

    maxCount = max(maxCount, dp[index[i][1]][index[i][2]])

print(maxCount)

# memoization
# def DFS(start):
#     dpVal = dp[start[0]][start[1]]
#     if dpVal == 0:
#         for addI, addJ in zip(di, dj):
#             ni = start[0] + addI
#             nj = start[1] + addJ
#
#             if 0 <= ni < size and 0 <= nj < size and forest[start[0]][start[1]] < forest[ni][nj]:
#                 dp[start[0]][start[1]] = max(dp[start[0]][start[1]], dpVal + DFS([ni, nj])) # dpVal은 어차피 0
#
#     return dp[start[0]][start[1]] + 1
#
#
# dp = [[0] * size for _ in range(size)]
# maxCount = 0
# for i in range(size):
#     for j in range(size):
#         maxCount = max(maxCount, DFS([i, j]))
#
# print(maxCount)

# DFS - 시간초과
# stack = [0] * (size ** 2)
# top = -1
#
# maxCount = 0
# for i in range(size):
#     for j in range(size):
#         visited = [[False] * size for _ in range(size)]
#         visited[i][j] = True
#         top = 0
#         stack[top] = [i, j]
#
#         while top != -1:
#             for addI, addJ in zip(di, dj):
#                 ni = stack[top][0] + addI
#                 nj = stack[top][1] + addJ
#
#                 if 0 <= ni < size and 0 <= nj < size and forest[stack[top][0]][stack[top][1]] < forest[ni][nj] and not visited[ni][nj]:
#                     top += 1
#                     stack[top] = [ni, nj]
#                     visited[ni][nj] = True
#                     break
#             else:
#                 if maxCount < top:
#                     maxCount = top
#                 top -= 1
#
# print(maxCount + 1)
