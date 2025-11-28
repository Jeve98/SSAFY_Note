import sys

sys.stdin = open("algo/input.txt", "r")


def DFS(start, end):
    if start == end:
        return []

    stack = [0] * (vertexC + 1)
    top = -1

    visited = [False] * (vertexC + 1)

    top += 1
    stack[top] = start
    visited[start] = True

    tmp = [start]
    isReturn = False
    while top != -1:
        for nextNode in edgeList[stack[top]]:
            if nextNode == end:
                isReturn = True
                visited[nextNode] = True
            elif not visited[nextNode]:
                top += 1
                stack[top] = nextNode
                visited[nextNode] = True

                tmp.append(nextNode)
                break
        else:
            top -= 1
    print(tmp)

    if isReturn:
        return tmp


vertexC = int(input())

edgeList = [set() for _ in range(vertexC + 1)]
for i in range(vertexC - 1):
    data = list(map(int, input().split()))
    edgeList[data[0]].add(data[1])
    edgeList[data[1]].add(data[0])

lca = list(map(int, input().split()))  # 0: child, 1: child, 2: parents

route = []
for i in range(2):
    route.extend(DFS(lca[i], lca[2]))

print(vertexC - len(route))
