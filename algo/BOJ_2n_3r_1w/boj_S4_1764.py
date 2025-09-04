hear, see = map(int, input().split())

find = set()
both = set()
for i in range(hear + see):
    name = input()
    if name in find:
        both.add(name)
    else:
        find.add(name)

print(len(both))
both = list(both)
both.sort()
for i in range(len(both)):
    print(both[i])
