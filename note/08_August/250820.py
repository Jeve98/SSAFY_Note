"""
[250820]

<알고리즘 라이브 강의>

Queue : FIFO의 front와 rear로 구성된 선형 자료구조
- 연산 : enqueue, dequeue, create_queue, is_empty, is_full, qpeek(queue의 front 원소를 삭제 없이 반환)

- 구현
    - Linear Queue : 데이터를 일렬로 저장하는 기본 Queue
        * 배열, 연결 리스트로 구현하되, front, rear의 위치와 queue의 size만으로 empty, full을 구현

    - Circular Queue : Linear Queue에서 배열 앞부분을 활용하지 못하는 단점을 해결하기 위한 응용 Queue
        1. 매 연산시 마다 저장된 원소들을 배열의 앞부분으로 이동 : 이동 시간이 급격하게 증가하여 효율성 급감
        2. 1차원 배열에서 front, rear가 size 이상으로 넘어갈 경우, 0으로 초기화
            * size 이상의 데이터를 수신한 경우, (크게 중요하지 않은 경우) 덮어쓰거나, (중요한 데이터인 경우) 데이터 수신을 보류

    - Linked-List Queue : 연결 리스트로 구현한 Queue로 자유로운 Queue의 확장이 가능한 응용 Queue
        * 연결 리스트로 구현하며 front, rear를 각각 첫 번째, 마지막 노드를 가리키는 링크로 활용
        
    - Priority Queue : FIFO가 아닌 우선순위에 따라 데이터를 출력하는 Queue로 시뮬레이션, 네트워크 트래픽 제어, 운영체제의 스케쥴링 등에 사용
        * 배열로 구현할 경우, 우선순위에 따라 적절한 위치에 삽입하거나 원소를 재배치하므로 시간, 메모리 낭비가 큼
        * 연결 리스트 

- 사용
    - 버퍼 : 데이터를 다른 곳으로 전송하는 동안 일시적으로 데이터를 보관하는 메모리 영역으로 입출력, 네트워크 관련 기능에서 이용
    ※ 버퍼링 : 버퍼를 활용하는 방식 혹은 버퍼를 채우는 동작


Deque(덱) : 양쪽 끝에서 빠르게 추가/삭제가 가능한 리스트류 컨테이너 자료형
- from collections import deque
- 연산 : append / appendleft, pop / popleft


<실습>


"""