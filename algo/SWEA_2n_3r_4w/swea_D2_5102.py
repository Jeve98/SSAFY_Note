T = int(input())
for case in range(T):
    nodeCount, edgeCount = map(int, input().split())

    edge = [[] for _ in range(nodeCount + 1)]
    for i in range(edgeCount):
        oneLine = list(map(int, input().split()))
        # 양방향 간선
        edge[oneLine[0]].append(oneLine[1])
        edge[oneLine[1]].append(oneLine[0])

    startNode, endNode = map(int, input().split())

    queue = [0] * nodeCount
    front = 0
    rear = 0
    queue[0] = startNode
    rear = (rear + 1) % len(queue)

    visited = [0] * (nodeCount + 1)
    visited[queue[front]] = 1

    while front != rear:
        for next in edge[queue[front]]:
            if visited[next] == 0:
                queue[rear] = next
                rear = (rear + 1) % len(queue)
                visited[next] = visited[queue[front]] + 1

        front = (front + 1) % len(queue)
        
        # end 방문 확인 시, 탐색 종료
        if visited[endNode] != 0:
            break

    # start, end가 연결된 경우 (방문 성공)
    if visited[endNode] != 0:
        distance = visited[endNode] - visited[startNode]
    # start, end가 연결되지 않은 경우 (방문 실패)
    else:
        distance = 0
    print(f'#{case + 1} {distance}')
