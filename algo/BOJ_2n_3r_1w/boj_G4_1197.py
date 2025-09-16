import sys
sys.stdin = open('../input.txt', 'r')


def find_set(n):
    # if n == parents[n]:
    #     return n
    #
    # parents[n] = find_set(parents[n])
    # return parents[n]

    while n != parents[n]:
        tmp = n
        n = parents[n]
        parents[tmp] = parents[n]

    return n


def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return

    parents[rep_y] = rep_x


vertexC, edgeC = map(int, input().split())

edgeList = [0] * edgeC
for i in range(edgeC):
    edgeList[i] = list(map(int, input().split()))   # [0]: start, [1]: end, [2]: weight
edgeList.sort(key=lambda x: x[2])

parents = [i for i in range(vertexC + 1)]

count = 0
total = 0
for edge in edgeList:
    start = edge[0]
    end = edge[1]
    w = edge[2]

    if find_set(start) != find_set(end):
        total += w
        count += 1
        union(start, end)

        if count == vertexC - 1:
            break

print(total)
