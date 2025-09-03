count = int(input())

people = [0] * count
for i in range(count):
    oneLine = list(input().split())
    oneLine[0] = int(oneLine[0])
    people[i] = oneLine

people.sort(key=lambda x: x[0])
for i in range(count):
    print(people[i][0], people[i][1])
