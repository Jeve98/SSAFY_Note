small = []
for i in range(9):
    small.append(int(input()))

# 내림차순 정렬
small.sort(reverse=True)
total = sum(small)
diff = total - 100

ans = []
for top in range(8, 0, -1):
    for down in range(top-1, -1, -1):
        tmpSum = small[top] + small[down]

        if tmpSum == diff:
            ans = [small[top], small[down]]


small.sort()
for i in range(9):
    if small[i] in ans:
        continue

    print(small[i])