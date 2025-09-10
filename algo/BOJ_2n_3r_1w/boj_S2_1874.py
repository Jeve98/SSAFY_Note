# import sys
# sys.stdin = open('../input.txt', 'r')

instruction = int(input())

stack = [0] * (instruction + 1)
top = -1

previous = 0
ans = []
for i in range(instruction):
    num = int(input())

    if top == -1 or previous < num:
        for i in range(previous + 1, num + 1):
            top += 1
            stack[top] = i
            ans.append('+')

        top -= 1
        ans.append('-')
        previous = num
    elif previous > num:
        if stack[top] == num:
            top -= 1
            ans.append('-')
        else:
            print('NO')
            break
else:
    for i in range(len(ans)):
        print(ans[i])
