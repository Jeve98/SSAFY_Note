dls = [[] for _ in range(10)]
print(dls)

# Debugging Start
# shift F9
arr = [1, 2, 3]
txt = 'test'
print(txt, arr)

# Debugging one line
# F8
arr = [2, 3, 4]

# Practice0
# T = int(input())    # test case
T = 1
# N = int(input())    # number count by case
N =5

for i in range(T):
    # ls = []
    # for j in range(N):
    #     ls = list(map(int, input().split()))
    ls = [1, 10, 100, 1000, 10000]

    maxNum = ls[0]
    minNum = ls[0]

    for index in range(N):
        # max
        if maxNum <= ls[index]:
            maxNum = ls[index]

        # min
        if minNum >= ls[index]:
            minNum = ls[index]

    print(f'#{i} max: {maxNum}, min: {minNum}')


# Practice1
"""
9
[7, 4, 2, 0, 0, 6, 0, 7, 0]
=> 7
9
[4, 2, 0, 0, 7, 6, 0, 7, 0]
=> 5
"""
# N = int(input())
N = 9
# boxes = list(map(int, input().split()))
boxes = [7, 4, 2, 0, 0, 6, 0, 7, 0]
index = len(boxes) - 1
maxFall = 0
# 마지막 박스는 확인할 필요가 없음
for i in range(1, len(boxes)):
    # 역순 확인
    boxLine = [0] * boxes[index - i]
    # 이후 박스 확인
    count = 0
    for j in range(index - i + 1, index + 1):
        count = boxes[index - i] - boxes[j]
        if count <= 0:
            continue

        for add in range(len(boxLine) - 1, len(boxLine) - count - 1, -1):
            boxLine[add] += 1

    for j in range(len(boxLine)):
        if maxFall <= boxLine[j]:
            maxFall = boxLine[j]

print(maxFall)


# Bubble Sort
ls = [3, 12, 1, 136, 13, 436]
count = len(ls)
for i in range(count-1, 0, -1):
    for j in range(i):
        if ls[j] >= ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]

print(ls)


# Counting Sort
ls = [0, 4, 1, 3, 1, 2, 4, 1]
count = [0] * (max(ls) + 1)
length = len(ls)
for i in range(length):
    count[ls[i]] += 1

for i in range(1, len(count)):
    count[i] += count[i-1]

ans = [0] * length
for i in range(length):
    count[ls[i]] -= 1
    ans[count[ls[i]]] = ls[i]

print(ans)


# swea0
# T = int(input())
# for i in range(T):
#     data = list(map(int, input().split()))  # [0] : number count, [1] : area
#     num = list(map(int, input().split()))
#
#     maxSum = 0
#     minSum = 1000000
#     for index in range(data[0] - data[1] + 1):
#         tempSum = 0
#         for sumCount in range(data[1]):
#             tempSum += num[index + sumCount]
#
#         if maxSum <= tempSum:
#             maxSum = tempSum
#         if minSum >= tempSum:
#             minSum = tempSum
#
#     print(f'#{i+1} {maxSum-minSum}')


# swea1
# T = int(input())
#
# for i in range(T):
#     N = int(input())
#     num = list(map(int, input().split()))
#
#     maxNum = num[0]
#     minNum = num[1]
#     for index in range(1, N):
#         if maxNum <= num[index]:
#             maxNum = num[index]
#         if minNum >= num[index]:
#             minNum = num[index]
#
#     print(f'#{i+1} {maxNum - minNum}')

# swea2
# 1206
