# import sys
# sys.stdin = open('../input.txt', 'r')

T = int(input())
for case in range(T):
    size = int(input())
    board = [0] * size
    start = 0
    end = 0
    for i in range(size):
        board[i] = input()

        for j in range(size):
            if board[i][j] == 'X':
                start = (i, j)
            elif board[i][j] == 'Y':
                end = (i, j)

    controlC = int(input())
    control = [0] * controlC
    for i in range(controlC):
        control[i] = list(input().split())      # [0]: length, [1]: instruction

    # delta - 상우하좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    ans = []
    for each in control:
        now = start
        direction = 0
        for instruction in each[1]:
            if instruction == 'R':
                direction += 1
            elif instruction == 'L':
                direction -= 1
            elif instruction == 'A':
                ni = now[0] + di[direction]
                nj = now[1] + dj[direction]

                if 0 <= ni < size and 0 <= nj < size and board[ni][nj] != 'T':
                    now = (ni, nj)

            if direction >= 4:
                direction = 0
            elif direction < 0:
                direction = 3

        if now == end:
            ans.append(1)
        else:
            ans.append(0)

    print(f'#{case + 1}', end='')
    for i in range(len(ans)):
        print(f' {ans[i]}', end='')
    print()
