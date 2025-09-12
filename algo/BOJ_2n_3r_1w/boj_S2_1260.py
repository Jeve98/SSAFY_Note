# import sys
# sys.stdin = open('../input.txt', 'r')


def DFS(now):
    for i in edge[now]:
        if not visited[i]:
            print(i, end=' ')
            visited[i] = True
            DFS(i)


vertexC, edgeC, startV = map(int, input().split())

edge = [[] for _ in range(vertexC + 1)]
for i in range(edgeC):
    oneLine = list(map(int, input().split()))   # [0]: start, [1]: arrive
    edge[oneLine[0]].append(oneLine[1])
    edge[oneLine[0]].sort()
    edge[oneLine[1]].append(oneLine[0])
    edge[oneLine[1]].sort()

visited = [False] * (vertexC + 1)
print(startV, end=' ')
visited[startV] = True
DFS(startV)

visited = [False] * (vertexC + 1)

queue = [0] * (vertexC + 1)
head = 0
rear = 0

queue[rear] = startV
rear = (rear + 1) % len(queue)
visited[startV] = True

print()
while head != rear:
    for i in edge[queue[head]]:
        if not visited[i]:
            visited[i] = True
            queue[rear] = i
            rear = (rear + 1) % len(queue)

    print(queue[head], end=' ')
    head = (head + 1) % len(queue)
