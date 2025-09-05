isbn = input()

check = 0
ans = 1
for i in range(len(isbn)):
    if i % 2 == 0:
        additional = 1
    else:
        additional = 3

    if isbn[i] != '*':
        check += int(isbn[i]) * additional
    else:
        ans = additional

for i in range(10):
    if (check + ans * i) % 10 == 0:
        ans = i
        break

print(ans)
