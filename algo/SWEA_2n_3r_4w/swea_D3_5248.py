# import sys
# sys.stdin = open('../input.txt', 'r')


def make_set(x):
    parent = [i for i in range(x + 1)]
    rank = [0] * (x + 1)

    return parent, rank


def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])

    return parents[x]


def union(x, y):
    x_rep = find_set(x)
    y_rep = find_set(y)

    # 같은 집합
    if x_rep == y_rep:
        return

    if ranks[x_rep] > ranks[y_rep]:
        parents[y_rep] = x_rep
    elif ranks[x_rep] < ranks[y_rep]:
        parents[x_rep] = y_rep
    else:
        parents[y_rep] = x_rep
        ranks[x_rep] += 1


T = int(input())
for case in range(T):
    peopleC, paperC = map(int, input().split())
    data = list(map(int, input().split()))

    parents, ranks = make_set(peopleC)
    for i in range(0, paperC):
        union(data[i * 2], data[i * 2 + 1])

    count = set()
    for i in range(1, peopleC + 1):
        count.add(find_set(i))

    print(f'#{case + 1} {len(count)}')
