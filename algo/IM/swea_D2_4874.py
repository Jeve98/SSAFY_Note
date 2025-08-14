T = int(input())
for case in range(T):
    cal = list(input().split())
    stack = [0] * len(cal)
    top = -1

    for i in cal:
        # 계산 종료
        if i == '.':
            if top == 0:
                print(f'#{case + 1} {stack[top]}')
            # 아직 계산해야 할 피연산자가 남은 경우
            else:
                print(f'#{case + 1} error')
        # 피연산자
        elif i not in '+-*/':
            top += 1
            stack[top] = int(i)
        # 연산자
        else:
            # 피연산자 2개 이상
            if top >= 1:
                rOperate = stack[top]
                lOperate = stack[top - 1]
                top -= 2
                if i == '+':
                    tmp = lOperate + rOperate
                    top += 1
                    stack[top] = tmp
                elif i == '-':
                    tmp = lOperate - rOperate
                    top += 1
                    stack[top] = tmp
                elif i == '*':
                    tmp = lOperate * rOperate
                    top += 1
                    stack[top] = tmp
                else:
                    tmp = lOperate // rOperate
                    top += 1
                    stack[top] = tmp
            # 피연산자 2개 미만
            else:
                print(f'#{case + 1} error')
                break
