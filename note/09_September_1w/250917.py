"""
[250917]

<알고리즘 라이브 강의>

Union-Find
    - 단순 Union-Find : O(n)
    - Rank : O(log n)
    - Path Comprehension : 조금 느린 O(1) == O(역아커만(n))

MST
    - Prim : 우선순위 큐에 후보군을 추가하고 최소값을 추출 == O(V log V(각 정점이 힙에 추가) + E log V(간선의 수만큼 힙에 추가))
    - Kruskal : 간선 정렬 + 간선 선택(사이클 검사) == O(E log E + E)

최단거리
    - Dijkstra : 우선순위 큐에 간선을 추가 == O(E log V)


<실습>


"""