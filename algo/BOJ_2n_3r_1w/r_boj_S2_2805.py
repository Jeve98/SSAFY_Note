import sys
sys.stdin = open('../input.txt', 'r')

treeC, target = map(int, input().split())
tree = list(map(int, input().split()))

l = 1
r = max(tree)
ans = 0
while l <= r:
    mid = (l + r) // 2

    count = 0
    for i in tree:
        if i >= mid:
            count += (i - mid)

    if count < target:
        r = mid - 1
    else:
        ans = mid
        l = mid + 1

print(ans)
