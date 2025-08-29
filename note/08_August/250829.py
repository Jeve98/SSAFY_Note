"""
[250829]

<알고리즘 라이브 강의>

Tree
- Binary Tree
    * Full Binary Tree
        - Complete Binary Tree
    * Skewed Binary Tree
    * Expression Binary Tree

    * BST(Binary Search Tree) : O(log n)의 빠른 검색 속도를 갖출 수 있도록 서로 다른 유일한 키를 갖는 데이터를 체계적으로 저장해둔 자료구조
        - 삽입 : 탐색 연산이 실패한 위치에 삽입
        - 삭제 : 삭제된 노드의 좌측 sub tree의 가장 우측 자식을 새로운 노드로 사용 (균형 파괴 가능)
- 순회
    ※ 부모 기준
    - 전위순회(preorder traversal) - VLR
    - 중위순회(inorder traversal) - LVR
    - 후위순회(postorder traversal) - LRV
- 표현
    - 배열
        * 1차원 배열 내에서 (i * 2), (i * 2 + 1)로 자식 표현
        * 별도의 좌측, 우측, 부모 배열 사용
    - Linked List


Heap : Complete Binary Tree에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해 만든 자료구조
- 최대 힙 : 부모 노드의 값이 자식 노드의 값보다 큰 Complete Binary Tree
- 최소 힙 : 부모 노드의 값이 자식 노드의 값보다 작은 Complete Binary Tree

- 삽입 : 자리 확장 및 저장 이후, heap의 종류에 따라 부모 노드와 자리 변경
- 삭제 : 루트 노드의 원소만 삭제가 가능하며 삭제 및 반환 이후, 마지막 노드를 루트로 올린 후, heap의 종류에 따라 더 알맞는 자식 노드와 자리 변경

- heap sort : 삭제되는 순서대로 별도의 sort arr에 저장하면 정렬 완료
- 우선순위 Queue : heap의 키를 우선순위로 이용하여 구현한 Queue


<실습>


"""