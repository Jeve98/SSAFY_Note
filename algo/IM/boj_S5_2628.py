# w h (1 <= w, h <= 100)
# cutting
# 0 num or 1 num    (0 : 가로, 1 : 세로)
# ...

data = list(map(int, input().split()))  # [0] : width, [1] : height
cut = int(input())
be_cut = [[[0, 0], [data[0], data[1]]]]
for i in range(cut):
    oneLine = list(map(int, input().split()))   # [0] : direction, [1] : cutting number
    tmp = []
    for target in be_cut:
        startPos = target[0]
        endPos = target[1]

        fPiece = []
        sPiece = []
        # 0 - 가로로 잘리면, y 좌표에 영향을 준다
        if oneLine[0] == 0:
            if startPos[1] < oneLine[1] < endPos[1]:
                fPiece = [[startPos[0], startPos[1]], [endPos[0], oneLine[1]]]
                sPiece = [[startPos[0], oneLine[1]], [endPos[0], endPos[1]]]
            else:
                tmp.append([startPos, endPos])
                continue
        # 1 - 세로로 잘리면, x 좌표에 영향을 준다
        else:
            if startPos[0] < oneLine[1] < endPos[0]:
                fPiece = [[startPos[0], startPos[1]], [oneLine[1], endPos[1]]]
                sPiece = [[oneLine[1], startPos[1]], [endPos[0], endPos[1]]]
            else:
                tmp.append([startPos, endPos])
                continue
        tmp.append(fPiece)
        tmp.append(sPiece)
    be_cut = tmp[:]

maxVol = 0
for target in be_cut:
    startPos = target[0]
    endPos = target[1]

    w = abs(startPos[0] - endPos[0])
    h = abs(startPos[1] - endPos[1])

    if maxVol < w * h:
        maxVol = w * h

print(maxVol)
