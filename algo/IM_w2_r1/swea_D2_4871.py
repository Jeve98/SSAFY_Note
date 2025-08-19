# DFS
T = int(input())
for case in range(T):
    vertex, edge = map(int, input().split())

    # 간선 정보 (인접 리스트)
    edgeInfo = [[] for _ in range(vertex + 1)]
    for i in range(edge):
        oneLine = list(map(int, input().split()))   # [0]: start vertex, [1]: end vertex
        edgeInfo[oneLine[0]].append(oneLine[1])

    start, end = map(int, input().split())
    visited = [False] * (vertex + 1)
    visited[0] = True
    stack = []

    while True:
        # 방문하지 않은 vertex인 경우에만 stack에 추가
        if visited[start] is False:
            stack.append(start)
            visited[start] = True

        # 이동 가능한 vertex 탐색
        for i in range(len(edgeInfo[start])):
            next = edgeInfo[start][i]
            # 방문하지 않은 vertex면 start 변경
            if visited[next] == False:
                start = next
                break
        # 이동 가능한 vertex가 모두 방문한 vertex인 경우
        else:
            # stack에 방문한 곳으로 재이동
            if stack:
                start = stack.pop()
            else:
                break

    if visited[end] is True:
        print(f'#{case + 1} 1')
    else:
        print(f'#{case + 1} 0')
