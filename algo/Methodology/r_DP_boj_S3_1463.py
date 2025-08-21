# boj 1463
"""
n = 1,  ans = 0
n = 2,  ans = 1 (/2)
n = 3,  ans = 1 (/3)
n = 4,  ans = 2 (/2 + n=2의 횟수)
n = 5,  ans = 3 (-1 + n=4의 횟수)
n = 6,  ans = 2 (/3 + n=2의 횟수)
n = 7,  ans = 3 (-1 + n=6의 횟수)

2, 3으로 나누어 떨어진다면, 연산 횟수 1회(/2 or /3) + 나누어진 값의 연산 횟수 n회
2, 3으로 나누어 떨어지지 않는다면, 연산 횟수 1회(-1) + 뺀 값의 연산 횟수 n회
"""
num = int(input())

# 하향식 : Memoization - recursive
# 높은 확률로 recursion error를 마주하므로 sys 모듈을 통해 recursion 깊이를 늘려야함
# import sys
# sys.setrecursionlimit(10**6)


# def decomposition(num):
#     # memoization 해둔 값이 있는 경우 (계산이 완료된 값)
#     if memoization[num] != 0 or num == 1:
#         return memoization[num]
#     # memoization 해둔 값이 없는 경우 (새로운 값)
#     else:
#         modify2 = 100000
#         modify3 = 100000
#
#         if num % 2 == 0:
#             modify2 = decomposition(num // 2)
#
#         if num % 3 == 0:
#             modify3 = decomposition(num // 3)
#
#         minus = decomposition(num - 1)
#
#         memoization[num] = min(modify2, modify3, minus) + 1
#
#         return memoization[num]
#
#
# memoization = [0] * (num + 1)
# memoization[1] = 0
# print(decomposition(num))

# 상향식 : Tabulation - 반복문
tabulation = [0] * (num + 1 + 2)
tabulation[0] = 0
tabulation[1] = 0
tabulation[2] = 1
tabulation[3] = 1

for i in range(4, num + 1):
    modify2 = 100000
    modify3 = 100000
    minus = tabulation[i - 1] + 1

    if i % 2 == 0:
        modify2 = tabulation[i // 2] + 1

    if i % 3 == 0:
        modify3 = tabulation[i // 3] + 1

    tabulation[i] = min(modify2, modify3, minus)

print(tabulation[num])

# tabulation 리팩토링
tabulation = [0] * (num + 1)
tabulation[1] = 0

for i in range(2, num + 1):
    tabulation[i] = tabulation[i - 1] + 1

    if i % 2 == 0:
        tabulation[i] = min(tabulation[i], tabulation[i // 2] + 1)

    if i % 3 == 0:
        tabulation[i] = min(tabulation[i], tabulation[i // 3] + 1)

print(tabulation[num])
