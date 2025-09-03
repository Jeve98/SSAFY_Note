count = int(input())

dice = []
for i in range(count):
    # A <> F , B <> D, C <> E
    # 0 <(sum5)> 5, 1 <(sum4)> 3, 2 <(sum6)> 4
    oneLine = list(map(int, input().split()))
    dice.append(oneLine)

maxSum = 0
for bottom in range(6):
    if bottom == 0 or bottom == 5:
        partner = 5 - bottom
    elif bottom == 1 or bottom == 3:
        partner = 4 - bottom
    else:
        partner = 6 - bottom

    bottomVal = dice[0][bottom]
    partnerVal = dice[0][partner]
    # 주사위 n개
    side = []
    for now in range(count):
        # 주사위 1개
        tmp = []
        # 설치된 주사위의 옆면 저장
        for i in range(6):
            if dice[now][i] == bottomVal or dice[now][i] == partnerVal:
                continue
            tmp.append(dice[now][i])
        side.append(tmp)

        # 다음 주사위의 bottom, partner 갱신
        bottomVal = partnerVal
        if now < count - 1:
            for i in range(6):
                if dice[now + 1][i] == bottomVal:
                    if i == 0 or i == 5:
                        partnerVal = dice[now + 1][5 - i]
                    elif i == 1 or i == 3:
                        partnerVal = dice[now + 1][4 - i]
                    else:
                        partnerVal = dice[now + 1][6 - i]
                    break

    tmpMaxSum = 0
    for i in range(count):
        tmpMaxSum += max(side[i])

    if maxSum < tmpMaxSum:
        maxSum = tmpMaxSum

print(maxSum)
