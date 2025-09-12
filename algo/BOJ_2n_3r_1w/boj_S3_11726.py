n = int(input())

dp = [0] * (n + 3)
dp[1] = 1
dp[2] = 2   # [1]에서 1*2 오른쪽 확장 + [0]에서 2*1 오른쪽 확장
dp[3] = 3   # [2]에서 1*2 오른쪽 확장 + [1]에서 2*1 오른쪽 확장
# dp[i] = dp[i-1] + dp[i-2]

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)
