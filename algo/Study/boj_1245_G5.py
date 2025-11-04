import sys
sys.stdin = open('algo/input.txt', 'r')

row, col = map(int, input().split())

board = [0] * row
for i in range(row):
    board[i] = list(map(int, input().split()))

# delta
di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

visited = [[False] * col for _ in range(row)]


def search(pos):
    visited[pos[0]][pos[1]] = True

    no = False
    for addI, addJ in zip(di, dj):
        ni = addI + pos[0]
        nj = addJ + pos[1]

        if 0 <= ni < row and 0 <= nj < col and board[pos[0]][pos[1]] < board[ni][nj]:
            no = True
        elif pos[0] <= ni < row and pos[1] <= nj < col and board[pos[0]][pos[1]] == board[ni][nj]:
            if visited[ni][nj]:
                no = True

            if no:
                search([ni, nj])
            else:
                no = search([ni, nj])

    return no


count = 0
for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            no = search([i, j])

            if not no:
                print(i, j)
                count += 1

print(count)
