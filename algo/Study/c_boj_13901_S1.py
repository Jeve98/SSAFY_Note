# import sys
# sys.stdin = open('algo/input.txt', 'r')

row, col = map(int, input().split())
visited = [[False] * col for _ in range(row)]

obstacleC = int(input())
for i in range(obstacleC):
    i, j = map(int, input().split())
    visited[i][j] = True

now = list(map(int, input().split()))
visited[now[0]][now[1]] = True

direction = list(map(int, input().split()))     # 1: up, 2: down, 3: left, 4: right
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

while True:
    move = False
    for dir in direction:
        while True:
            ni = now[0] + di[dir]
            nj = now[1] + dj[dir]

            if 0 <= ni < row and 0 <= nj < col and not visited[ni][nj]:
                visited[ni][nj] = True
                now[0] = ni
                now[1] = nj
                move = True
            else:
                break
    
    if not move:
        break

print(now[0], now[1])
