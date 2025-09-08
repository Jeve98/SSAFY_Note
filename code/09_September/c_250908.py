# -- brute force subset
def subset(num):
# def subset(num, []):
    if num == count:
        print(candidate)
        return

    candidate.append(arr[num])
    subset(num + 1)
    candidate.pop()
    subset(num + 1)

    # subset(num + 1, candidate + [arr[num]])
    # subset(num + 1, candidate)


count = 3
arr = ['a', 'b', 'c']
candidate = []
subset(0)
# subset(0, [])
print()


# -- binary counting subset
# i (0~2^n) : i 번째 부분 집합 - 검사하는 bit 자리를 좌측으로 shift 하며 검사
for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        if i & (1 << idx):
            print(arr[idx], end=' ')
    print()


# 검사 대상의 bit 자리를 우측으로 shift 하며 검사
def subset(tar):
    for i in range(len(arr)):
        if tar & 0x1:   # bit 연산임을 강조하기 위한 16진수 1 표기
            print(arr[i], end=' ')
        tar >>= 1


for target in range(1 << len(arr)):
    subset(target)
    print()
print()


# -- combination
def combination(num, pos):
    if num == select:
        print(path)
        return

    for i in range(pos, len(arr)):
        path.append(arr[i])
        # 순열과 달리, 순서가 중요하지 않으므로, 선택지를 줄이는 방식으로 동작
        combination(num + 1, i + 1)     # 중복을 허용하지 않는 조합
        # combination(num + 1, i)       # 중복을 허용하는 조합
        path.pop()


arr = ['a', 'b', 'c', 'd', 'e']
select = 3
path = []
combination(0, 0)
print()


# practice problem0 - 최소 동전
# 500 * 3, 100 * 2, 10 * 3
coin = [500, 100, 50, 10]
target = 1730
count = 0

for i in range(len(coin)):
    if coin[i] < target:
        tmp = target // coin[i]
        count += tmp
        target -= (coin[i] * tmp)

    if target == 0:
        break

print(count)
print()


# practice problem1 - 최소 대기 시간
# 10 * 3, 15 * 2, 30 * 1
user = [15, 30, 50, 10]
user.sort()
wait = 0

for i in range(len(user)):
    tmp = user[i] * (len(user) - i - 1)
    wait += tmp

print(wait)
