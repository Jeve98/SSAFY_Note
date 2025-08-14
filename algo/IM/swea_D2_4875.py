def maze_runner(caseNum):
    size = int(input())

    maze = []
    for i in range(size):
        onLine = input()
        maze.append(onLine)

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    start = [0, 0]
    end = [size - 1, 0]
    for i in range(size):
        for j in range(size):
            if maze[i][j] == '3':
                start[0] = i
                start[1] = j
            if maze[i][j] == '2':
                end[0] = i
                end[1] = j

    stack = []
    visited = [start]
    while True:
        for addI, addJ in zip(di, dj):
            ni = start[0] + addI
            nj = start[1] + addJ
            if 0 <= ni < size and 0 <= nj < size:
                # 통로 발견 시
                if maze[ni][nj] == '0' and [ni, nj] not in visited:
                    stack.append(start)
                    start = [ni, nj]
                    visited.append(start)
                    break

                # 출구 발견 시
                if maze[ni][nj] == '2':
                    print(f'#{caseNum + 1} 1')
                    return
        # 현재 위치한 곳에서 상하좌우를 전부 확인했을 때,
        # 상하좌우가 전부 벽이거나 방문한 적 있는 통로인 경우
        else:
            if stack:
                start = stack.pop()
            # stack에 남은 곳이 없을 경우
            else:
                print(f'#{caseNum + 1} 0')
                return


T = int(input())
for case in range(T):
    maze_runner(case)
