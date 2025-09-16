"""
[250916]

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
- Graph
    - 무향 그래프, 유향 그래프, 가중치 그래프, 사이클이 없는 방향 그래프, 완전 그래프, 부분 그래프
    - 표현법 : 인접 행렬, 인접 리스트, 간선 리스트
    - DFS, BFS, Union-Find(Disjoint Set)
        * Depth First Search : 경로 출력, 경우의 수 확인 시에 사용
        * Breadth First Search : 도달까지의 횟수, 혹은 최소 거리 확인 시에 사용
        * Union-Find(Disjoint Set - 배타적 집합, 서로소 집합) : 공통 원소가 없는 집합으로 Graph 병합 시에 Cycle 발생의 확인 가능
            - 연산 : make_set(x), find_set(x), union(x, y)

    - MST(Minimum Spanning Tree, 최소 비용 신장 트리) : 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 Tree
        ex) Prim, Kruskal >> 완전 그래프에 가까울 수록 prim이, 희소 그래프에 가까울 수록 kruskal이 효율적
            * Prim : BFS처럼 특정 정점에서의 후보군을 담되, 해당 후보군 중에서 가장 작은 가중치이자 Cycle이 발생하지 않는 간선을 선택
                >> 정점 기준 선택
                0. MST/visited 배열을 기준으로 우선순위 큐에서 하나의 정점에서 인접한 정점들 중 최소 비용의 간선을 선택
            * Kruskal : 가장 작은 가중치부터 선택하되, Cycle 발생 시 다음 간선을 선택
                >> 간선 기준 선택
                0. 간선의 가중치를 기준으로 정렬
                1. 낮은 가중치 순으로 선택하되 Cycle 발생 시, 취소 - union find

************************************************************** bellman, floyd **********************************
    - 최단 경로 : 특정 정점까지의 경로 중, 가중치의 합이 최소가 되는 경로
        ex) Dijkstra, Bellman-Ford, Floyd-Warshall
            * Dijkstra : Prim과 같이 Greedy를 기반으로 시작 정점에서 특정 정점까지의 최소 누적 거리를 선택하되 음의 가중치를 허용하지 않음
                >> 우선순위 큐에서 출력되는 순간, 최단 누적 거리가 우선해서 출력되므로 해당 정점까지의 최단 거리가 확정됨
            * Bellman-Ford : 특정 정점 간의 최단 경로를 출력하며 음의 가중치를 허용함
            * Floyd-Warshall : 모든 정점들 간의 최단 경로를 출력

    ※ MST vs 최단 경로 : MST는 모든 정점이 연결됨이 보장되지만 최단 경로는 특정 정점 2개의 연결만을 보장함


<실습>


"""