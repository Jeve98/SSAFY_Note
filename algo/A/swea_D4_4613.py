T = int(input())
for case in range(T):
    row, col = map(int, input().split())

    flag = []
    for i in range(row):
        oneLine = input()
        flag.append(oneLine)

    ans = []
    for startLine in range(1, row - 1):
        for endLine in range(1, row - startLine):
            count = 0
            # testing = list(map(list, flag))
            # 하얀줄
            for i in range(0, startLine):
                for j in range(col):
                    if flag[i][j] != 'W':
                        count += 1
                        # testing[i][j] = 'W'
            # 파란줄
            for i in range(startLine, startLine + endLine):
                for j in range(col):
                    if flag[i][j] != 'B':
                        count += 1
                        # testing[i][j] = 'B'
            # 빨간줄
            for i in range(startLine + endLine, row):
                for j in range(col):
                    if flag[i][j] != 'R':
                        count += 1
                        # testing[i][j] = 'R'

            ans.append(count)
            # for i in range(row):
            #     print(''.join(testing[i]))
            # print()

    print(f'#{case + 1} {min(ans)}')
