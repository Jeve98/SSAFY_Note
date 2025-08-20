# subset by backtracking 일반론
def backtrack(a, k, n):  # a 주어진 배열, k 결정할 원소, n 원소 개수
    c = [0] * MAXCANDIDATES

    if k == n:
        process_solution(a, k)  # 답이면 원하는 작업을 한다
    else:
        # 매번 같은 수의 대체가 존재하지 않을 수도 있다
        # ex) 미로 찾기에서 분기점에서 마주하는 길은 하나일 수도, 여럿일 수도 있다
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)


def construct_candidates(a, k, n, c):  # 후보 추천
    c[0] = True  # 원소의 포함 여부
    c[1] = False
    return 2


def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end=' ')
    print()


MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
num = [1, 2, 3, 4]
backtrack(a, 0, 3)

# 분할 정복
def power(base, exponent):
    if exponent == 0:
        return 1

    if exponent % 2 == 0:
        new_base = power(base, exponent // 2)
        return new_base * new_base
    else:
        new_base = power(base, (exponent - 1) // 2)
        return (new_base * new_base) * base


# --실습--
arr = [i for i in range(1, 6)]
size = len(arr)


# permutation : n개의 원소 중 r개를 뽑아 순서를 고려하고 나열
def permutation(now):
    # 기저 조건 : 종료 조건
    if now == r:
        print(result)
        return

    # 유도 조건 : 재귀 조건
    for i in range(size):
        if not visited[i]:
            visited[i] = True
            result[now] = arr[i]
            permutation(now + 1)
            # 다음 i번 째 처리를 위해 방문처리 초기화
            visited[i] = False


r = 3
visited = [False] * size
result = [0] * r
permutation(0)


# subset
def subset(now):
    # 기저 조건 : 종료 조건
    if now == size:
        for i in range(size):
            if out[i]:
                print(arr[i], end=' ')
        print()
        return

    # 유도 조건 : 재귀 조건
    for i in [True, False]:
        out[now] = i
        subset(now + 1)


out = [False] * size
subset(0)
