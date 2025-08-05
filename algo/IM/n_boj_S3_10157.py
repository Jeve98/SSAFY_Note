# C R - map size
# k - target person

row, column = map(int, input().split())
target = int(input())

# 감소폭은 처음 1회를 제외하고 2회마다 1씩 감소한다.
# ex) column > row - 1 > column - 1 > row - 2 > column - 2 > ... >
