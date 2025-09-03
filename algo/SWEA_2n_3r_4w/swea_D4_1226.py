for case in range(10):
    caseNum = int(input())

    maze = []
    start = []
    end = []
    for i in range(16):
        oneLine = input()
        maze.append(oneLine)

        for j in range(16):
            if oneLine[j] == '2':
                start = [i, j]
            if oneLine[j] == '3':
                end = [i, j]

    queue = [[] for _ in range(16 ** 2)]
    front = 0
    rear = 0
    queue[0] = start
    rear = (rear + 1) % len(queue)

    visited = [[0] * 16 for _ in range(16)]
    visited[queue[front][0]][queue[front][1]] = 1

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while front != rear:
        for addI, addJ in zip(di, dj):
            ni = addI + queue[front][0]
            nj = addJ + queue[front][1]

            # 벽이 아니고 방문한 적 없을 경우
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                queue[rear] = [ni, nj]
                rear = (rear + 1) % len(queue)
                visited[ni][nj] = visited[queue[front][0]][queue[front][1]] + 1

        front = (front + 1) % len(queue)

        # 목적지 도달 시 탐색 중단
        if visited[end[0]][end[1]] != 0:
            break

    if visited[end[0]][end[1]] != 0:
        print(f'#{case + 1} 1')
    else:
        print(f'#{case + 1} 0')
