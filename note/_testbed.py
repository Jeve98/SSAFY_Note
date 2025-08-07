tmp = bin(11)
tmp = str(tmp)
count = 0
for i in tmp:
    if i == '1':
        count += 1
print(count, tmp)