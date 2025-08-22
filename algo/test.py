tunnel = {
        # 상하좌우
        '1': zip([-1, 1, 0, 0], [0, 0, -1, 1]),
        # 상하
        '2': [[-1, 1, 0, 0], [0, 0, 0, 0]],
        # 좌우
        '3': [[0, 0, 0, 0], [0, 0, -1, 1]],
        # 상우
        '4': [[-1, 0, 0, 0], [0, 0, 0, 1]],
        # 하우
        '5': [[0, 1, 0, 0], [0, 0, 0, 1]],
        # 하좌
        '6': [[0, 1, 0, 0], [0, 0, -1, 0]],
        # 상좌
        '7': [[-1, 0, 0, 0], [0, 0, -1, 0]],
    }

for pos in tunnel['2']:
    print(pos)

row = 3
col = 3
undergroundEdge = [[[] for _ in range(col)] for _ in range(row)]
print(undergroundEdge)
print(undergroundEdge[1][1])

test = {
    1: 10
}

print(test[1])
