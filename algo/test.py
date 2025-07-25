test = [0] * 5
tmp = []
tmp.append(test)
tmp.append(test)
print(tmp)

tmp = [0 * 5]
print(len(tmp), tmp)

tmp = [0 for _ in range(5)]
print(len(tmp), tmp)

test = [[] for _ in range(5)]
print(test)
test[1].append(1)
print(test)