for case in range(10):
    length = int(input())
    cal = input()

    stack = [0] * len(cal)
    top = -1
    postCal = []
    for i in cal:
        # 연산자가 +로만 한정
        if i != '+':
            postCal.append(int(i))
        else:
            if top == -1:
                top += 1
                stack[top] = i
            else:
                postCal.append(stack[top])
                stack[top] = i

    while top != -1:
        postCal.append(stack[top])
        top -= 1

    stack = [0] * len(postCal)
    top = -1
    for i in postCal:
        if i != '+':
            top += 1
            stack[top] = i
        else:
            if top >= 1:
                rOperate = stack[top]
                lOperate = stack[top - 1]
                top -= 2
                if i == '+':
                    tmp = lOperate + rOperate
                    top += 1
                    stack[top] = tmp

    print(f'#{case + 1} {stack[top]}')
