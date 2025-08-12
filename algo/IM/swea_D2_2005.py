T = int(input())
for case in range(T):
    size = int(input())

    previousStack = []
    nowStack = []

    print(f'#{case + 1}')
    print(1)
    for i in range(size - 1):
        # 첫 값은 항상 1
        print(1, end=' ')
        nowStack.append(1)

        top = len(previousStack) - 1
        while True:
            if top <= 0:
                print(1)
                nowStack.append(1)
                previousStack = nowStack
                nowStack = []
                break

            poping = previousStack[top]
            peek = previousStack[top - 1]
            top -= 1

            print(poping + peek, end=' ')
            nowStack.append(poping + peek)
