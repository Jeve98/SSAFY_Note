"""
[250915]

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
            * N-Queen


자료구조
- Graph : 데이터 간의 연결 관계를 표현한 자료구조로 정점과 간선의 집합으로 이루어져, N:N 관계를 표현하기 용이
    - 무향 그래프, 유향 그래프, 가중치 그래프, 사이클이 없는 방향 그래프, 완전 그래프, 부분 그래프
    - 표현법 : 인접 행렬, 인접 리스트, 간선 배열
        * 인접 행렬 : 2차원 배열을 이용하여 간선의 유무 정보를 저장
            >> 직관적이고 검색이 빠르며 가중치와 같은 추가적인 정보 저장에 유리하지만 저장 공간의 낭비가 발생
        * 인접 리스트 : 각 정점마다 인접한 정점을 연결 리스트 혹은 배열로 저장
            >> 공간 낭비가 적으나 검색이 느리고 추가적인 정보 저장이 어려움
        * 간선 리스트 : 한 간선을 두 정점의 쌍으로 표현하여 저장
    - DFS, BFS, Union-Find(Disjoint Set)
        * Depth First Search : 경로 출력, 경우의 수 확인 시에 사용
            - 재귀 호출 : 구현이 쉽지만 느리고 재귀 호출 제한이 존재함
            - 반복문 (stack) : 빠르지만 구현이 상대적으로 어려움
        * Breadth First Search : 도달까지의 횟수, 혹은 최소 거리 확인 시에 사용
            - 반복문 (queue)
                > queue에 추가하며 방문 초기화 : 중복 최소화 가능
                > queue에서 출력하며 방문 초기화
        * Union-Find(Disjoint Set - 배타적 집합, 서로소 집합) : 공통 원소가 없는 집합으로 Graph 병합 시에 Cycle 발생의 확인 가능
            - 대표자 : 각 집합을 대표하는 하나의 원소
            - 연산
                * make_set(x) : 유일한 멤버 x를 포함하는 새로운 집합을 생성
                * find_set(x) : 집합의 대표자 반환을 통해 x를 포함하는 집합 검색
                * union(x, y) : x, y를 포함하는 두 집합 통합하되, 통합 시에 rank(sub-tree의 높이)를 이용하여 더 작은 집합을 이동
            - 구현
                * linked-list
                * tree : 자식 노드가 부모 노드를 가리키며 root node를 대표자로 설정
                ※ 편향 tree 혹은 깊이가 깊을 경우, 불필요한 재귀가 발생할 수 있으므로 find_set() 동작 시 마다 경로 압축을 사용


<실습>

swea 5247, 5248 7465
백준 4963 - dfs, bfs
"""