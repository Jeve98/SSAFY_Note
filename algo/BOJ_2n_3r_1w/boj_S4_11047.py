# import sys
# sys.stdin = open('../input.txt', 'r')

coinC, total = map(int, input().split())

coins = [0] * coinC
for i in range(coinC):
    coins[i] = int(input())

# Greedy
count = 0
for i in range(coinC - 1, -1, -1):
    if total >= coins[i]:
        tmp = (total // coins[i])
        total -= (coins[i] * tmp)
        count += tmp

    if total == 0:
        break

print(count)

# DP
# dp = [2100000000] * (total + 1)
# dp[0] = 0
# for coin in coins:
#     for i in range(coin, total + 1):
#         dp[i] = min(dp[i], dp[i - coin] + 1)
#
# print(dp[total])

# BFS - queue를 직접 구현할 경우, overflow가 발생할 가능성이 매우 높음
# length = 100000
# queue = [0] * length
# head = 0
# rear = 0
# visited = set()
#
# queue[rear] = [0, 0]    # [0]: count, [1]: sum
# rear = (rear + 1) % length
#
# while head != rear:
#     now = queue[head]
#     head = (head + 1) % length
#
#     if now[1] == total:
#         print(now[0])
#         break
#
#     for coin in coins:
#         if now[1] + coin <= total and now[1] + coin not in visited:
#             queue[rear] = [now[0] + 1, now[1] + coin]
#             visited.add(now[1] + coin)

# BFS
# from collections import deque
#
# queue = deque()
# queue.append((0, 0))    # [0]: count, [1]: sum
# visited = set()
#
# while queue:
#     count, current = queue.popleft()
#
#     if current == total:
#         print(count)
#         break
#
#     for coin in coins:
#         next_sum = current + coin
#         if next_sum <= total and next_sum not in visited:
#             visited.add(next_sum)
#             queue.append((count + 1, next_sum))
