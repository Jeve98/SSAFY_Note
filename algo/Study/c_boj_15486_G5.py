# import sys
# sys.stdin = open("algo/input.txt", "r")

days = int(input())

reservation = [0] * days
for i in range(days):
    reservation[i] = list(map(int, input().split()))

dp = [0] * days
for i in range(days - 1, -1, -1):
    if reservation[i][0] + i > days:
        dp[i] = max(dp)
    else:
        if reservation[i][0] + i == days:
            move = i
        else:
            move = reservation[i][0] + i

        dp[i] = reservation[i][1] + dp[move]

        for j in range(1, reservation[i][0]):
            dp[i] = max(dp[i], dp[i + j])

# print(dp)
print(dp[0])
