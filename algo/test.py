ls = [[1, 2, 3], [4, 5, 6]]


def test(ls):
    nls = ls[:]
    nls[0][1] = 'a'
    print(nls)


print(ls)
test(ls)
print(ls)
print(id(ls[0][1]), id(ls[1][1]))

for i in range(1, 1):
    print(i)
