# import sys
# sys.stdin = open('../input.txt', 'r')
import math


def find_set(n):
    if n == parents[n]:
        return n

    parents[n] = find_set(parents[n])

    return parents[n]


def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return

    parents[rep_y] = rep_x


T = int(input())
for case in range(T):
    islandC = int(input())

    vertexData = [0] * islandC
    xPos = list(map(float, input().split()))
    yPos = list(map(float, input().split()))
    for i in range(islandC):
        vertexData[i] = (xPos[i], yPos[i])

    tax = float(input())

    parents = [i for i in range(islandC)]

    dis = []
    for i in range(islandC - 1):
        for j in range(i, islandC):
            tmp = math.sqrt((vertexData[i][0] - vertexData[j][0]) ** 2 + (vertexData[i][1] - vertexData[j][1]) ** 2)
            dis.append((i, j, tmp))
    dis.sort(key=lambda x: x[2])

    count = 0
    total = 0
    for i in range(len(dis)):
        start = dis[i][0]
        end = dis[i][1]
        w = dis[i][2]

        if find_set(start) != find_set(end):
            total += (w ** 2)
            union(start, end)
            count += 1

            if count == islandC - 1:
                break

    print(f'#{case + 1} {round(total * tax)}')
