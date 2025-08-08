T = int(input())
for case in range(T):
    data = list(map(int, input().split()))  # [0]: size, [1]: length

    vertical = [[] for _ in range(data[0])]
    ans = []
    find = False
    for i in range(data[0]):
        oneLine = input()

        # 세로열 생성
        for k in range(data[0]):
            vertical[k].append(oneLine[k])

        # 가로열 검사
        if not find:
            for j in range(0, data[0] - data[1] + 1):
                if oneLine[j:j + data[1]] == oneLine[j:j + data[1]][::-1]:
                    ans = oneLine[j:j + data[1]]
                    find = True
                    break

    # 가로열에서 찾은 경우, 세로열은 탐색하지 않음
    if not find:
        for oneLine in vertical:
            if find:
                break

            for i in range(0, data[0] - data[1] + 1):
                if oneLine[i:i + data[1]] == oneLine[i:i + data[1]][::-1]:
                    ans = oneLine[i:i + data[1]]
                    find = True
                    break

    print(f'#{case + 1} {"".join(ans)}')
