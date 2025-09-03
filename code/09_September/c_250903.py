# 16진수 변환
def d_to_h(n):
    if n == 0:
        return 0

    # 별도의 if문 없이 나올 수 있는 모든 경우의 수를 문자열로 저장하고, 해당하는 인덱스 번째로 접근
    hex_digit = "0123456789ABCDEF"
    ans = ''

    while n != 0:
        index = n % 16
        ans = hex_digit[index] + ans
        n //= 16

    return ans


print(d_to_h(15), d_to_h(17), d_to_h(0))


# 비트 연산
ans = int('11011110', 2) & int('11011', 2)
print(ans, bin(ans))
ans = int('4A3', 16) | 25
print(ans, hex(ans))


# subset
arr = [1, 2, 3, 4]
# subset 개수 : 1 << len(arr) - 2^len(arr)
for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        # i : 0, 1, 2, ..., 2^len(arr) - 1 == 0, 1, 10, 11, ..., 1111
        # 1 << idx : 1, 10, 100, 1000, ...
        if i & (1 << idx):
            print(arr[idx], end=' ')
    print()
