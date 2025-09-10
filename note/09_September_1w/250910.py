"""
[250910]

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

    - 분할 정복 기법 : 문제를 작은 하위 문제로 나누어 각각 해결한 뒤, 그 결과를 결합하여 해결하는 기법
        - Top-Down approach : 문제를 n/2으로 나누어 분할하여 정복 후 결합
        ex) merge sort, quick sort, binary search
            * merge sort - O(n log n) : 다수의 정렬된 자료의 집합을 병합하여 1개의 정렬된 집합을 생성하는 방식으로 다수의 프로세서에서 병렬적으로 정렬할 때 사용
                1. 집합의 요소가 1개가 될 때까지 분할
                2. 2개의 집합의 요소간 대소를 비교하며 병합
            * quick sort - O(n log n) : 기준값을 중심으로 배열을 2개로 분할하고 정렬하여 전체를 정렬하는 방식으로 대량 데이터에서 높은 효율을 보임
                1. partitioning : pivot을 기준으로 작은 수를 좌측에, 큰 수를 우측에 배치 (pivot의 위치만 정렬된 상태)
                2. pivot의 좌우측 집합에 대하여 partitioning 반복
                    ※ Hoare-partition : 최좌측, 최우측, 중앙의 값 중에서 중간값을 pivot으로 설정하고 정순으로 큰 값을 찾고, 역순으로 작은 값을 찾으며 이 둘의 위치를 교환
                    ※ Lomuto-partition : 한 방향에서 각각 큰 값, 작은 값을 찾으며 진행하다가 둘의 위치를 변경
            * binary search - O(log n)
                ※ lower bound / upper bound
                ※ parametric search : 최적화 문제를 결정 문제로 변환하는 방법으로 결정 문제를 반복하여 최적화 문제에 대한 답을 구함
                    - 최적화 문제 : 조건을 만족하는 최대/최소값은 얼마인가
                    - 결정 문제 : 현재의 값으로 조건을 만족하는가


<실습>


"""