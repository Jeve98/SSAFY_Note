import sys
sys.stdin = open('algo/input.txt', 'r')

T = int(input())
for tCase in range(T):
    num = int(input())
    dp = [0] * (num + 3)

    dp[0] = dp[1] = dp[2] = 1

    for i in range(3, num):
        dp[i] = dp[i - 2] + dp[i - 3]

    print(dp[num - 1])
