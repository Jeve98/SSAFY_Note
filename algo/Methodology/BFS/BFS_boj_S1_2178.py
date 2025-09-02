row, col = map(int, input().split())

table = [0] * row
for i in range(row):
    oneLine = input()
    table[i] = oneLine

queue = [0] * (row * col)
head = 0
rear = 0
visited = [[0] * col for _ in range(row)]

queue[rear] = [0, 0]
rear = (rear + 1) % len(queue)
visited[0][0] = 1

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

while head != rear:
    for addI, addJ in zip(di, dj):
        ni = queue[head][0] + addI
        nj = queue[head][1] + addJ

        if 0 <= ni < row and 0 <= nj < col and table[ni][nj] == '1' and visited[ni][nj] == 0:
            queue[rear] = [ni, nj]
            rear = (rear + 1) % len(queue)
            visited[ni][nj] = visited[queue[head][0]][queue[head][1]] + 1

    head = (head + 1) % len(queue)

    if visited[row - 1][col - 1]:
        print(visited[row - 1][col - 1])
        break
