# in coming
icp = {
    '*': 2,
    '+': 1,
       }
# in stack
isp = {
    '*': 2,
    '+': 1,
}

for case in range(10):
    length = int(input())
    cal = input()

    stack = [0] * len(cal)
    top = -1
    postCal = []
    for i in cal:
        if i not in '+*':
            postCal.append(int(i))
        else:
            # stack이 비었거나 입력 부호가 기입력된 부호의 top 보다 우선순위가 높은 경우
            if top == -1 or icp[i] > isp[stack[top]]:
                top += 1
                stack[top] = i
            # stack이 비지 않았고 입력 부호가 기입력된 부호의 top 보다 우선순위가 낮은 경우
            else:
                # stack이 비었거나 입력 부호가 기입력된 부호의 top 보다 우선순위가 높아질 때까지 반복
                while top != -1 and icp[i] > isp[stack[top]]:
                    postCal.append(stack[top])
                    top -= 1
                stack[top] = i

    while top != -1:
        postCal.append(stack[top])
        top -= 1

    stack = [0] * len(postCal)
    top = -1
    for i in postCal:
        if i != '+' or i != '*':
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
                elif i == '*':
                    tmp = lOperate * rOperate
                    top += 1
                    stack[top] = tmp

    print(f'#{case + 1} {stack[top]}')