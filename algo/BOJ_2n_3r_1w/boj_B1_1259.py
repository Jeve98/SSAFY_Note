while True:
    oneLine = input()

    if oneLine == '0':
        break

    if oneLine == oneLine[::-1]:
        print('yes')
    else:
        print('no')
