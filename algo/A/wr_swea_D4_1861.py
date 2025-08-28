# BFS, DFS 타임 아웃
# T = int(input())
# for case in range(T):
#     size = int(input())
#
#     table = []
#     for i in range(size):
#         oneLine = list(map(int, input().split()))
#         table.append(oneLine)
#
#     maxNum = 0
#     maxCount = 0
#     # DFS
#     for i in range(size):
#         for j in range(size):
#             stack = [[] for _ in range(size ** 2)]
#             top = -1
#             stack[0] = [i, j]
#             top += 1
#
#             visited = [[False] * size for _ in range(size)]
#             visited[stack[top][0]][stack[top][1]] = True
#             visitCount = 1
#
#             # 상하좌우
#             di = [-1, 1, 0, 0]
#             dj = [0, 0, -1, 1]
#
#             while top != -1:
#                 for addI, addJ in zip(di, dj):
#                     ni = stack[top][0] + addI
#                     nj = stack[top][1] + addJ
#
#                     if 0 <= ni < size and 0 <= nj < size and visited[ni][nj] is False and table[ni][nj] - 1 == table[stack[top][0]][stack[top][1]]:
#                         top += 1
#                         stack[top] = [ni, nj]
#                         visited[ni][nj] = True
#                         visitCount += 1
#                         break
#                 else:
#                     top -= 1
#
#             if maxCount < visitCount:
#                 maxCount = visitCount
#                 maxNum = table[i][j]
#
#             # BFS
#             queue = [[] for _ in range(size ** 2)]
#             front = 0
#             rear = 0
#             queue[0] = [i, j]
#             rear = (rear + 1) % len(queue)
#
#             visited = [[False] * size for _ in range(size)]
#             visited[queue[front][0]][queue[front][1]] = True
#             visitCount = 1
#
#             # 상하좌우
#             di = [-1, 1, 0, 0]
#             dj = [0, 0, -1, 1]
#
#             while front != rear:
#                 for addI, addJ in zip(di, dj):
#                     ni = addI + queue[front][0]
#                     nj = addJ + queue[front][1]
#
#                     if 0 <= ni < size and 0 <= nj < size and table[ni][nj] - 1 == table[queue[front][0]][queue[front][1]] and visited[ni][nj] is False:
#                         queue[rear] = [ni, nj]
#                         rear = (rear + 1) % len(queue)
#                         visited[ni][nj] = True
#                         visitCount += 1
#
#                 front = (front + 1) % len(queue)
#
#             if maxCount < visitCount:
#                 maxCount = visitCount
#                 maxNum = table[i][j]
#
#     print(f'#{case + 1} {maxNum} {maxCount}')

# DP
T = int(input())
for case in range(T):
    size = int(input())

    table = []
    pos = [[] for _ in range(size ** 2 + 1)]
    for i in range(size):
        oneLine = list(map(int, input().split()))
        table.append(oneLine)

        # table[i][j]의 값을 인덱스로 하는 pos 배열에 i, j 좌표 저장
        for j in range(size):
            pos[oneLine[j]] = [i, j]

    dp = [[1] * size for _ in range(size)]

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for num in range(size ** 2, 0, -1):
        i = pos[num][0]
        j = pos[num][1]

        for addI, addJ in zip(di, dj):
            ni = addI + i
            nj = addJ + j

            if 0 <= ni < size and 0 <= nj < size and table[ni][nj] + 1 == table[i][j]:
                dp[ni][nj] = dp[i][j] + 1

    maxCount = -100000
    minNum = 100000
    for i in range(size):
        for j in range(size):
            if maxCount < dp[i][j]:
                maxCount = dp[i][j]
                minNum = table[i][j]
            elif maxCount == dp[i][j] and minNum > table[i][j]:
                minNum = table[i][j]

    print(f'#{case + 1} {minNum} {maxCount}')
