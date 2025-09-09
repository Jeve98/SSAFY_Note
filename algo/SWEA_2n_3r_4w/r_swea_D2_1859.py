# import sys
# sys.stdin = open('../input.txt', 'r')

# 시간 초과
"""
T = int(input())
for case in range(T):
    days = int(input())

    price = list(map(int, input().split()))
    maxPrice = max(price)
    maxIndex = days

    maxEarn = 0
    count = 1
    for i in range(days - 1):
        if price[i] == price[i + 1]:
            count += 1
        elif price[i] <= price[i + 1]:
            maxEarn += (price[i + 1] - price[i]) * count
            count += 1
        else:
            if price[i] == maxPrice:
                maxIndex = i

            if price[i] < maxPrice and i < maxIndex:
                maxEarn += (maxPrice - price[i]) * count
            count = 1

            maxPrice = max(price[i + 1:])
            maxIndex = days

    print(f'#{case + 1} {maxEarn}')
"""

T = int(input())
for case in range(T):
    days = int(input())
    price = list(map(int, input().split()))

    maxEarn = 0
    base = price[days - 1]
    for i in range(days - 1, -1, -1):
        if base > price[i]:
            maxEarn += (base - price[i])
        elif base < price[i]:
            base = price[i]

    print(f'#{case + 1} {maxEarn}')
