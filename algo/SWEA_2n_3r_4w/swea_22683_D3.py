# import sys
# sys.stdin = open('../input.txt', 'r')


def DFS(now, cut, nowDirection, count):
    global ans

    if now == end:
        if count < ans:
            ans = count

        return

    if count >= ans:
        return

    for dir in range(4):
        ni = now[0] + di[dir]
        nj = now[1] + dj[dir]

        tmp = abs(dir - nowDirection)
        if tmp == 3:
            tmp = 1

        if 0 <= ni < size and 0 <= nj < size and not visited[ni][nj]:
            if board[ni][nj] == 'T' and cut > 0:
                visited[ni][nj] = True
                DFS((ni, nj), cut - 1, dir, count + tmp + 1)
                visited[ni][nj] = False
            elif board[ni][nj] != 'T':
                visited[ni][nj] = True
                DFS((ni, nj), cut, dir, count + tmp + 1)
                visited[ni][nj] = False


T = int(input())
for case in range(T):
    size, cutting = map(int, input().split())
    board = [0] * size
    start = 0
    end = 0
    for i in range(size):
        board[i] = input()

        for j in range(size):
            if board[i][j] == 'X':
                start = (i, j)
            elif board[i][j] == 'Y':
                end = (i, j)

    # delta - 상우하좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    direction = 0

    visited = [[False] * size for _ in range(size)]
    visited[start[0]][start[1]] = True

    ans = 2100000000
    DFS(start, cutting, direction, 0)

    if ans == 2100000000:
        print(f'#{case + 1} {-1}')
    else:
        print(f'#{case + 1} {ans}')
