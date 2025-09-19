import sys
sys.stdin = open('../../input.txt', 'r')

# Dijkstra
# from collections import deque
#
#
# def dijkstra(start):
#     primaryQ = deque()
#     primaryQ.append((0, start))
#
#     distance = [210000000] * (vertexC + 1)
#     distance[start] = 0
#
#     while primaryQ:
#         nowDis, nowNode = primaryQ.popleft()
#
#         if distance[nowNode] < nowDis:
#             continue
#
#         for participate in vertexList[nowNode]:
#             newDis, nextNode = participate[0], participate[1]
#
#             if distance[nextNode] > nowDis + newDis:
#                 distance[nextNode] = nowDis + newDis
#                 primaryQ.append((distance[nextNode], nextNode))
#                 ans[nextNode] = nowNode


# Bellman-Ford
def bellman(start):
    distance = [210000000] * (vertexC + 1)
    distance[start] = 0

    for i in range(vertexC - 1):
        for edge in edgeList:
            if type(edge) == list:
                if distance[edge[1]] > distance[edge[0]] + edge[2]:
                    distance[edge[1]] = distance[edge[0]] + edge[2]
                    result[edge[1]] = edge[0]


vertexC, edgeC = map(int, input().split())
# vertexList = [[] for _ in range(vertexC + 1)]
edgeList = [0] * (edgeC * 2)
for i in range(edgeC):
    oneLine = list(map(int, input().split()))   # [0]: start, [1]: end, [2]: weight
    # vertexList[oneLine[0]].append((oneLine[2], oneLine[1]))
    # vertexList[oneLine[1]].append((oneLine[2], oneLine[0]))

    edgeList[i] = oneLine
    edgeList.append([oneLine[1], oneLine[0], oneLine[2]])

# Dijkstra
# ans = [[] for _ in range(vertexC + 1)]
# dijkstra(1)
#
# result = []
# for i in range(vertexC + 1):
#     if ans[i]:
#         result.append((i, ans[i]))
#
# print(len(result))
# for i in range(len(result)):
#     print(result[i][0], result[i][1])

# Bellman-Ford
result = [0] * (vertexC + 1)
bellman(1)

count = 0
for i in range(vertexC + 1):
    if result[i] != 0:
        count += 1

print(count)
for i in range(1, vertexC + 1):
    if result[i] != 0:
        print(i, result[i])
