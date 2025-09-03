T = int(input())
for case in range(T):
    size = int(input())

    # 1: wall, 0: street, 2: start, 3: end
    maze = []
    start = []
    end = []
    for i in range(size):
        oneLine = input()
        maze.append(oneLine)

        for j in range(size):
            if oneLine[j] == '2':
                start = [i, j]
            if oneLine[j] == '3':
                end = [i, j]

    queue = [[] for _ in range(size ** 2)]
    front = 0
    rear = 0
    queue[0] = start
    rear = (rear + 1) % len(queue)

    visited = [[0] * size for _ in range(size)]
    visited[queue[front][0]][queue[front][1]] = 1

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    while front != rear:
        for addI, addJ in zip(di, dj):
            ni = addI + queue[front][0]
            nj = addJ + queue[front][1]

            # 벽이 아니고 방문한 적이 없을 경우
            if 0 <= ni < size and 0 <= nj < size and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                queue[rear] = [ni, nj]
                rear = (rear + 1) % len(queue)
                visited[ni][nj] = visited[queue[front][0]][queue[front][1]] + 1

        front = (front + 1) % len(queue)

        # 도착점 방문 성공 시 탐색 중단
        if visited[end[0]][end[1]] != 0:
            break

    # 방문 성공
    if visited[end[0]][end[1]] != 0:
        # 도착지 제외
        distance = visited[end[0]][end[1]] - visited[start[0]][start[1]] - 1
    else:
        distance = 0
    print(f'#{case + 1} {distance}')
