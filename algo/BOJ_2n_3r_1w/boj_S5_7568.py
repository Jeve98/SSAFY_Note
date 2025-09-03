count = int(input())

people = [0] * count
for i in range(count):
    oneLine = list(map(int, input().split()))
    people[i] = oneLine

rank = [0] * count
for i in range(count):
    for j in range(count):
        if i == j:
            continue

        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1

for i in range(count):
    print(rank[i] + 1, end=' ')
