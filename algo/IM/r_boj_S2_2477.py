supply = int(input())

data = []
count = [0] * 4
for i in range(6):
    oneLine = list(map(int, input().split()))  # [0]: direction, [1]: length
    data.append(oneLine)
    count[oneLine[0]-1] += 1

wh = []
near = []
for i in range(6):
    # 1번 나온 값(가장 긴 가로 세로) 저장
    if count[data[i][0]-1] == 1:
        wh.append(data[i][1])
        # 인접한 2번 나온 값을 저장
        if count[data[i-1][0]-1] == 2:
            near.append(data[i-1][1])
        else:
            if i+1 >= 6:
                i = -1
            near.append(data[i+1][1])
near.extend(wh)

delArea = 1
counting = 0
for i in range(6):
    if data[i][1] not in near:
        delArea *= data[i][1]

area = wh[0] * wh[1] - delArea
print(area * supply)
