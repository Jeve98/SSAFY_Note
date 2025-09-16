# import sys
# sys.stdin = open('../input.txt', 'r')
from heapq import heappush as hpush, heappop as hpop


def dijkstra(startPos):
    primaryQ = [(0, startPos)]

    distance = [[100000000] * size for _ in range(size)]
    distance[startPos[0]][startPos[1]] = 0

    # delta
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while primaryQ:
        nowDis, nowPos = hpop(primaryQ)

        if distance[nowPos[0]][nowPos[1]] < nowDis:
            continue

        for addI, addJ in zip(di, dj):
            ni = nowPos[0] + addI
            nj = nowPos[1] + addJ

            if 0 <= ni < size and 0 <= nj < size:
                newDis = nowDis + 1
                if board[ni][nj] > board[nowPos[0]][nowPos[1]]:
                    newDis += (board[ni][nj] - board[nowPos[0]][nowPos[1]])

                if distance[ni][nj] <= newDis:
                    continue

                distance[ni][nj] = newDis
                hpush(primaryQ, (newDis, [ni, nj]))

    return distance


T = int(input())
for case in range(T):
    size = int(input())

    board = [0] * size
    for i in range(size):
        board[i] = list(map(int, input().split()))

    result = dijkstra((0, 0))
    print(f'#{case + 1} {result[size - 1][size - 1]}')
