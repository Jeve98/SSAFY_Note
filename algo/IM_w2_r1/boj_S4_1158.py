people, out = map(int, input().split())

queue = [0] * (people + 1)
head = 0
rear = 0

for i in range(1, people + 1):
    queue[rear] = i
    rear = (rear + 1) % len(queue)

for i in range(out - 1):
    now = queue[head]
    head = (head + 1) % len(queue)
    queue[rear] = now
    rear = (rear + 1) % len(queue)
print(f'<{queue[head]}', end='')
head = (head + 1) % len(queue)

while head != rear:
    for i in range(out - 1):
        now = queue[head]
        head = (head + 1) % len(queue)
        queue[rear] = now
        rear = (rear + 1) % len(queue)

    print(f', {queue[head]}', end='')
    head = (head + 1) % len(queue)

print('>')
