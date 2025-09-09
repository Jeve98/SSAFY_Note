cardCount = int(input())
card = list(map(int, input().split()))
card.sort()

findCount = int(input())
find = list(map(int, input().split()))

for i in range(findCount):
    l = 0
    r = len(card)
    while l < r:
        mid = (l + r) // 2

        if card[mid] >= find[i]:
            r = mid
        else:
            l = mid + 1
    lower = r

    l = 0
    r = len(card)
    while l < r:
        mid = (l + r) // 2

        if card[mid] > find[i]:
            r = mid
        else:
            l = mid + 1
    upper = r

    print(upper - lower, end=' ')
