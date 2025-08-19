T = int(input())
for case in range(T):
    ingredient, calorie = map(int, input().split())
    ingredients = []
    for i in range(ingredient):
        oneLine = list(map(int, input().split()))   # [0]: score, [1]: each calorie
        ingredients.append(oneLine)

    # 칼로리 순으로 정렬
    ingredients.sort(key=lambda x: x[1])

    maxScore = 0
    pointer = 0
    while pointer < ingredient:
        tmpCalo = 0
        tmpScore = 0
        for i in range(pointer, ingredient):
            if tmpCalo + ingredients[i][1] <= calorie:
                tmpCalo += ingredients[i][1]
                tmpScore += ingredients[i][0]
                # ㅈ댐 knapsack 문제 이렇게 푸는거 아님...