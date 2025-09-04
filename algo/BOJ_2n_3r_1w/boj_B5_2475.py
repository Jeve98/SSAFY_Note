numbers = list(map(int, input().split()))

tmpSum = 0
for i in range(len(numbers)):
    tmpSum += numbers[i] ** 2

ans = tmpSum % 10
print(ans)
