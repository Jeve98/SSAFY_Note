# practice problem0
s1 = 'xypv'
s2 = 'eoggxypvsy'

ans = True
for i in s1:
    if i not in s2:
        ans = False

if ans:
    print('T')
else:
    print('F')
print()

# practice problem1
n = 5
data = ['GOFFA', 'OYECR', 'UJAJQ', 'JAEZN', 'WJAKC']
for i in data:
    if 'Z' in i:
        print('T')
    else:
        print('F')
print()

# practice problem2
n = 5
data = ['000#0', '00###', '000#0', '00#00', '000#0']
count = 0
for i in data:
    for j in i:
        if j == '#':
            count += 1
print(count)
print()

# practice problem3
n = 5
data = ['GOABA', 'OYCDR', 'UJAJQ', 'JAEZN', 'WJAKC']

ans = False
for i in range(n - 1):
    for j in range(n - 1):
        if data[i][j] == 'A' and data[i][j + 1] == 'B' and data[i + 1][j] == 'C' and data[i + 1][j + 1] == 'D':
            ans = True
            break

print(ans)
print()

# practice problem4
n = 5
data = ['00101', '1#101', '00000', '11101', '00010']

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
count = 0
for i in range(1, 4):
    for j in range(1, 4):
        if data[i][j] == '#' or data[i][j] == '0':
            for addi, addj in zip(di, dj):
                ni = addi + i
                nj = addj + j
                if data[ni][nj] != '0' and data[ni][nj] != '#':
                    break
            else:
                count += 1
print(count)
print()
