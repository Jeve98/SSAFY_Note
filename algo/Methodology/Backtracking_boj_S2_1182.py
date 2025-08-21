"""
backtracking = DFS + pruning
"""

# boj 1182
numCount, targetSum = map(int, input().split())
numbers = list(map(int, input().split()))


# use making subset
# def subset(now):
#     global count
#     if now == numCount:
#         tmpSum = 0
#         # 공집합 제외
#         if sum(make) > 0:
#             for i in range(numCount):
#                 if make[i] != 0:
#                     tmpSum += numbers[i]
#             if tmpSum == targetSum:
#                 count += 1
#     else:
#         make[now] = 1
#         subset(now + 1)
#         make[now] = 0
#         subset(now + 1)
#
#
# make = [0] * numCount
# count = 0
# subset(0)
# print(count)


# use nowSum
def subset(now, nowSum, use):
    global count
    if now == numCount:
        if nowSum == targetSum and use != 0:
            count += 1
    else:
        subset(now + 1, nowSum + numbers[now], use + 1)
        subset(now + 1, nowSum, use)


use = 0
count = 0
subset(0, 0, use)
print(count)
