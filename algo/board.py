pillarCount = int(input())

pillars = []
for i in range(pillarCount):
    oneLine = list(map(int, input().split()))   # [0]: x pos, [1]: height
    pillars.append(oneLine)

highest = 0
hIndex = 0
pillars.sort()
for i in range(pillarCount):
    if highest < pillars[i][1]:
        highest = pillars[i][1]
        hIndex = i

# 가장 높은 기둥의 높이 * 1
vol = highest

lpointer = 0
rpointer = hIndex
tmpHigh = 0
while True:
    if rpointer == 0:
        break

    for i in range(rpointer):
        if tmpHigh < pillars[i][1]:
            tmpHigh = pillars[i][1]
            lpointer = i

    vol += (pillars[rpointer][0] - pillars[lpointer][0]) * tmpHigh
    rpointer, lpointer, tmpHigh = lpointer, 0, 0

lpointer = hIndex
rpointer = 0
tmpHigh = 0
while True:
    if lpointer >= pillarCount - 1:
        break

    for i in range(lpointer + 1, pillarCount):
        if tmpHigh < pillars[i][1]:
            tmpHigh = pillars[i][1]
            rpointer = i

    vol += (pillars[rpointer][0] - pillars[lpointer][0]) * tmpHigh
    lpointer, rpointer, tmpHigh = rpointer, 0, 0

print(vol)
