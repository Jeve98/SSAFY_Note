size = int(input())
room = [[] for _ in range(size)]
# always start in (0,1) : important is head position, because tail can follow head's route
for i in range(size):
    oneLine = list(map(int, input().split()))   # [0]: empty, [1]: wall
    room[i] = oneLine

# 우 하 대각
di = [0, 1, 1]
dj = [1, 0, 1]


# 시간 초과
# def dfs(now, status):
#     global count
#
#     if now == [size - 1, size - 1]:
#         count += 1
#         return
#
#     # 가로일 경우, 가능한 이동 방향은 가로, 대각선
#     if status == 0:
#         for i in range(status, 3, 2):
#             ni = now[0] + di[i]
#             nj = now[1] + dj[i]
#             if validation(ni, nj, i):
#                 dfs([ni, nj], i)
#     # 세로일 경우, 가능한 이동 방향은 세로, 대각선
#     elif status == 1:
#         for i in range(status, 3):
#             ni = now[0] + di[i]
#             nj = now[1] + dj[i]
#             if validation(ni, nj, i):
#                 dfs([ni, nj], i)
#     # 대각선일 경우, 가능한 이동 방향은 전부
#     else:
#         for i in range(3):
#             ni = now[0] + di[i]
#             nj = now[1] + dj[i]
#             if validation(ni, nj, i):
#                 dfs([ni, nj], i)
#
#
# def validation(ni, nj, status):
#     # 우 하
#     if ni < size and nj < size and status < 2 and room[ni][nj] == 0:
#          return True
#     # 대각
#     elif ni < size and nj < size and status == 2 and room[ni][nj] == 0 and room[ni - 1][nj] == 0 and room[ni][nj - 1] == 0:
#          return True
#     else:
#         return False
#
#
# count = 0
# # 0: 가로, 1: 세로, 2: 대각선
# dfs([0, 1], 0)
# print(count)
