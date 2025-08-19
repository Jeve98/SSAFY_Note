T = int(input())
for case in range(T):
    string1 = input()
    string2 = input()

    ls = [0] * len(string1)
    for i in range(len(string1)):
        for j in string2:
            if string1[i] == j:
                ls[i] += 1

    ls.sort(reverse=True)

    print(f'#{case + 1} {ls[0]}')
