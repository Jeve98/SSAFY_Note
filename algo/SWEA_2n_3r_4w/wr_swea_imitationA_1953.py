# 연결될 수 없는 파이프까지 계산에 포함됨
"""
def move(nowTime, nowPos):
    global count

    # 종료조건
    # 1. 시간 초과
    # 2. 이동 가능한 방이 없거나, 이동 가능한 방이 전부 방문한 기록이 있는 경우
    if nowTime > time:
        return

    key = underground[nowPos[0]][nowPos[1]]
    for index in range(4):
        ni = tunnel[key][0][index] + nowPos[0]
        nj = tunnel[key][1][index] + nowPos[1]

        if 0 <= ni < row and 0 <= nj < col and visited[ni][nj] is False and underground[ni][nj] != '0':
            visited[ni][nj] = True
            move(nowTime + 1, [ni, nj])
            count += 1


T = int(input())
for case in range(T):
    row, col, startI, startJ, time = map(int, input().split())

    underground = []
    for i in range(row):
        oneLine = list(input().split())
        underground.append(oneLine)

    # delta
    tunnel = {
        # 상하좌우
        '1': [[-1, 1, 0, 0], [0, 0, -1, 1]],
        # 상하
        '2': [[-1, 1, 0, 0], [0, 0, 0, 0]],
        # 좌우
        '3': [[0, 0, 0, 0], [0, 0, -1, 1]],
        # 상우
        '4': [[-1, 0, 0, 0], [0, 0, 0, 1]],
        # 하우
        '5': [[0, 1, 0, 0], [0, 0, 0, 1]],
        # 하좌
        '6': [[0, 1, 0, 0], [0, 0, -1, 0]],
        # 상좌
        '7': [[-1, 0, 0, 0], [0, 0, -1, 0]],
    }

    visited = [[False] * col for _ in range(row)]
    visited[startI][startJ] = True
    count = 1

    # time은 인자로 보내줘야 모든 경우가 동시에 작동
    move(2, [startI, startJ])

    print(f'#{case + 1} {count}')
"""

# delta 탐색 응용
T = int(input())
for case in range(T):
    row, col, startI, startJ, time = map(int, input().split())

    underground = []
    for i in range(row):
        oneLine = list(map(int, input().split()))
        underground.append(oneLine)

    # 상하좌우
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # immutable type, int
    type = {
        # 벽
        0: [],
        # 상하좌우
        1: [0, 1, 2, 3],
        # 상하
        2: [0, 1],
        # 좌우
        3: [2, 3],
        # 상우
        4: [0, 3],
        # 하우
        5: [1, 3],
        # 하좌
        6: [1, 2],
        # 상좌
        7: [0, 2],
    }

    # 두 터널이 연결되어 있음을 확인하기 위해서는 이동가능한 방향이 서로 반대가 되어야 함
    # 상(0) <-> 하(1), 좌(2) <-> 우(3)
    opposite = {
        0: 1,
        1: 0,
        2: 3,
        3: 2,
    }

    queue = [[] for _ in range(row * col + 1)]
    front = 0
    rear = 0
    queue[rear] = [startI, startJ]
    rear = (rear + 1) % len(queue)

    visited = [[0] * col for _ in range(row)]
    visited[startI][startJ] = 1
    visitCount = 1

    now = 1
    while front != rear:
        # 현재 queue[front]에 존재하는 요소가 언제 input 됐는지 시간을 확인
        now = visited[queue[front][0]][queue[front][1]]
        # input 된 시간이 예정 시간 이상일 경우, 해당 요소에 대한 추가적인 검사는 필요하지 않음
        if now >= time:
            # 다음 queue 값을 확인 하기 위해 front 증가
            front = (front + 1) % len(queue)
            continue

        now += 1
        typeCheck = underground[queue[front][0]][queue[front][1]]
        for eachType in type[typeCheck]:
            # delta 탐색 응용
            ni = delta[eachType][0] + queue[front][0]
            nj = delta[eachType][1] + queue[front][1]

            if 0 <= ni < row and 0 <= nj < col and opposite[eachType] in type[underground[ni][nj]] and visited[ni][nj] == 0:
                queue[rear] = [ni, nj]
                rear = (rear + 1) % len(queue)
                # visited 배열에 저장되는 값은 현재 기준이 되는 요소가 input된 시간 + 1 (다음 시간이 되어야 queue에 input되므로)
                visited[ni][nj] = visited[queue[front][0]][queue[front][1]] + 1
                visitCount += 1

        front = (front + 1) % len(queue)

    print(f'#{case + 1} {visitCount}')
