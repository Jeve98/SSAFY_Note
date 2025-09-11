# -- n-queen 2차원 배열 --
def check(row, col):
    # 동일한 col 위치 확인
    for i in range(row):
        if visited[i][col]:
            return False

    # 좌측 대각선 확인 - while
    # i = row - 1
    # j = col - 1
    # while i >= 0 and j >= 0:
    #     if visited[i][j]:
    #         return False
    #
    #     i -= 1
    #     j -= 1

    # 좌측 대각선 확인 - for
    for i in range(1, min(row, col) + 1):
        if visited[row - i][col - i]:
            return False

    # 우측 대각선 확인
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if visited[i][j]:
            return False

        i -= 1
        j += 1

    return True


def n_queen(row, count):
    global ans

    if row == n:
        print(path)
        # 최대 배치된 개수
        if count > ans:
            ans = count
        # ans += 1      # 가능한 경우의 수
        return

    for col in range(n):
        if check(row, col):
            path.append(col)

            visited[row][col] = True
            n_queen(row + 1, count + 1)
            visited[row][col] = False

            path.pop()


n = 4
ans = 0

path = []
visited = [[False] * n for _ in range(n)]
n_queen(0, 0)
print(ans)
print()


# -- n-queen 1차원 배열 -- (실습 코드 확인)
