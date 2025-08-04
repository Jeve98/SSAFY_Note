n = int(input())
num = list(map(int, input().split()))

upCount = 0
downCount = 0
result = 0
for i in range(n-1):
    # 오름차순 수열
    if num[i] <= num[i+1]:
        upCount += 1
    else:
        upCount = 0

    # 내림차순 수열
    if num[i] >= num[i+1]:
        downCount += 1
    else:
        downCount = 0

    result = max(upCount, downCount, result)

# 본인을 포함하여 출력
print(result+1)
