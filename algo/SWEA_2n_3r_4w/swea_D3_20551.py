T = int(input())
for case in range(T):
    candyBox = list(map(int, input().split()))

    eat = 0
    for i in range(len(candyBox) - 2, -1, -1):
        if candyBox[i] >= candyBox[i + 1]:
            tmp = candyBox[i] - candyBox[i + 1] + 1
            eat += tmp
            candyBox[i] -= tmp

            if candyBox[i] <= 0:
                print(f'#{case + 1} -1')
                break
    else:
        print(f'#{case + 1} {eat}')
