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
def check(row):
    for prev_row in range(row):
        # 세로 체크
        if visited[row] == visited[prev_row]:
            return False

        # 열과 행의 차이가 같다 == 현재 col 의 좌우 대각선이다
        # visited 에 저장된 값 = 어느 col에 두었는 가 ?
        # row - prev_row = 행의 차이
        # visited[row] - visited[prev_row] = 열의 차이
        # 이 두 개가 같으면 대각선
        if abs(row - prev_row) == abs(visited[row] - visited[prev_row]):
            return False

    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        visited[row] = col  # 현재 row 의 col 에 놓았다 라고 가정하고
        if not check(row):  # 세로와 대각선을 체크해준다.
            continue

        dfs(row + 1)

N = 8
visited = [0] * N
cnt = 0

dfs(0)
print(f'N = {N} / answer = {cnt}')