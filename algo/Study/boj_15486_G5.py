# import sys
# sys.stdin = open('algo/input.txt', 'r')

days = int(input())

reservation = [0] * days
for i in range(days):
    reservation[i] = list(map(int, input().split()))

dp = [0] * days
for i in range(days - 1, -1, -1):
    if reservation[i][0] + i >= days:
        dp[i] = 0
    else:
        temp = dp[i][1] + dp[i + reservation[i][0]]
        for j in range(1, i + 1):
            dp[i] = max(temp, dp[i + j])

print(dp[0])
