# W H   - width height
# S     -store count
# d(1,2) left , d(3,4) up   - store position (1-n, 2-s, 3-w, 4-e)
# ...
# d(1,2) left , d(3,4) up   - people position (1-n, 2-s, 3-w, 4-e)

data = list(map(int, input().split()))  # [0] : width, [1] : height

storeCount = int(input())
store = []
for i in range(storeCount):
    oneLine = list(map(int, input().split()))   # [0] : 동서남북, [1] : 거리
    store.append(oneLine)

human = list(map(int, input().split())) # [0] : 동서남북, [1] : 거리

# (0, 좌표) or (width, 좌표)
# (좌표, 0) or (좌표, height)
storePos = []
for i in range(storeCount):
    # [1] : 좌측 경계에서 떨어진 정도
    if store[i][0] <= 2:
        # map의 좌측 하단을 (0, 0)으로 설정
        store[i][0] -= 1
        storePos.append((store[i][1], store[i][0] * data[1]))
    # [1] : 상단 경계에서 떨어진 정도
    else:
        store[i][0] -= 3
        storePos.append((store[i][0] * data[0], store[i][1]))

# [1] : 좌측 경계에서 떨어진 정도
if human[0] <= 2:
    # map의 좌측 하단을 (0, 0)으로 설정
    human[0] -= 1
    humanPos = (human[1], human[0] * human[1])
# [1] : 상단 경계에서 떨어진 정도
else:
    human[0] -= 3
    humanPos = (human[0] * data[0], human[1])

print(storePos)
print(humanPos)

# 거리 계산
move = 0
for target in storePos:
    Sx, Sy = target[0], target[1]
    Hx, Hy = humanPos[0], humanPos[1]
    move += abs(Sx - Hx)
    move += abs(Sy - Hy)

print(move)