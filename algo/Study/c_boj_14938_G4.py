# import sys
# sys.stdin = open("algo/input.txt", "r")

from heapq import heappush as hpush, heappop as hpop


# DFS의 경우, 더 짧은 경로를 사전 차단할 수 있는 경우가 발생
# def DFS(nodes, searchDis):
#     global tmp

#     if searchDis > 0:
#         for node in nodes:
#             if not visited[node[0]] and searchDis - node[1] >= 0:
#                 tmp += items[node[0] - 1]
#                 visited[node[0]] = True
#                 DFS(edgeList[node[0]], searchDis - node[1])


# areaC, searchDis, edgeC = map(int, input().split())
# items = list(map(int, input().split()))

# edgeList = [[] for _ in range(areaC + 1)]
# for i in range(edgeC):
#     data = list(map(int, input().split()))  # 0: start, 1: end, 2: distance
#     edgeList[data[0]].append((data[1], data[2]))
#     edgeList[data[1]].append((data[0], data[2]))

# maxItem = 0
# for i in range(1, areaC + 1):
#     visited = [False] * (areaC + 1)
#     visited[i] = True
#     tmp = items[i - 1]
#     DFS(edgeList[i], searchDis)

#     if tmp > maxItem:
#         maxItem = tmp

# print(maxItem)


def dijkstra(now):
    global maxItem

    hq = []
    hpush(hq, (0, now))

    distance = [10000] * (areaC + 1)

    while hq:
        cost, node = hpop(hq)

        if distance[node] > cost:
            distance[node] = cost

            for newNode in edgeList[node]:
                nN, dis = newNode
                hpush(hq, (dis + cost, nN))

    tmp = 0
    for i in range(1, areaC + 1):
        if distance[i] <= searchDis:
            tmp += items[i - 1]

    if tmp > maxItem:
        maxItem = tmp


areaC, searchDis, edgeC = map(int, input().split())
items = list(map(int, input().split()))

edgeList = [[] for _ in range(areaC + 1)]
for i in range(edgeC):
    data = list(map(int, input().split()))  # 0: start, 1: end, 2: distance
    edgeList[data[0]].append((data[1], data[2]))
    edgeList[data[1]].append((data[0], data[2]))

maxItem = 0
for i in range(1, areaC + 1):
    dijkstra(i)
print(maxItem)
