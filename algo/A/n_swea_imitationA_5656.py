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


"""
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