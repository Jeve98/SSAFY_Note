T = int(input())
for case in range(T):
    origin = input()

    stack = [0] * len(origin)
    stack[0] = origin[0]
    top = 0

    for i in range(1, len(origin)):
        if stack[top] == origin[i]:
            top -= 1
        else:
            top += 1
            stack[top] = origin[i]

    print(f'#{case + 1} {top + 1}')
