# import sys
# sys.stdin = open('../input.txt', 'r')


def permutation(now):
    if now == 6:
        makeNum()
        return

    for i in range(4):
        participate[now] = [di[i], dj[i]]
        permutation(now + 1)


def makeNum():
    global ans

    for i in range(4):
        for j in range(4):
            pos = [i, j]

            tmp = [board[i][j]]
            for p in range(6):
                ni = pos[0] + participate[p][0]
                nj = pos[1] + participate[p][1]

                if 0 <= ni < 4 and 0 <= nj < 4:
                    tmp.append(board[ni][nj])
                    pos[0] = ni
                    pos[1] = nj
                else:
                    break
            else:
                tmp = ''.join(tmp)
                ans.add(tmp)


T = int(input())
for case in range(T):
    board = [0] * 4
    for i in range(4):
        oneLine = list(map(str, input().split()))
        board[i] = oneLine

    # 상하좌우 > 6자리 중복 순열
    # 이후 board의 모든 요소에서 생성된 중복 순열에 따라 문자열 생성
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    ans = set()
    participate = [0] * 6
    permutation(0)

    print(f'#{case + 1} {len(ans)}')
