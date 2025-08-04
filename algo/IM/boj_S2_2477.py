supply = int(input())

data = []
count = [0] * 4
for i in range(6):
    oneLine = list(map(int, input().split()))  # [0]: direction, [1]: length
    data.append(oneLine)
    count[oneLine[0]-1] += 1

wh = []
for i in range(6):
    if count[data[i][0]-1] == 1:
        wh.append(data[i][1])

delArea = 0
counting = 0
for i in range(6):
    if count[data[i][0]-1] == 2:
        if count[data[i-1][0]-1] == 2 and count[data[i+1][0]-1] == 2:
            delArea = data[i][1] * data[i+1][1]
            print(data[i][1], data[i+1][1])

area = wh[0] * wh[1] - delArea
print(area * supply)