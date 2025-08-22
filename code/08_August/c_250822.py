# Binary Tree traversal
nodeCount = 13
edgeData = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
edgeData = list(map(int, edgeData.split()))

edge = [[] for _ in range(nodeCount + 1)]
parentsEdge = [False] * (nodeCount + 1)
for i in range(0, nodeCount + 1, 2):
    edge[edgeData[i]].append(edgeData[i + 1])
    parentsEdge[edgeData[i + 1]] = edgeData[i]

# 자식 노드가 하나만 존재할 경우, 오른쪽 자식으로 None 추가
for i in range(1, nodeCount + 1):
    while len(edge[i]) < 2:
        edge[i].append(None)

"""
                  1
               /     \
              2       3
             /     /    \
            4     5      6
           /     / \\   / \
          7     8   9  10  11
         /                /
        12               13
"""
print(edge)
preO = 'pre  : 1 2 4 7 12 3 5 8 9 6 10 11 13'
inO = 'in   : 12 7 4 2 1 8 5 9 3 10 6 13 11'
postO = 'post : 12 7 4 2 8 9 5 10 13 11 6 3 1'


def preorder(parents):
    if parents:
        print(parents, end=' ')
        preorder(edge[parents][0])
        preorder(edge[parents][1])


def inorder(parents):
    if parents:
        inorder(edge[parents][0])
        print(parents, end=' ')
        inorder(edge[parents][1])


def postorder(parents):
    if parents:
        postorder(edge[parents][0])
        postorder(edge[parents][1])
        print(parents, end=' ')


print(preO)
print('pre  :', end=' ')
preorder(1)
print()
print(inO)
print('in   :', end=' ')
inorder(1)
print()
print(postO)
print('post :', end=' ')
postorder(1)
print()


def findAncestor(target):
    if parentsEdge[target]:
        ancestor.append(parentsEdge[target])
        findAncestor(parentsEdge[target])


ancestor = []
findAncestor(13)
print(ancestor)
