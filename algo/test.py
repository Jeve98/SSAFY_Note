def test():
    return 1, 3

print(test() + test())
a = [10, 20]
a[0], a[1] = test() + test()
print(a)
