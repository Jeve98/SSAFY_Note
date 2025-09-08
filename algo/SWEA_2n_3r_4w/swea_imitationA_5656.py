"""
T = int(input())
for case in range(T):
    shoot, row, col = list(map(int, input().split()))

    stage = []
    leftBrick = [0] * col
    for i in range(row):
        oneLine = list(map(int, input().split()))
        stage.append(oneLine)

        for j in range(col):
            if oneLine[j] != 0:
                leftBrick[j] += 1



for shoot
    for leftBrick (is not 0)
        선택된 col에 맞춰 블록 파괴
        전체를 검사하며 stage, leftBrick 갱신
    stage, leftBrick 원복
--------------------------------------------------
def func(stage, leftbrick, count):
    횟수 초과
    if count == shoot:
        tmpSum = sum(leftbrick)
        if maxbrick < tmpSum:
            maxbrick = tmpSum
    
    for col in leftbrick (is not 0)
        블록 파괴, leftbrick 갱신, stage 변경
        stage = staging(stage, leftbrick)
        func(stage, leftbrick, count + 1)

def destroy(stage, leftbrick, pos):
    ??

def staging(stage, leftbrick):
    for col > 0
        for row
            if find 0 and count < leftbrick[row]
                save = row
            # 이번 col에 대한 정리가 끝난 경우
            elif count == leftbrick[row]
                break 
            else
                count ++
                if save
                    stage[save][col] = find
                    find = 0
                    save ++    
            
    return stage

"""
import copy


def order(count, stage):
    global ans

    if count == drop:
        tmpScore = 0
        for i in range(height):
            for j in range(width):
                if stage[i][j] != 0:
                    tmpScore += 1

        if ans > tmpScore:
            ans = tmpScore
        return

    for i in range(width):
        tmpStage = dropping(stage, i)
        order(count + 1, tmpStage)


def dropping(stage, index):
    for i in range(height):
        if stage[i][index] != 0:
            stage = destroy([i, index], stage)
            stage = staging(stage)
            return stage
    return stage


def destroy(pos, stage):
    myStage = copy.deepcopy(stage)

    if 0 <= pos[0] < height and 0 <= pos[1] < width:
        go = myStage[pos[0]][pos[1]]
        myStage[pos[0]][pos[1]] = 0
        for i in range(1, go):
            myStage = destroy([pos[0], pos[1] - i], myStage)
            myStage = destroy([pos[0], pos[1] + i], myStage)
            myStage = destroy([pos[0] - i, pos[1]], myStage)
            myStage = destroy([pos[0] + i, pos[1]], myStage)

    return myStage


def staging(stage):
    for i in range(width):
        find = False
        nextFind = False
        index = 0
        count = 0
        for j in range(height):
            if stage[j][i] != 0 and not nextFind:
                find = True
                index = j
            elif find and stage[j][i] == 0:
                nextFind = True
                count += 1
            elif nextFind and stage[j][i] != 0:
                for k in range(index, -1, -1):
                    stage[k + count][i] = stage[k][i]
                    stage[k][i] = 0
                index = j
                nextFind = False
                count = 0

        if nextFind:
            for j in range(index, -1, -1):
                stage[j + count][i] = stage[j][i]
                stage[j][i] = 0

    return stage


T = int(input())
for case in range(T):
    drop, width, height = map(int, input().split())

    stage = [[] for _ in range(height)]
    for i in range(height):
        oneLine = list(map(int, input().split()))
        stage[i] = oneLine

    ans = 2100000000
    order(0, stage)
    print(f'#{case + 1} {ans}')
