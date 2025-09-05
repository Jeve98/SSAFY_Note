num = int(input())
for case in range(num):
    oneLine = input()

    stack = [0] * len(oneLine)
    top = -1
    for i in range(len(oneLine)):
        if oneLine[i] == '(':
            top += 1
            stack[top] = oneLine[i]
        else:
            if stack[top] != '(':
                print('NO')
                break
            top -= 1
    else:
        if top == -1:
            print('YES')
        else:
            print('NO')
