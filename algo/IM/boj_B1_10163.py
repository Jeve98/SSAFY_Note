# 메모리 초과
count = int(input())

paper = []
for i in range(count):
    oneLine = list(map(int, input().split()))   # [0]: x, [1]: y, [2]: width, [3]: height
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
