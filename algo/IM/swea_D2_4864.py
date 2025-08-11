T = int(input())
for case in range(T):
    str1 = input()
    str2 = input()

    find = True
    for i in range(len(str2) - len(str1) + 1):
        for j in range(len(str1)):
            if str2[i + j] != str1[j]:
                find = False
                break
        else:
            find = True
            break

    if find:
        print(f'#{case + 1} 1')
    else:
        print(f'#{case + 1} 0')
