import sys
sys.stdin = open('algo/input.txt', 'r')

paddleC = int(input())
paddle = list(map(int, input().split()))
start, end = map(int, input().split())
start -= 1
end -= 1

direction = 1
if start > end:
    direction *= -1

queue = [0] * (paddleC * 10)
head = 0
rear = 0
length = len(queue)
visited = [False] * paddleC

queue[rear] = (paddle[start], start, 0)
rear = (rear + 1) % length
visited[start] = True

find = False
while head != rear:
    if queue[head][1] == end:
        print(queue[head][2])
        find = True
        break

    next = queue[head][1]
    while True:
        next += queue[head][0] * direction

        if direction == 1:
            if next <= end and not visited[next]:
                queue[rear] = (paddle[next], next, queue[head][2] + 1)
                rear = (rear + 1) % length
                visited[next] = True
            elif next > end:
                break
        else:
            if next >= end and not visited[next]:
                queue[rear] = (paddle[next], next, queue[head][2] + 1)
                rear = (rear + 1) % length
                visited[next] = True
            elif next < end:
                break

    head = (head + 1) % length

if not find:
    print(-1)
