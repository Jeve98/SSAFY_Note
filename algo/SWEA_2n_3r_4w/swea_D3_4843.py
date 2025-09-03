T = int(input())
for case in range(T):
    count = int(input())
    numbers = list(map(int, input().split()))

    up = numbers[:]
    down = numbers[:]
    upIndex = 0
    downIndex = 0
    for i in range(count - 1):
        upIndex = i
        downIndex = i
        for j in range(i, count):
            # 오름차순
            if up[upIndex] > up[j]:
                upIndex = j
            # 내림차순
            if down[downIndex] < down[j]:
                downIndex = j

        up[i], up[upIndex] = up[upIndex], up[i]
        down[i], down[downIndex] = down[downIndex], down[i]

    ans = []
    for i in range(count // 2):
        ans.append(down[i])
        ans.append(up[i])

    print(f'#{case + 1}', end=' ')
    for i in range(10):
        print(ans[i], end=' ')
    print()