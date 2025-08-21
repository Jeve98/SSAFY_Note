def choose(now, nowSum, nowScore):
    global maxScore
    if now == ingredient and nowSum <= calorie:
        if nowScore > maxScore:
            maxScore = nowScore
    elif nowSum < calorie:
        choose(now + 1, nowSum + ingredients[now][1], nowScore + ingredients[now][0])
        choose(now + 1, nowSum, nowScore)


T = int(input())
for case in range(T):
    ingredient, calorie = map(int, input().split())
    ingredients = []
    for i in range(ingredient):
        oneLine = list(map(int, input().split()))   # [0]: score, [1]: each calorie
        ingredients.append(oneLine)

    maxScore = 0
    choose(0, 0, 0)

    print(f'#{case + 1} {maxScore}')
