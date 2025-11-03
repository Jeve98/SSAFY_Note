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
            return True
        elif 0 <= ni < row and 0 <= nj < col and not visited[ni][nj] and board[pos[0]][pos[1]] == board[ni][nj]:
            no = search([ni, nj])
            if no:
                return True
        elif 0 <= ni < row and 0 <= nj < col and board[pos[0]][pos[1]] == board[ni][nj]:
            pass
    
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
