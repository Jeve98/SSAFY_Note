# import sys
# sys.stdin = open('../../input.txt', 'r')

row, col = map(int, input().split())

board = [0] * row
startNode = 0
for i in range(row):
    board[i] = list(map(int, input().split()))

    for j in range(col):
        if board[i][j] == 2:
            startNode = (i, j)

# # Dijkstra
# from heapq import heappush as hpush, heappop as hpop
#
#
# def dijkstra(startNode):
#     primaryQ = [(0, startNode)]
#
#     distance = [[-1] * col for _ in range(row)]
#     distance[startNode[0]][startNode[1]] = 0
#     for i in range(row):
#         for j in range(col):
#             if board[i][j] == 0:
#                 distance[i][j] = 0
#
#     # delta
#     di = [-1, 1, 0, 0]
#     dj = [0, 0, -1, 1]
#
#     while primaryQ:
#         dist, nowNode = hpop(primaryQ)
#
#         for addI, addJ in zip(di, dj):
#             ni = nowNode[0] + addI
#             nj = nowNode[1] + addJ
#
#             if 0 <= ni < row and 0 <= nj < col and board[ni][nj] == 1 and distance[ni][nj] == -1:
#                 distance[ni][nj] = dist + 1
#                 hpush(primaryQ, (dist + 1, (ni, nj)))
#
#     return distance
#
#
# result = dijkstra(startNode)
# print('dijkstra')
# for i in range(row):
#     for j in range(col):
#         print(result[i][j], end=' ')
#     print()


# # Bellman-Ford
# def bellman(start):
#     distance = [[2100000000] * col for _ in range(row)]
#     distance[start[0]][start[1]] = 0
#
#     for i in range(row):
#         for j in range(col):
#             if board[i][j] == 0:
#                 distance[i][j] = 0
#
#     for i in range(row * col - 1):
#         for one in edge:
#             start = one[1]
#             end = one[2]
#             if distance[start[0]][start[1]] != 2100000000:
#                 distance[end[0]][end[1]] = min(distance[end[0]][end[1]], distance[start[0]][start[1]] + one[0])
#
#     for i in range(row):
#         for j in range(col):
#             if distance[i][j] == 2100000000:
#                 distance[i][j] = -1
#
#     return distance
#
#
# # delta
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
#
# edge = []
# for i in range(row):
#     for j in range(col):
#         for addI, addJ in zip(di, dj):
#             ni = i + addI
#             nj = j + addJ
#
#             if 0 <= ni < row and 0 <= nj < col and board[ni][nj] != 0 and board[i][j] != 0:
#                 edge.append((1, (i, j), (ni, nj)))      # [0]: weight, [1]: start, [2]: end
#
# result = bellman(startNode)
# print('bellman-ford')
# for i in range(row):
#     for j in range(col):
#         print(result[i][j], end=' ')
#     print()

# BFS
from collections import deque

queue = deque()
visited = [[-1] * col for _ in range(row)]
queue.append(startNode)
visited[startNode[0]][startNode[1]] = 0

# delta
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

while queue:
    nowNode = queue.popleft()

    for addI, addJ in zip(di, dj):
        ni = nowNode[0] + addI
        nj = nowNode[1] + addJ

        if 0 <= ni < row and 0 <= nj < col and board[ni][nj] == 1 and visited[ni][nj] == -1:
            visited[ni][nj] = visited[nowNode[0]][nowNode[1]] + 1
            queue.append((ni, nj))

print('BFS')
for i in range(row):
    for j in range(col):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
