def fibo(n):
    if memoization[n][2] != -1:
        return memoization[n]

    if n == 0:
        memoization[0][2] = 0
        memoization[0][0] = 1
        memoization[0][1] = 0
        return memoization[0]
    elif n == 1:
        memoization[1][2] = 1
        memoization[1][0] = 0
        memoization[1][1] = 1
        return memoization[1]
    else:
        memoization[n][2] = fibo(n - 1)[2] + fibo(n - 2)[2]
        memoization[n][0] = fibo(n - 1)[0] + fibo(n - 2)[0]
        memoization[n][1] = fibo(n - 1)[1] + fibo(n - 2)[1]
        return memoization[n]


T = int(input())
for case in range(T):
    n = int(input())

    memoization = [[-1] * 3 for _ in range(41)]     # [0]: 0이 호출된 횟수, [1]: 1이 호출된 횟수, [2]: 값
    fibo(n)

    zero = memoization[n][0]
    one = memoization[n][1]
    print(zero, one)
