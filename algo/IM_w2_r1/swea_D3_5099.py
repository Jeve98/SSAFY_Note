def add_pizza(now):
    global count
    global ovenCount

    oven[now][0] = pizza.pop(0)
    oven[now][1] = count
    count += 1
    ovenCount += 1


T = int(input())
for case in range(T):
    ovenSize, pizzaCount = map(int, input().split())
    pizza = list(map(int, input().split()))

    oven = [[0] * 2 for _ in range(ovenSize)]

    ovenCount = 0
    now = 0
    count = 1

    ans = 0
    while pizzaCount != 0:
        # 처음 빈 화덕에 피자 추가
        if pizza and ovenCount < ovenSize:
            add_pizza(now)
            now = (now + 1) % ovenSize
        else:
            for i in range(ovenSize):
                oven[i][0] //= 2

                # 치즈가 다 녹은 경우, 해당 번호에 새로운 피자를 추가
                if oven[i][0] == 0:
                    pizzaCount -= 1
                    ovenCount -= 1
                    now = i
                    # 피자가 남아있을 경우, 피자 추가
                    if pizza:
                        add_pizza(now)
                    # 피자가 남아있지 않을 경우, 해당 칸을 빈칸으로 두기 위해 임의의 숫자 추가
                    else:
                        oven[i][0] = 2 ** 21

                    # 모든 피자가 완성된 경우
                    if pizzaCount == 0:
                        ans = oven[i][1]
                        break

    print(f'#{case + 1} {ans}')
