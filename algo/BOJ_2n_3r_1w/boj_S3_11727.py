# import sys
# sys.stdin = open('../input.txt', 'r')

size = int(input())

if size == 1:
    print(1)
elif size == 2:
    print(3)
elif size == 3:
    print(5)
else:
    dp = [0] * size

    dp[0] = 1   # 1개
    dp[1] = 3   # 2 (2*2, 2*1), dp[0] + 1*2
    dp[2] = 5   # dp[0] * 2 (2*2, 2*1), dp[1] + 1*2

    for i in range(3, size):
        dp[i] = dp[i - 2] * 2 + dp[i - 1]

    print(dp[size - 1] % 10007)
