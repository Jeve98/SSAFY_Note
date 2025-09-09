# import sys
# sys.stdin = open('../input.txt', 'r')

instruction = int(input())

queue = [0] * instruction
head = 0
rear = 0

for i in range(instruction):
    oneLine = input().split()
    if oneLine[0] == 'push':
        queue[rear] = oneLine[1]
        rear = (rear + 1) % instruction
    elif oneLine[0] == 'pop':
        if head == rear:
            print(-1)
        else:
            print(queue[head])
            head = (head + 1) % instruction
    elif oneLine[0] == 'size':
        print(rear - head)
    elif oneLine[0] == 'empty':
        if head == rear:
            print(1)
        else:
            print(0)
    elif oneLine[0] == 'front':
        if head == rear:
            print(-1)
        else:
            print(queue[head])
    elif oneLine[0] == 'back':
        if head == rear:
            print(-1)
        else:
            print(queue[rear - 1])
