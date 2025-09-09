# import sys
# sys.stdin = open('../input.txt', 'r')

instruction = int(input())

stack = [0] * instruction
top = -1

for i in range(instruction):
    oneLine = input().split()
    if oneLine[0] == 'push':
        top += 1
        stack[top] = oneLine[1]
    elif oneLine[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif oneLine[0] == 'size':
        print(top + 1)
    elif oneLine[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif oneLine[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
