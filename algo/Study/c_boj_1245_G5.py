# import sys
# sys.stdin = open('algo/input.txt', 'r')

row, col = map(int, input().split())

board = [0] * row
for i in range(row):
    board[i] = list(map(int, input().split()))

# delta
di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

queue = [0] * (row * col  + 1)
head = 0
rear = 0

visited = [[False] * col for _ in range(row)]

count = 0
for i in range(row):
    for j in range(col):
        if visited[i][j]:
            peak = False
        else:
            peak = True
            visited[i][j] = True

            for addI, addJ in zip(di, dj):
                ni = i + addI
                nj = j + addJ

                if 0 <= ni < row and 0 <= nj < col and board[i][j] < board[ni][nj]:
                    peak = False
                elif 0 <= ni < row and 0 <= nj < col and board[i][j] == board[ni][nj]:
                    if not visited[ni][nj]:
                        queue[rear] = [ni, nj]
                        visited[ni][nj] = True
                        rear = (rear + 1) % len(queue)
            
            while head != rear:
                newI, newJ = queue[head][0], queue[head][1]
                visited[newI][newJ] = True
                for addI, addJ in zip(di, dj):
                    ni = newI + addI
                    nj = newJ + addJ

                    if 0 <= ni < row and 0 <= nj < col and board[i][j] < board[ni][nj]:
                        peak = False    
                    elif 0 <= ni < row and 0 <= nj < col and board[i][j] == board[ni][nj]:
                        if not visited[ni][nj]:
                            queue[rear] = [ni, nj]
                            visited[ni][nj] = True
                            rear = (rear + 1) % len(queue)
                    
                head = (head + 1) % len(queue)
                
            if peak:
                count += 1

print(count)