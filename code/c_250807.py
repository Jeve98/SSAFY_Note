# bit를 통해 부분 집합 생성
bit = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            bit.append([i * 1, j * 2, k * 3])
print(bit)


# 부분 집합 확인
def subset(bit):
    for i in range(len(bit)):
        if bit[i]:  # bit[i] == 0, 즉 False일 때를 제외하고 작동
            print(arr[i], end=' ')


arr = [4, -1, 25]
subset([1, 1, 0])
print()

# bit 연산자
print(3 & 6)  # 011 & 110 == 010
print(3 | 6)  # 011 | 110 == 111
print(3 << 1)  # 011 << 1칸 == 110
print(13 >> 2)  # 1101 >> 2칸 == 0011

# bit 연산자를 통해 부분 집합 생성
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1 << n):  # range(2^n)
    for j in range(n):  # 원소의 수만큼 비교
        if i & (1 << j):  # i의 j번 비트가 1인 경우
            print(arr[j], end=' ')
    print(f'\ni : {i:b}')
print()

# search
import random

arr = []
for i in range(10):
    arr.append(random.randint(0, 20))

# ? sort
ls = arr[:]
for i in range(len(ls) - 1):
    for j in range(i + 1, len(ls)):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
print(f'? : {ls}')

# selection sort
ls1 = arr[:]
minIndex = 0
for i in range(len(ls1) - 1):
    minIndex = i
    for j in range(i + 1, len(ls1)):
        if ls1[minIndex] > ls1[j]:
            minIndex = j
    ls1[minIndex], ls1[i] = ls1[i], ls1[minIndex]
print(f'selection : {ls1}')

# bubble sort
ls2 = arr[:]
for i in range(len(ls2) - 1, 0, -1):
    for j in range(i):  # len - 1까지 증가해야 j + 1에서 overflow을 방지
        if ls2[j] > ls2[j + 1]:
            ls2[j], ls2[j + 1] = ls2[j + 1], ls2[j]
print(f'bubble : {ls2}')

# binary search
search = arr[0]
arr.sort()
# while
# start = 0
# end = len(arr) - 1
# count = 0
# while start <= end:
#     middle = (start + end) // 2
#     count += 1
#     if arr[middle] > search:
#         end = middle - 1
#     elif arr[middle] < search:
#         start = middle + 1
#     else:
#         print(f'count : {count}, search : {search}, find : {arr[middle]}')
#         break


# 재귀
# def binary_search(start, end, arr, find):
#     middle = (start + end) // 2
#     if arr[middle] > find:
#         return binary_search(start, middle - 1, arr, find)
#     elif arr[middle] < find:
#         return binary_search(middle + 1, end, arr, find)
#     else:
#         return middle
#
#
# ans = binary_search(0, len(arr) - 1, arr, search)
# print(f'search : {search}, ans : {ans}')

# practice problem0
# T = int(input())
#
# for k in range(T):
#     ls = list(map(int, input().split()))
#     n = len(ls)
#
#     for i in range(1, 1 << n):  # 공집합 제외
#         tmpSum = []
#         for j in range(n):
#             if i & (1 << j):
#                 tmpSum.append(ls[j])
#
#         if sum(tmpSum) == 0:
#             print('T')
#             break
#     else:
#         print('F')
