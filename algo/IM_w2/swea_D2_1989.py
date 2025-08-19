T = int(input())
for case in range(T):
    letter = input()

    for i in range(len(letter)):
        if letter[i] != letter[len(letter) - 1 - i]:
            print(f'#{case + 1} 0')
            break
    else:
        print(f'#{case + 1} 1')
