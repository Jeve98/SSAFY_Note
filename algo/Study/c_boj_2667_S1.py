# import sys
# sys.stdin = open('algo/input.txt', 'r')

size = int(input())
apart = [0] * size
for i in range(size):
    apart[i] = input()

# delta
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

queue = [0] * (size ** 2 + 1)
head = 0
rear = 0
length = len(queue)

visited = [[False] * size for _ in range(size)]

total = []
for i in range(size):
    for j in range(size):
        if apart[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            count = 1
            queue[rear] = (i, j)
            rear = (rear + 1) % length

            while head != rear:
                for addI, addJ in zip(di, dj):
                    ni = queue[head][0] + addI
                    nj = queue[head][1] + addJ

                    if 0 <= ni < size and 0 <= nj < size and apart[ni][nj] == '1' and not visited[ni][nj]:
                        visited[ni][nj] = True
                        count += 1
                        queue[rear] = (ni, nj)
                        rear = (rear + 1) % length
                
                head = (head + 1) % length
            
            total.append(count)

print(len(total))
total.sort()
for i in total:
    print(i)
