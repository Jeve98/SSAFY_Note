def analysis():
    twoSq = list(map(int, input().split()))

    # 좌표 정리
    pos = [[] for _ in range(2)]  # pos[sq num][x, y][left, right]
    for index in range(2):
        pos[0].append([twoSq[:4][index], twoSq[:4][index + 2]])
        pos[1].append([twoSq[4:][index], twoSq[4:][index + 2]])

    """
    두 점 이상에서의 겹침(사각형의 선분 만남, 일부-완전 겹침)도 점 겹침으로 출력
    # 점 탐색
    fSQ = []
    sSQ = []
    for reverse in range(0, 3, 2):
        for x, y in zip(pos[0][0], pos[0][1][::1 - reverse]):
            fSQ.append([x, y])
        for x, y in zip(pos[1][0], pos[1][1][::1 - reverse]):
            sSQ.append([x, y])

    for point in fSQ:
        if point in sSQ:
            return 'c'
    """

    if (pos[0][0][1] == pos[1][0][0] or pos[0][0][0] == pos[1][0][1]) and \
            (pos[0][1][1] == pos[1][1][0] or pos[0][1][0] == pos[1][1][1]):
        return 'c'

    # 선분 탐색
    # 0번 sq의 x좌표 중 우측 값이 1번 sq의 x좌표 중 좌측 값과 동일하거나
    # 0번 sq의 x좌표 중 좌측 값이 1번 sq의 x좌표 중 우측 값과 동일하고
    if pos[0][0][1] == pos[1][0][0] or pos[0][0][0] == pos[1][0][1]:
        # 0번 sq의 y좌표 중 상단 값이 1번 sq의 y좌표 중 하단 값보다 작지 않고
        # 0번 sq의 y좌표 중 하단 값이 1번 sq의 y좌표 중 상단 값보다 작은 경우
        if not pos[0][1][1] < pos[1][1][0] and pos[0][1][0] < pos[1][1][1]:
            return 'b'
        # 0번 sq의 y좌표 중 하단 값이 1번 sq의 y좌표 중 상단 값보다 크지 않고
        # 0번 sq의 y좌표 중 상단 값이 1번 sq의 y좌표 중 하단 값보다 큰 경우
        if not pos[0][1][0] > pos[1][1][1] and pos[0][1][1] > pos[1][1][0]:
            return 'b'
    # 0번 sq의 y좌표 중 상단 값이 1번 sq의 y좌표 중 하단 값과 동일하거나
    # 0번 sq의 y좌표 중 하단 값이 1번 sq의 y좌표 중 상단 값과 동일하고
    elif pos[0][1][1] == pos[1][1][0] or pos[0][1][0] == pos[1][1][1]:
        # 0번 sq의 x좌표 중 우측 값이 1번 sq의 x좌표 중 좌측 값보다 작지 않고
        # 0번 sq의 x좌표 중 좌측 값이 1번 sq의 x좌표 중 우측 값보다 작은 경우
        if not pos[0][0][1] < pos[1][0][0] and pos[0][0][0] < pos[1][0][1]:
            return 'b'
        # 0번 sq의 x좌표 중 좌측 값이 1번 sq의 x좌표 중 우측 값보다 크지 않고
        # 0번 sq의 x좌표 중 우측 값이 1번 sq의 x좌표 중 좌측 값보다 큰 경우
        if not pos[0][0][0] > pos[1][0][1] and pos[0][0][1] > pos[1][0][0]:
            return 'b'

    # 독립 개체 탐색
    # 0번 sq의 x좌표 중 우측 값이 1번 sq의 x좌표 중 좌측 값보다 작거나 (0번, 1번 순)
    # 0번 sq의 x좌표 중 좌측 값이 1번 sq의 x좌표 중 우측 값보다 큰 경우 (1번, 0번 순)
    if pos[0][0][1] < pos[1][0][0] or pos[0][0][0] > pos[1][0][1]:
        return 'd'
    # 0번 sq의 y좌표 중 상단 값이 1번 sq의 y좌표 중 하단 값보다 작거나
    # 0번 sq의 y좌표 중 하단 값이 1번 sq의 y좌표 중 상단 값보다 큰 경우
    if pos[0][1][1] < pos[1][1][0] or pos[0][1][0] > pos[1][1][1]:
        return 'd'

    # 그 외 (겹침)
    return 'a'


for i in range(4):
    ans = analysis()
    print(ans)
