# 후위표기법 변환
# in coming
icp = {
    '(': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
       }
# in stack
isp = {
    '(': 0,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
}

# (6+5*(2-8)/2)
# cal = input()
cal = '(6+5*(2-8)/2)'
stack = [0] * len(cal)
top = -1

postFix = []
for i in cal:
    if i not in '(*/+-)':
        postFix.append(i)
    # 여는 괄호까지 pop
    elif i == ')':
        while stack[top] != '(' and top > -1:
            postFix.append(stack[top])
            top -= 1
        # 여는 괄호 제거
        if top != -1:
            top -= 1
    else:
        if top == -1 or isp[stack[top]] < icp[i]:
            top += 1
            stack[top] = i
        elif isp[stack[top]] >= icp[i]:
            while top > -1 and isp[stack[top]] >= icp[i]:
                postFix.append(stack[top])
                top -= 1
            top += 1
            stack[top] = i

print(postFix)


# 후위표기법 계산
stack = [0] * len(postFix)
top = -1
for i in postFix:
    if i not in '*/+-':
        top += 1
        stack[top] = i
    elif top >= 1:
        second = int(stack[top])
        first = int(stack[top - 1])
        top -= 2
        if i == '+':
            tmp = first + second
            top += 1
            stack[top] = tmp
        elif i == '-':
            tmp = first - second
            top += 1
            stack[top] = tmp
        elif i == '*':
            tmp = first * second
            top += 1
            stack[top] = tmp
        else:
            tmp = first / second
            top += 1
            stack[top] = tmp
    else:
        print('error')
print(stack[top])
