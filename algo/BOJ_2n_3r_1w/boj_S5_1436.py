num = int(input())

ans = 666
count = 1
while count < num:
    ans += 1

    if '666' in str(ans):
        count += 1

print(ans)
