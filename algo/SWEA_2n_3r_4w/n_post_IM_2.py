"""
공 굴리기

N*N 배열에서 각 칸의 높이가 주어진다.
공은 높은 곳에서 낮은 곳으로 굴러가는데, 정확히는 상하좌우의 값 중에서 최솟값인 곳으로 떨어진다.
만약 상하좌우보다 본인의 높이가 낮다면 더 이상 움직이지 않는다.
상하좌우의 높이가 같은 경우는 주어지지 않는다.
공은 N*N 배열의 경계를 벗어나지는 않는다.
공이 가장 길게 굴러갔을 때, 공이 지나가는 최대의 칸의 수를 구하시오.

입력
TC - test case
N
N*N 배열의 높이가 N줄에 걸쳐 주어짐 (자연수)

-ex-
(입력)
3
3
1 2 3
4 5 6
7 8 9
4
70 42 47 32
11 1 3 59
75 90 5 81
84 42 11 59
4
70 42 47 32
11 97 37 59
75 90 5 81
84 42 11 59

(출력)
#1 5
#2 6
#3 4
"""

T = int(input())
for case in range(T):
    size = int(input())

    table = []
    for i in range(size):
        oneLine = list(map(int, input().split()))
        table.append(oneLine)

    # DP

    # # DFS
    # # 상하좌우
    # di = [-1, 1, 0, 0]
    # dj = [0, 0, -1, 1]
    #
    # maxCount = 0
    # for i in range(size):
    #     for j in range(size):
    #         stack = [0] * (size ** 2)
    #         top = 0
    #         stack[top] = (i, j)
    #
    #         tmpMin = table[stack[top][0]][stack[top][1]]
    #         while top != -1:
    #             index = []
    #             for addI, addJ in zip(di, dj):
    #                 ni = stack[top][0] + addI
    #                 nj = stack[top][1] + addJ
    #
    #                 if 0 <= ni < size and 0 <= nj < size and tmpMin > table[ni][nj]:
    #                     tmpMin = table[ni][nj]
    #                     index = [ni, nj]
    #
    #             if index:
    #                 top += 1
    #                 stack[top] = (index[0], index[1])
    #             else:
    #                 break
    #
    #         if maxCount < top + 1:
    #             maxCount = top + 1
    #
    # print(f'#{case + 1} {maxCount}')
