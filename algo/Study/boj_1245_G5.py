import sys
sys.stdin = open('algo/input.txt', 'r')

row, col = map(int, input().split())

board = [0] * row
for i in range(row):
    board[row] = list(map(int, input().split()))

queue = [0] * (row * col + 1)
head = 0
rear = 0
length = len(queue)

# delta
di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

