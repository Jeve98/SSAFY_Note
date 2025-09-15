# import sys
# sys.stdin = open('../input.txt', 'r')

from collections import deque

T = int(input())
for case in range(T):
    start, target = map(int, input().split())

    calculate = [1, -1, 2, -10]

    queue = deque()
    for i in calculate:
        queue.append([start, i, 0])     # [0]: 현재까지의 연산 결과, [1]: 다음 연산, [2]: 연산 횟수

    visited = set()

    while queue:
        now = queue.popleft()

        if now[0] == target:
            print(f'#{case + 1} {now[2]}')
            break

        # M <= 1000000
        if now[0] > 1000000:
            continue

        tmp = 0
        if now[1] == 2:
            tmp = now[0] * now[1]
        else:
            tmp = now[0] + now[1]

        # 불필요한 연산을 막기 위해 visited 사용
        # 단, 값의 범위를 명확히 알 수 없고, 최대치로 배열을 생성할 경우, 불필요하게 메모리를 낭비하므로 set을 이용
        if tmp not in visited:
            visited.add(tmp)

            for i in calculate:
                queue.append([tmp, i, now[2] + 1])
