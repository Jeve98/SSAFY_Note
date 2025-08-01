studentCount = int(input())
lotta = list(map(int, input().split()))

student = [0 for _ in range(studentCount)]

for i in range(studentCount):
    if lotta[i] == 0:
        student[i] = i
    else:
        for j in range(i):
            student[i] = i - lotta[i]
            if student[j] >= student[i]:
                student[j] += 1

ans = [0 for _ in range(studentCount)]
for i in range(studentCount):
    ans[student[i]] = i

for i in ans:
    print(i + 1, end=' ')