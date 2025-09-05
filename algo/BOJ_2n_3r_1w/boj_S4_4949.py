while True:
    oneLine = input()
    if len(oneLine) == 1:
        break

    stack = [0] * len(oneLine)
    top = -1
    for i in range(len(oneLine)):
        if oneLine[i] == '(' or oneLine[i] == '[':
            top += 1
            stack[top] = oneLine[i]
        elif oneLine[i] == ')':
            if stack[top] != '(':
                print('no')
                break
            top -= 1
        elif oneLine[i] == ']':
            if stack[top] != '[':
                print('no')
                break
            top -= 1
    else:
        if top == -1:
            print('yes')
        else:
            print('no')
