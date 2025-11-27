import sys

sys.stdin = open("algo/input.txt", "r")

vertexC = int(input())

edgeList = [[] for _ in range(vertexC)]
for i in range(vertexC - 1):
    data = list(map(int, input().split()))
    edgeList[data[0] - 1].append(data[1] - 1)
    edgeList[data[1] - 1].append(data[0] - 1)

lca = list(map(int, input().split()))


def make_set(x):
    parents = [i for i in range(x + 1)]
    ranks = [0] * (x + 1)
    return parents, ranks


def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):
    repX = find_set(x)
    repY = find_set(y)

    if repX == repY:
        return

    if ranks[repX] < ranks[repY]:
        parents[repX] = repY
    elif ranks[repX] > ranks[repY]:
        parents[repY] = repX
    else:
        parents[repY] = repX
        ranks[repX] += 1


parents, ranks = make_set(vertexC)
for i in range(vertexC - 1):
    for j in edgeList[i]:
        union(i, j)

print(parents)
