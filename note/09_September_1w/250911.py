"""
[250911]

<알고리즘 라이브 강의>

알고리즘
- Brute Force > Greedy > DP > 분할 정복 > 특화 알고리즘
    - Brute Force
        - 반복 (n번 반복)
            ex) DFS, BFS, ...
        - 재귀 (n중 반복)
            ex) 순열, 조합, 부분집합, DFS, ...
            * 순열, 중복 순열, 부분 집합, 조합

    - Greedy
        1. 반복되는 규칙 발견
        2. Greedy 검증
            2-1. 탐욕적 선택 조건 (Greedy Choice Property) >> 각 단계의 규칙이 변하지 않을 것
            2-2. 최적 부분 구조 (Optimal Substructure) >> 직/간접 증명, 귀납법, 귀류법 등을 이용하여 논리적으로 증명하거나 직관에 따라 반례를 찾을 것
        ex) 배수 관계에 있는 동전 교환(변형된 knapsack), fractional knapsack, 활동 선택
            * 동전 교환, fractional knapsack, 활동 선택

    - DP
        - Memoization
        - Tabulation
        ex) 배수 관계가 없는 동전 교환, 0-1 knapsack
            * 0-1 knapsack

    - 분할 정복 기법
        - Top-Down approach
        ex) merge sort, quick sort, binary search
            * merge sort - O(n log n)
            * quick sort - O(n log n)
                ※ Hoare-partition
                ※ Lomuto-partition
            * binary search - O(log n)
                ※ lower bound / upper bound
                ※ parametric search

    - Backtracking (Pruning)
        ex) N-Queen
            * N-Queen : BF로 진행 시, O(n^n)가 소요되고 DFS로 진행 시, O(n!)가 소요되므로 backtracking이 필수적으로 요구됨


자료구조
- Graph
    - Tree : non-cycle, non-direction Graph that non-linear, hierarchical data structure
    - Heap
        ※ import heapq - 기본적으로 min heap으로 구현되어 있으므로, max heap을 만들기 위해서는 값을 음수로 만들어서 enqueue 해줄 필요가 있음
        >> 삽입 / 삭제가 빈번한 경우, list와 더불어 매번 sort를 사용하는 것보다 heap을 사용하는 것이 효율적


<실습>


"""