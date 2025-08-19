# W H   - width height
# S     -store count
# d(1,2) left , d(3,4) up   - store position (1-n, 2-s, 3-w, 4-e)
# ...
# d(1,2) left , d(3,4) up   - people position (1-n, 2-s, 3-w, 4-e)

# 좌표 변환
data = list(map(int, input().split()))  # [0] : width, [1] : height

storeCount = int(input())
store = []
for i in range(storeCount):
    oneLine = list(map(int, input().split()))  # [0] : 동서남북, [1] : 거리
    store.append(oneLine)

human = list(map(int, input().split()))  # [0] : 동서남북, [1] : 거리

# (0, 좌표) or (width, 좌표)
# (좌표, 0) or (좌표, height)
storePos = []
for i in range(storeCount):
    # [1] : 좌측 경계에서 떨어진 정도
    if store[i][0] <= 2:
        # map의 좌측 하단을 (0, 0)으로 설정
        store[i][0] -= 1
        storePos.append((store[i][1], store[i][0] * data[1]))
        # 방향 정보 복구
        store[i][0] += 1
    # [1] : 상단 경계에서 떨어진 정도
    else:
        store[i][0] -= 3
        storePos.append((store[i][0] * data[0], store[i][1]))
        # 방향 정보 복구 (이후 사용을 위해 범위 확장)
        store[i][0] += 4

# [1] : 좌측 경계에서 떨어진 정도
if human[0] <= 2:
    # map의 좌측 하단을 (0, 0)으로 설정
    human[0] -= 1
    humanPos = (human[1], human[0] * data[1])
    # 방향 정보 복구
    human[0] += 1
# [1] : 상단 경계에서 떨어진 정도
else:
    human[0] -= 3
    humanPos = (human[0] * data[0], human[1])
    # 방향 정보 복구 (이후 사용을 위해 범위 확장)
    human[0] += 4

print(storePos)
print(humanPos)

# 거리 계산
move = 0
index = 0
for target in storePos:
    Sx, Sy = target[0], target[1]
    Hx, Hy = humanPos[0], humanPos[1]
    # 반대편에 위치한 경우
    if abs(human[0] - store[index][0]) == 1:
        tmp0 = Sx + Sy + Hx + Hy
        tmp1 = 2 * data[0] - Sx - Hx + Sy + Hy
        tmp2 = 2 * data[1] - Sy - Hy + Sx + Hx
        move += min(tmp0, tmp1, tmp2)
    else:
        move += abs(Sx - Hx)
        move += abs(Sy - Hy)

    index += 1

print(move)


# 1차원 직선화
def change_map(tar, wh):
    # north
    if tar[0] == 1:
        return tar[1]
    # south
    elif tar[0] == 2:
        return wh[0] + wh[1] + wh[0] - tar[1]
    # west
    elif tar[0] == 3:
        return 2 * wh[0] + wh[1] + wh[1] - tar[1]
    # east
    else:
        return wh[0] + tar[1]


data = list(map(int, input().split()))  # [0] : width, [1] : height

storeCount = int(input())
store = []
for i in range(storeCount):
    oneLine = list(map(int, input().split()))  # [0] : 동서남북, [1] : 거리
    store.append(oneLine)

human = list(map(int, input().split()))  # [0] : 동서남북, [1] : 거리

storePos = []
for i in range(storeCount):
    storePos.append(change_map(store[i], data))

humanPos = change_map(human, data)
print(storePos)
move = 0
wholeLength = 2 * (data[0] + data[1])
for i in range(storeCount):
    tmpLength = abs(storePos[i] - humanPos)
    move += min(tmpLength, wholeLength - tmpLength)

print(move)