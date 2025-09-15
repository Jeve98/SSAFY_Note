# import sys
# sys.stdin = open('../input.txt', 'r')


def make_set(n):
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    return parent, rank


def find_set(n):
    if n == parents[n]:
        return n

    parents[n] = find_set(parents[n])

    return parents[n]


def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return

    if ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    elif ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    else:
        parents[rep_y] = rep_x
        ranks[rep_x] += 1


T = int(input())
for case in range(T):
    peopleC, edgeC = map(int, input().split())

    parents, ranks = make_set(peopleC)
    for i in range(edgeC):
        oneLine = list(map(int, input().split()))
        union(oneLine[0], oneLine[1])

    count = set()
    for i in range(peopleC):
        count.add(find_set(i + 1))

    print(f'#{case + 1} {len(count)}')
