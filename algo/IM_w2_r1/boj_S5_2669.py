everySq = set()
for i in range(4):
    oneLine = list(map(int, input().split()))   # [0]: first x, [1]: first y, [2]: second x, [3]: second y
    # 좌표 1개를 1칸의 공간으로 변환한다면, 한 쪽 끝 좌표를 포함하지 않는 것으로 모든 공간이 표현됨
    for row in range(oneLine[0], oneLine[2]):
        for col in range(oneLine[1], oneLine[3]):
            everySq.add((row, col))

print(len(everySq))

# 배열을 하나의 공간으로 인식해서 칠하는 방법