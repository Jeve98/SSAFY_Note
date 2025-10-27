# import sys
# sys.stdin = open('algo/input.txt', 'r')

size = int(input())
board = [0] * size
for i in range(size):
    board[i] = list(map(int, input().split()))

visited = [[False] * size for _ in range(size)]
stack = [0] * (size ** 2)
top = -1

now = (0, 0)
visited[0][0] = True
top += 1
stack[top] = now

while True:
    if top == -1:
        print('Hing')
        break

    if now[0] + board[stack[top][0]][stack[top][1]] < size and not visited[now[0] + board[stack[top][0]][stack[top][1]]][now[1]]:
        now = (now[0] + board[stack[top][0]][stack[top][1]], now[1])
        visited[now[0]][now[1]] = True
        top += 1
        stack[top] = now
    elif now[1] + board[stack[top][0]][stack[top][1]] < size and not visited[now[0]][now[1] + board[stack[top][0]][stack[top][1]]]:
        now = (now[0], now[1] + board[stack[top][0]][stack[top][1]])
        visited[now[0]][now[1]] = True
        top += 1
        stack[top] = now
    else:
        top -= 1
        now = stack[top]
    
    if now == (size - 1, size - 1):
        print('HaruHaru')
        break
    