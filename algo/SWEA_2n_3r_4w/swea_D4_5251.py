# import sys
# sys.stdin = open('../input.txt', 'r')
from heapq import heappush as hpush, heappop as hpop


def dijkstra(startNode):
    primaryQ = [(0, startNode)]

    distance = [100000] * (vertexC + 1)
    distance[startNode] = 0

    while primaryQ:
        nowDis, nowNode = hpop(primaryQ)

        if distance[nowNode] < nowDis:
            continue

        for w, end in edgeData[nowNode]:
            newDis = nowDis + w

            if distance[end] <= newDis:
                continue

            distance[end] = newDis
            hpush(primaryQ, (newDis, end))

    return distance


T = int(input())
for case in range(T):
    vertexC, edgeC = map(int, input().split())

    edgeData = [[] for _ in range(vertexC + 1)]
    for i in range(edgeC):
        oneLine = list(map(int, input().split()))       # [0]: start, [1]: end, [2]: weight
        edgeData[oneLine[0]].append((oneLine[2], oneLine[1]))

    result = dijkstra(0)
    print(f'#{case + 1} {result[vertexC]}')
