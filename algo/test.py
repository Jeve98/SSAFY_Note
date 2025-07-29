tmp = [1, 2, 3]
tmp.insert(0, '0' * 2)
tmp.append([0] * 2)
tmp.extend([0, 0])

print(tmp)

for i in range(10):
    if i % 2 == 0:
        i += 1

    print(i)