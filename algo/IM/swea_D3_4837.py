T = int(input())
A = [i for i in range(1, 13)]
for case in range(T):
    data = list(map(int, input().split()))  # [0] : length, [1] : sum

    ans = 0
    for i in range(1 << 12):    # A집합의 크기는 12
        # length 개 짜리 부분 배열이 아니면 계산 X
        count = 0
        tmp = bin(i)
        tmp = str(tmp)
        for test in tmp:
            if test == '1':
                count += 1
        if not count == data[0]:
            continue

        tmpSum = 0
        for j in range(12):
            if i & (1 << j):
                tmpSum += A[j]

        if tmpSum == data[1]:
            ans += 1

    print(f'#{case + 1} {ans}')