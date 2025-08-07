# # input with list comprehension
# # 1 2
# # 3 4
# ls = []
# for i in range(2):
#     ls.append(list(map(int, input().split())))
# print(ls)
# # [[1, 2], [3, 4]]
#
# ls = [list(map(int, input().split())) for _ in range(2)]
# print(ls)
# # [[1, 2], [3, 4]]
#
# ls = [list(map(int, input().split())) * 2]
# print(ls)
# # [[1, 2, 1, 2]]

# 얕은 복사로 인해 오염되는 2차원 배열
ls = [[0] * 4] * 3
ls[0][0] = 10
print(ls)

ls = [[0] * 4 for _ in range(3)]
ls[0][0] = 10
print(ls)

# 배열 순회
ls = [[1,2,3], [4,5,6], [7,8,9]]

# 행 우선 순회
for i in range(len(ls)):
    for j in range(len(ls[i])):
        print(ls[i][j], end=' ')
    print()
print()

# 열 우선 순회 (모든 행의 길이가 같은 경우)
for j in range(len(ls[0])):
    for i in range(len(ls)):
        print(ls[i][j], end=' ')
    print()
print()
# (zip 사용)
ls2 = list(zip(*ls))
for i in range(len(ls2)):
    for j in range(len(ls2[i])):
        print(ls2[i][j], end=' ')
    print()
print()

# 지그재그 순회
for i in range(len(ls)):
    for j in range(len(ls[i])):
        # i가 짝수일 때, 정탐색
        # j = 0 > 2, j = 1 > 1, j = 2 > 0 (len - j - 1)
        print(ls[i][j + (len(ls[i]) - 2 * j - 1) * (i % 2)], end=' ')
    print()
print()

# 부분 배열 순회
ls = [[i + j * 10 for i in range(10)] for j in range(1, 11)]
for caseR in range(8):
    for caseC in range(8):
        for i in range(caseR, caseR + 3):
            for j in range(caseC, caseC + 3):
                print(ls[i][j], end=' ')
            print()
        print()

# 델타 탐색
# 방향별 더할 값
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(4, 7):
    for j in range(3, 6):
        for addI, addJ in zip(di, dj):
            # 유효 인덱스 확인 필요
            print(ls[i+addI][j+addJ], end=' ')
        print('|', end=' ')
    print()

# 전치 행렬
ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    for j in range(i):
        ls[i][j], ls[j][i] = ls[j][i], ls[i][j]
print(ls)
# zip
ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ls2 = list(zip(*ls))
print(ls2)

# 단일 for문 대각선 원소 접근
for i in range(3):
    print(ls[i][i], end=' ')
print()
for i in range(3):
    print(ls[i][3 - i - 1], end=' ')
print()


# practice problem0 (347, 531, 90)
# T = int(input())
# for i in range(T):
#     size = int(input())
#     arr = []
#     for j in range(size):
#         oneLine = list(map(int, input().split()))
#         arr.append(oneLine)
#     # delta
#     di = [-1, 1, -1, 1]
#     dj = [-1, -1, 1, 1]
#     middle = size // 2
#     sumEl = arr[middle][middle]
#     for count in range(1, 3):
#         for addi, addj in zip(di, dj):
#             sumEl += arr[middle + addi * count][middle + addj * count]
#     print(sumEl)
#     # 단일 for문 대각선 원소 접근 (짝수 길이일 경우, 중심 2회 계산이 없음)
#     sumEl = 0
#     for index in range(size):
#         sumEl += arr[index][index]
#         sumEl += arr[index][size - index - 1]
#     sumEl -= arr[size // 2][size // 2]
#     print(sumEl)


# practice problem1
# T = int(input())
# for i in range(T):
#     size = int(input())
#     arr = []
#     for j in range(size):
#         oneLine = list(map(int, input().split()))
#         arr.append(oneLine)
#
#     di = [0, 0, -1, 1]
#     dj = [-1, 1, 0, 0]
#     for row in range(size):
#         for col in range(size):
#             sumEl = 0
#             for addi, addj in zip(di, dj):
#                 if not (row+addi < 0 or row+addi >= size) and not (col+addj < 0 or col+addj >= size):
#                     sumEl += abs(arr[row][col] - arr[row+addi][col+addj])
#             print(sumEl)
