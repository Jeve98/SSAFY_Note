test = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
print(list(map(list, zip(*test[::-1]))))

st = 'SEa efK'
for i in st:
    if i.isupper():
        print(i)