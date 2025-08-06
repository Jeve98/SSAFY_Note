# w h   - w : width, h : height
# p q   - first pos(p,q)
# t     - time

"""
# 막대한 t로 인해 타임 아웃 - 애드 혹 문제
di = 1
dj = 1

w, h = map(int, input().split())    # w: max col, h: max row
pos = list(map(int, input().split()))   # [0]: x, [1]: y
time = int(input())

for hour in range(time):
    tmpI, tmpJ = pos[0] + di, pos[1] + dj

    if tmpI >= w or tmpI <= 0:
        di *= -1
    if tmpJ >= h or tmpJ <= 0:
        dj *= -1

    pos[0], pos[1] = tmpI, tmpJ

print(pos[0], pos[1])
"""

# 점화식 (애드 혹)
w, h = map(int, input().split())    # w: max col, h: max row
pos = list(map(int, input().split()))   # [0]: x, [1]: y
time = int(input())

# 방향까지 동일한 상태로 원래의 x, y 좌표로 돌아오는 주기는 2w, 2h 이다
# ex) x = 0 and right, x가 다시 0이 될 때는 w만큼의 거리를 2번 움직였을 때 (반대를 찍고 돌아왔을 때)
x = (pos[0] + time) % (w * 2)
y = (pos[1] + time) % (h * 2)

# x, y 좌표가 w, h보다 큰 경우는 되돌아오고 있는 경우로 2w, 2h에서 좌표를 빼면 현재 위치를 알 수 있음
if x > w:
    x = w * 2 - x
if y > h:
    y = h * 2 -y

print(x, y)
