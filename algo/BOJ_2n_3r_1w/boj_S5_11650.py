count = int(input())

pos = [0] * count
for i in range(count):
    oneLine = list(map(int, input().split()))
    pos[i] = oneLine

pos.sort()
for i in range(count):
    print(pos[i][0], pos[i][1])
