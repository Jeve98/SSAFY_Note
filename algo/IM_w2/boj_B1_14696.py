# 4 > 3 > 2 > 1순 비교
battle = int(input())

A = []
B = []
ls = [[], []]
for i in range(battle):
    for ab in range(2):
        data = list(map(int, input().split()))  # [0]: cards count, [1:]: card data
        count = [0] * 4
        for card in range(1, data[0] + 1):
            count[data[card] - 1] += 1
        ls[ab].append(count)

for a, b in zip(*ls):
    for i in range(3, -1, -1):
        if a[i] > b[i]:
            print('A')
            break
        elif a[i] < b[i]:
            print('B')
            break
        elif i == 0:
            print('D')
