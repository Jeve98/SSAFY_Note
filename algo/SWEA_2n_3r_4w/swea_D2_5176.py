def inorder(now):
    global increase

    if now < len(tree):
        inorder(now * 2)
        tree[now] = increase
        increase += 1
        inorder(now * 2 + 1)


T = int(input())
for case in range(T):
    num = int(input())

    tree = [0] * (num + 1)

    increase = 1
    inorder(1)

    print(f'#{case + 1} {tree[1]} {tree[int(num / 2)]}')
