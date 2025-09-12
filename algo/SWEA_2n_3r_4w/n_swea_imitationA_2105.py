import sys
sys.stdin = open('../input.txt', 'r')

T = int(input())
for case in range(T):
    size = int(input())

    board = [0] * size
    for i in range(size):
        board[i] = list(map(int, input().split()))
