import sys
sys.stdin = open('../input.txt', 'r')

T = int(input())
for case in range(T):
    size, sculp = map(int, input().split())

    board = [0] * size
    for i in range(size):
        oneLine = list(map(int, input().split()))
        board[i] = oneLine

