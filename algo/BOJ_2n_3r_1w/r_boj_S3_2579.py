# import sys
# sys.stdin = open('../input.txt', 'r')

# subset - 시간초과
# def subset(now, total, seq):
#     global ans
#
#     if now == stairC - 1:
#         if seq <= 1:
#             total += stair[now]
#         else:
#             return
#
#         if total > ans:
#             ans = total
#         return
#
#     if seq >= 3:
#         return
#
#     for i in [True, False]:
#         if i:
#             subset(now + 1, total + stair[now], seq + 1)
#         else:
#             subset(now + 1, total, 0)
#
#
# stairC = int(input())
#
# stair = [0] * stairC
# for i in range(stairC):
#     stair[i] = int(input())
#
# ans = 0
# subset(0, 0, 0)
# print(ans)

# DP
stairC = int(input())

stair = [0] * stairC
for i in range(stairC):
    stair[i] = int(input())

if stairC == 1:
    print(stair[0])
elif stairC == 2:
    print(stair[0] + stair[1])
else:
    dp = [0] * stairC
    dp[0] = stair[0]
    dp[1] = dp[0] + stair[1]
    dp[2] = max(dp[0] + stair[2], stair[1] + stair[2])

    for i in range(3, stairC):
        # dp[i - 3] + stair[i - 1] + stair[i]
        # dp[i - 1]로 식을 구성할 경우, dp[i - 1]의 값이 i - 2번째 계단을 밟지 않았다는 것을 보장할 수 없음
        dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

    print(dp[stairC - 1])
