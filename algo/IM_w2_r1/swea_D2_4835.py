T = int(input())
for i in range(T):
    data = list(map(int, input().split()))  # [0] : number count, [1] : area
    num = list(map(int, input().split()))

    maxSum = 0
    minSum = 1000000
    for index in range(data[0] - data[1] + 1):
        tempSum = 0
        for sumCount in range(data[1]):
            tempSum += num[index + sumCount]

        if maxSum <= tempSum:
            maxSum = tempSum
        if minSum >= tempSum:
            minSum = tempSum

    print(f'#{i+1} {maxSum-minSum}')