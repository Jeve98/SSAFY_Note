# import sys
# sys.stdin = open('../input.txt', 'r')


def subset(now, select):
    global ans

    if now == ingredientC:
        if len(select) == ingredientC // 2:
            selectScore = 0
            nonSelectScore = 0

            for i in range(ingredientC):
                for j in range(ingredientC):
                    if i in select and j in select:
                        selectScore += synergy[i][j]
                    elif i not in select and j not in select:
                        nonSelectScore += synergy[i][j]

            tmp = abs(selectScore - nonSelectScore)

            if tmp < ans:
                ans = tmp
        return

    for i in [True, False]:
        if i:
            subset(now + 1, select + [now])
        else:
            subset(now + 1, select)


T = int(input())
for case in range(T):
    ingredientC = int(input())

    synergy = [0] * ingredientC
    for i in range(ingredientC):
        synergy[i] = list(map(int, input().split()))

    ans = 2100000000
    subset(0, [])
    print(f'#{case + 1} {ans}')
