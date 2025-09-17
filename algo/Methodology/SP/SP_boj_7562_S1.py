import sys
sys.stdin = open('../../input.txt', 'r')

# Dijkstra
# from heapq import heappush as hpush, heappop as hpop
#
#
# def dijkstra(start):
#     primaryQ = [(0, start)]
#
#     distance = [[2100000000] * size for _ in range(size)]
#     distance[start[0]][start[1]] = 0
#
#     while primaryQ:
#         nowDis, nowNode = hpop(primaryQ)
#
#         # 성능 향상
#         if distance[nowNode[0]][nowNode[1]] < nowDis:
#             continue
#
#         for addI, addJ in zip(di, dj):
#             ni = nowNode[0] + addI
#             nj = nowNode[1] + addJ
#
#             if 0 <= ni < size and 0 <= nj < size:
#                 newDis = nowDis + 1
#                 if distance[ni][nj] > newDis:
#                     distance[ni][nj] = newDis
#                     hpush(primaryQ, (distance[ni][nj], [ni, nj]))
#
#     return distance


T = int(input())
for case in range(T):
    size = int(input())
    start = list(map(int, input().split()))
    destination = list(map(int, input().split()))

    # delta - knight
    di = [-1, -2, -2, -1, 1, 2, 2, 1]
    dj = [-2, -1, 1, 2, 2, 1, -1, -2]

    # Dijkstra
    # result = dijkstra(start)
    # print(result[destination[0]][destination[1]])

    # Bellman-Ford

    # BFS
