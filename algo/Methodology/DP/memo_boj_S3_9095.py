def separate(last):
    if memoization[last] != -1:
        return memoization[last]

    if last <= 0:
        return 0
    else:
        memoization[last] = separate(last - 1) + separate(last - 2) + separate(last - 3)
        return memoization[last]


T = int(input())
for case in range(T):
    num = int(input())

    memoization = [-1] * 12
    memoization[1] = 1  # 1
    memoization[2] = 2  # 2, 1+1
    memoization[3] = 4  # 3, 2+1, 1+2, 1+1+1

    print(separate(num))
