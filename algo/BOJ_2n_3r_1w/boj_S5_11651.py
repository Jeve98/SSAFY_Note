count = int(input())

pos = [0] * count
for i in range(count):
    oneLine = list(map(int, input().split()))
    pos[i] = oneLine

pos.sort(key=lambda x: (x[1], x[0]))
for i in range(count):
    print(pos[i][0], pos[i][1])
