# L : length of cake
# N : count of people
# p k : cake number

cakeLength = int(input())
cake = [0 for _ in range(cakeLength)]

people = int(input())
wanderMax = 0
wanderer = 0
for i in range(people):
    data = list(map(int, input().split()))  # [0] : start, [1] : end

    if wanderMax < data[1] - data[0] + 1:
        wanderMax = data[1] - data[0] + 1
        wanderer = i + 1

    for index in range(data[0] - 1, data[1]):
        if cake[index] == 0:
            cake[index] = i + 1

count = [0 for _ in range(people)]
for i in range(cakeLength):
    if cake[i] != 0:
        count[cake[i] - 1] += 1

maxCake = 0
owner = 0
for i in range(people):
    if maxCake < count[i]:
        maxCake = count[i]
        owner = i + 1

# 가장 많이 받을 것이라 기대한 사람, 실제로 가장 많이 받은 사람
print(wanderer, owner, sep='\n')