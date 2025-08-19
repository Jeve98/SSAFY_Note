T = int(input())
for case in range(T):
    str, macro = input().split()

    count = 0
    i = 0
    j = 0
    while i < len(str):
        if str[i] != macro[j]:
            i = i - j + 1
            j = 0

        i += 1
        j += 1

        # 매크로 사용이 가능한 문자열이 발견된 경우
        if j == len(macro):
            count += 1
            j = 0

    # 매크로 1회 == 1회 타이핑
    ans = len(str) - (len(macro) * count) + count
    print(f'#{case + 1} {ans}')
