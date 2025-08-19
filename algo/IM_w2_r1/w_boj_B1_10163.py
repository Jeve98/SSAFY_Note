# 메모리 초과
"""
count = int(input())

paper = []
for i in range(count):
    oneLine = list(map(int, input().split()))  # [0]: x, [1]: y, [2]: width, [3]: height
    # 좌표로 변환    ([0], [1]: 좌하단 (x, y), [2], [3]: 우상단 (x, y))
    oneLine[2] += oneLine[0]
    oneLine[3] += oneLine[1]

    tmp = set()
    for row in range(oneLine[0], oneLine[2]):
        for col in range(oneLine[1], oneLine[3]):
            tmp.add((row, col))
    paper.append(tmp)

every = set()

for i in range(count - 1, -1, -1):
    paper[i] -= every
    every.update(paper[i])

for i in range(count):
    vol = len(paper[i])
    print(vol)
"""

# Time out in worst case
"""
count = int(input())

paper = [[0] * 1001 for _ in range(1001)]
LU = [1000, 1000]
RD = [0, 0]
for each in range(count):
    oneLine = list(map(int, input().split()))   # [0]: x, [1]: y, [2]: width, [3]: height
    # 좌표로 변환    ([0], [1]: 좌하단 (x, y), [2], [3]: 우상단 (x, y))
    oneLine[2] += oneLine[0]
    oneLine[3] += oneLine[1]

    # 계산 범위 제한  >> 전체 맵을 한정하는 방법. 맵을 한정시키는 것이 아니라 각 색종이 객체의 크기만큼 순회.
    # y : 312 64 60
    # n : 316 1204 1188
    # worst case : 각 색종이가 전체 맵의 꼭짓점에 개별적으로 위치한 경우
    for i in range(2):
        if LU[i] >= oneLine[i]:
            LU[i] = oneLine[i]
        if RD[i] <= oneLine[2 + i]:
            RD[i] = oneLine[2 + i]

    for i in range(oneLine[0], oneLine[2]):
        for j in range(oneLine[1], oneLine[3]):
            paper[i][j] = each + 1

for each in range(count):
    counting = 0
    for i in range(LU[0], RD[0]):
        for j in range(LU[1], RD[1]):
            if paper[i][j] == each + 1:
                counting += 1

    print(counting)
"""

count = int(input())

paper = [[0] * 1001 for _ in range(1001)]
paperPos = []
for each in range(count):
    oneLine = list(map(int, input().split()))   # [0]: x, [1]: y, [2]: width, [3]: height
    # 좌표로 변환    ([0], [1]: 좌하단 (x, y), [2], [3]: 우상단 (x, y))
    oneLine[2] += oneLine[0]
    oneLine[3] += oneLine[1]

    # 각 색종이별 좌표를 저장
    paperPos.append(oneLine)

    """
    for i in range(oneLine[0], oneLine[2]):
        for j in range(oneLine[1], oneLine[3]):
            paper[i][j] = each + 1
    """
    for row in range(oneLine[0], oneLine[2]):
        paper[row][oneLine[1]:oneLine[3]] = [each + 1] * (oneLine[3] - oneLine[1])

for each in range(count):
    counting = 0
    """
    # 각 색종이의 크기만큼만 순회
    for i in range(paperPos[each][0], paperPos[each][2]):
        for j in range(paperPos[each][1], paperPos[each][3]):
            if paper[i][j] == each + 1:
                counting += 1
    """
    for row in range(paperPos[each][0], paperPos[each][2]):
        counting += paper[row].count(each + 1)

    print(counting)
