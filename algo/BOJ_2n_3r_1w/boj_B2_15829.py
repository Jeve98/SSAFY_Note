length = int(input())
string = input()

hashing = 'abcdefghijklmnopqrstuvwxyz'

ans = 0
for i in range(length):
    convert = 0
    for index in range(len(hashing)):
        if string[i] == hashing[index]:
            convert = index + 1
            break
    ans += convert * (31 ** i)

ans %= 1234567891
print(ans)
