for case in range(10):
    caseNum, edge = map(int, input().split())

    edgeInfo = [[] for _ in range(100)]
    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        # 짝수 번째는 시작 노드, 홀수 번째는 도착 노드
        edgeInfo[data[i]].append(data[i + 1])

    visited = [False] * 100
    stack = []
    start = 0

    while True:
        if visited[start] is False:
            visited[start] = True
            stack.append(start)

        for i in range(len(edgeInfo[start])):
            next = edgeInfo[start][i]
            if visited[next] is False:
                start = next
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break

    if visited[99] is True:
        print(f'#{caseNum} 1')
    else:
        print(f'#{caseNum} 0')
