def test(now):
    for i in range(now, 19, 2):
        print(f'now: {now}, i: {i}', end=' ')
        test(i + 4)
    print()

test(3)