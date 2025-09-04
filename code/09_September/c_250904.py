# practice problem0
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
print()


# practice problem1 - permutation
path = []
maxCount = 3
participant = ['a', 'b', 'c', 'd', 'e']


def repetitionPermutation(count):
    if count == maxCount:
        print(path)
        return

    for i in range(len(participant)):
        path.append(participant[i])
        repetitionPermutation(count + 1)
        path.pop()


print('repetition permutation')
repetitionPermutation(0)
print()


def permutation(now):
    if now == maxCount:
        print(path)
        return

    for i in range(len(participant)):
        if not visited[i]:
            path.append(participant[i])
            visited[i] = True
            permutation(now + 1)
            path.pop()
            visited[i] = False


print('permutation')
visited = [False] * len(participant)
permutation(0)
print()


# practice problem2
participant = [1, 2, 3, 4, 5, 6]


# - memorize path
def permutation(now):
    global under10

    ans = sum(path)
    if ans > 10:
        return

    if now == diceCount:
        under10 += 1
        return

    for i in range(len(participant)):
        path[now] = participant[i]
        permutation(now + 1)
        path[now] = 0


# - non-memorize path
def prefix_permutation(now, total):
    global under10

    if total > 10:
        return

    if now == diceCount:
        under10 += 1
        return

    for i in range(len(participant)):
        prefix_permutation(now + 1, total + participant[i])


# - memorize path
diceCount = 3
under10 = 0
path = [0] * 3
permutation(0)
print(under10)
print()

# - non-memorize path
under10 = 0
prefix_permutation(0, 0)
print(under10)
print()


# practice problem3
def over_three():
    for i in range(3):
        if path[i] == path[i + 1] == path[i + 2]:
            return True

    return False


def permutation(count):
    global result

    if count == 5:
        if over_three():
            result += 1
        return

    for i in range(len(cards)):
        path[count] = cards[i]
        permutation(count + 1)


cards = ['A', 'K', 'Q', 'J']
path = [0] * 5
result = 0
permutation(0)
print(result)
