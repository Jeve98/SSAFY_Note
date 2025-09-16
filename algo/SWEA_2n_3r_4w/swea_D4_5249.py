# import sys
# sys.stdin = open('../input.txt', 'r')


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
    vertexC, edgeC = map(int, input().split())

    edgeList = [0] * edgeC
    for i in range(edgeC):
        oneLine = list(map(int, input().split()))       # [0]: start, [1]: end, [2]: weight
        edgeList[i] = oneLine

    edgeList.sort(key=lambda x: x[2])

    parents = [i for i in range(vertexC + 1)]
    count = 0
    total = 0
    for i in range(edgeC):
        start = edgeList[i][0]
        end = edgeList[i][1]
        w = edgeList[i][2]

        if find_set(start) != find_set(end):
            total += w
            count += 1
            union(start, end)

            if count == vertexC:
                break

    print(f'#{case + 1} {total}')
