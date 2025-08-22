def inorder(parents):
    if parents:
        parents = int(parents)
        inorder(tree[parents][1])
        print(tree[parents][0], end='')
        inorder(tree[parents][2])


for case in range(10):
    nodeCount = int(input())

    tree = [[] for _ in range(nodeCount + 1)]
    for i in range(nodeCount):
        oneLine = list(input().split())     # [0]: node num, [1]: data, [2, 3]: connected node (left, right)

        for data in range(1, len(oneLine)):
            tree[int(oneLine[0])].append(oneLine[data])     # [0]: data, [1, 2]: connected node (left, right)

        # 비어있는 자식 노드를 None으로 변환
        while len(tree[int(oneLine[0])]) < 3:
            tree[int(oneLine[0])].append(None)

    print(f'#{case + 1} ', end='')
    inorder(1)
    print()
