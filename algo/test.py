tmp = [1, 2, 3]
tmp.insert(0, '0' * 2)
tmp.append([0] * 2)
tmp.extend([0, 0])

print(tmp)
