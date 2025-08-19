T = int(input())
for case in range(T):
    oneLine = input()

    stack = [0] * len(oneLine)
    top = -1
    for i in oneLine:
        if i in ['(', '{']:
            top += 1
            stack[top] = i
        elif i in [')', '}']:
            if top >= 0:
                # 유니코드값 비교
                # ( <-> ) : 1 차이
                # { <-> } : 2 차이
                # [ <-> ] : 2 차이
                code = abs(ord(stack[top]) - ord(i))
                if code <= 2:
                    top -= 1
                else:
                    print(f'#{case + 1} 0')
                    break
            else:
                print(f'#{case + 1} 0')
                break
    else:
        if top == -1:
            print(f'#{case + 1} 1')
        else:
            print(f'#{case + 1} 0')
