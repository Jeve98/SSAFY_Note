T = int(input())

for i in range(T):
    N = int(input())
    num = list(map(int, input().split()))

    maxNum = num[0]
    minNum = num[0]
    for index in range(1, N):
        if maxNum <= num[index]:
            maxNum = num[index]
        if minNum >= num[index]:
            minNum = num[index]

    print(f'#{i+1} {maxNum - minNum}')