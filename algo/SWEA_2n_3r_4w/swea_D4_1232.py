def inorder(now):
    # 연산자
    if tree[now] in "+-*/":
        if tree[now] == '+':
            return inorder(vertex[now][0]) + inorder(vertex[now][1])
        elif tree[now] == '-':
            return inorder(vertex[now][0]) - inorder(vertex[now][1])
        elif tree[now] == '*':
            return inorder(vertex[now][0]) * inorder(vertex[now][1])
        elif tree[now] == '/':
            return inorder(vertex[now][0]) // inorder(vertex[now][1])
    # 피연산자
    else:
        return int(tree[now])


for case in range(10):
    nodeCount = int(input())

    tree = [0] * (nodeCount + 1)
    vertex = [[] for _ in range(nodeCount + 1)]
    for i in range(nodeCount):
        oneLine = list(input().split())
        oneLine[0] = int(oneLine[0])

        # 피연산자 노드
        if len(oneLine) == 2:   # [0]: node count, [1]: value
            tree[oneLine[0]] = oneLine[1]
        # 연산자 노드
        else:   # [0]: node count, [1]: type, [2]: left child, [3]: right child
            tree[oneLine[0]] = oneLine[1]
            vertex[oneLine[0]].append(int(oneLine[2]))
            vertex[oneLine[0]].append(int(oneLine[3]))

    print(f'#{case + 1} {inorder(1)}')
