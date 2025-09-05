T = int(input())
for case in range(T):
    floor = int(input())
    room = int(input())

    apt = [[i for i in range(room + 1)] for _ in range(floor + 1)]
    for i in range(1, floor + 1):
        for j in range(1, room + 1):
            apt[i][j] = apt[i - 1][j]
            for k in range(j):
                apt[i][j] += apt[i - 1][k]

    print(apt[floor][room])
