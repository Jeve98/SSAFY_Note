import sys
sys.stdin = open('../input.txt', 'r')


# sys.setrecursionlimit(3000)
# def DFS(nowPos, num):
#     for addI, addJ in zip(di, dj):
#         ni = nowPos[0] + addI
#         nj = nowPos[1] + addJ
#
#         if 0 <= ni < height and 0 <= nj < width and island[ni][nj] == 1 and visited[ni][nj] == 0:
#             visited[ni][nj] = num
#             DFS([ni, nj], num)


while True:
    width, height = map(int, input().split())

    if width == height == 0:
        break

    island = [0] * height
    for i in range(height):
        oneLine = list(map(int, input().split()))
        island[i] = oneLine

    # delta (상하좌우좌상우상좌하우하)
    di = [-1, 1, 0, 0, -1, -1, 1, 1]
    dj = [0, 0, -1, 1, -1, 1, -1, 1]
    di_a = []
    dj_a = []

    visited = [[0] * width for _ in range(height)]

    # DFS
    # count = 1
    # ans = set()
    # for i in range(height):
    #     for j in range(width):
    #         if visited[i][j] == 0 and island[i][j] == 1:
    #             visited[i][j] = count
    #             ans.add(count)
    #             DFS([i, j], count)
    #             count += 1
    #
    # print(len(ans))
