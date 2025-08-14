"""
[250814]

<알고리즘 라이브 강의>

Stack
- 사용
    0. 괄호 검사
    1. Function Call
    2. DFS - 비선형구조(그래프)에서 모든 자료를 빠짐없이 검색하기 위한 탐색
    3. 중위 표기법의 후위 표기법 변환 및 계산
        * 변환
        1) 입력 받은 중위 표기법에서 토큰을 읽는다.
        2) 토큰이 피연산자면 토큰을 출력한다.
        3) 토큰이 연산자일 때,
            - 이 토큰이 스택의 top에 위치한 연산자보다 우선순위가 높으면 push한다.
            - 그렇지 않으면 연산자의 우선순위보다 작을 때까지 pop한 후 push한다.
        4) 토큰이 닫는 괄호면 여는 괄호가 나올 때까지 pop한다.
            - 스택 밖의 여는 괄호는 우선순위가 가장 높으며 스택 안의 여는 괄호는 우선순위가 가장 낮다.
        ex) input : (6 + 5 * (2 - 8) / 2)   stack = none
            print : 6,                      stack = (
            print : 6,                      stack = ( +
            print : 6 5,                    stack = ( +
            print : 6 5,                    stack = ( + *
            print : 6 5,                    stack = ( + * (
            print : 6 5 2,                  stack = ( + * ( -
            print : 6 5 2 8 -,              stack = ( + *    (여는 괄호는 출력하지 않는다)
            print : 6 5 2 8 - *,            stack = ( + /
            print : 6 5 2 8 - * 2,          stack = ( + /
            print : 6 5 2 8 - * 2 / +,      stack = none   (여는 괄호는 출력하지 않는다)

        * 계산
        1) 피연산자를 만나면 push한다.
        2) 연산자를 만나면 필요한 만큼 피연산자를 pop하고 그 결과를 다시 push한다.
        3) 수식이 끝나면 마지막으로 pop하여 출력한다.
        ex) input : 6 5 2 8 - * 2 / +,      stack = none
            input : - * 2 / +,              stack = 6 5 2 8
            input : * 2 / +,                stack = 6 5 -6(2 - 8)
            input : 2 / +,                  stack = 6 -30(5 * -6)
            input : / +,                    stack = 6 -30 2
            input : +,                      stack = 6 -15(-30 / 2)
            input : none,                   stack = -9(6 + -15)
            print : -9,                     stack = none

    4. Backtracking : 후보해를 구성하다가 해가 될 수 없다고 판단되면 되돌아가서 다른 경로를 시도하는 방법으로 최적화, 결정 문제에 적용
        ex) N-Queens, 미로, 순열/조합, 부분집합, 스도쿠
        - Prunning의 유무로 일반적인 DFS와 구분됨
            ※ Prunning : Promising(유망)하지 않은 경로를 계산에서 제외하는 것


<실습>


"""