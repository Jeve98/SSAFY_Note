# import sys
# sys.stdin = open("algo/input.txt", "r")

from collections import deque


def BFS():
    global maxClean

    queue = deque()

    visited = [[False] * col for _ in range(row)]

    for each in virus:
        visited[each[0]][each[1]] = True
        queue.append(each)

        while queue:
            now = queue.popleft()
            for addI, addJ in zip(di, dj):
                ni = now[0] + addI
                nj = now[1] + addJ

                if (
                    0 <= ni < row
                    and 0 <= nj < col
                    and not visited[ni][nj]
                    and board[ni][nj] == 0
                ):
                    visited[ni][nj] = True
                    queue.append((ni, nj))

    count = 0
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and board[i][j] == 0:
                count += 1

    if count > maxClean:
        maxClean = count


row, col = map(int, input().split())

board = [0] * row
virus = []
blank = []
for i in range(row):
    board[i] = list(map(int, input().split()))

    for j in range(col):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            blank.append((i, j))

# delta
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

maxClean = 0
for i in range(len(blank) - 2):
    board[blank[i][0]][blank[i][1]] = 1

    for j in range(i + 1, len(blank) - 1):
        board[blank[j][0]][blank[j][1]] = 1

        for k in range(j + 1, len(blank)):
            board[blank[k][0]][blank[k][1]] = 1
            BFS()
            board[blank[k][0]][blank[k][1]] = 0
        board[blank[j][0]][blank[j][1]] = 0
    board[blank[i][0]][blank[i][1]] = 0


print(maxClean)
