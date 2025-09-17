import sys
sys.stdin = open('../input.txt', 'r')


def DFS(start, canDig, length):
    global ans

    for addI, addJ in zip(di, dj):
        ni = start[0] + addI
        nj = start[1] + addJ

        if 0 <= ni < size and 0 <= nj < size and not visited[ni][nj]:
            if board[start[0]][start[1]] > board[ni][nj]:
                visited[ni][nj] = True
                DFS([ni, nj], canDig, length + 1)
                visited[ni][nj] = False
            elif canDig and board[start[0]][start[1]] > board[ni][nj] - maxDig:
                tmp = board[ni][nj]
                board[ni][nj] = board[ni][nj] - (board[ni][nj] - board[start[0]][start[1]] + 1)
                visited[ni][nj] = True
                DFS([ni, nj], not canDig, length + 1)
                board[ni][nj] = tmp
                visited[ni][nj] = False

    if length > ans:
        ans = length


T = int(input())
for case in range(T):
    size, maxDig = map(int, input().split())

    board = [0] * size
    maxHeight = 0
    maxHIndex = []
    for i in range(size):
        board[i] = list(map(int, input().split()))

        for j in range(size):
            if board[i][j] > maxHeight:
                maxHeight = board[i][j]
                maxHIndex = [(i, j)]
            elif board[i][j] == maxHeight:
                maxHIndex.append((i, j))

    # delta
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    visited = [[False] * size for _ in range(size)]

    ans = 0
    for startNode in maxHIndex:
        visited[startNode[0]][startNode[1]] = True
        DFS(startNode, True, 1)
        visited[startNode[0]][startNode[1]] = False

    print(f'#{case + 1} {ans}')
