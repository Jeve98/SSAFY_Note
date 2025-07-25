"""
[250723]

<Python 라이브 강의>

function : 특정 기능을 수행하는 재사용 가능한 코드의 묶음 (가독성, 유지보수성, 재사용성 상승)
- structure : input(parameter), function body(docstring & logic), output(return value)
    ※ return문이 없는 경우(return value가 없는 경우), None을 반환
    ex) print() >> 반환 != 출력
    - Python Style Guide
        * Function Name : 소문자와 언더스코어를 기반으로(snake case) 동사로 시작하여 함수의 동작을 설명하되 명어 사용을 지양
            ex) def save_user()
            ex) def is/has_true()
        * Docstring(함수 설명) : 내부부터 작성하지 않고 3따옴표 이후 바로 이어서 작성
    
    - Parameter(매개변수) and Argument(인자)
        parameter : 함수를 정의할 때, 함수가 받을 값을 나타내는 '변수'
        Argument : 함수를 호출할 때, 실제로 전달되는 '값'
            * Positional Argument(위치 인자) : 인자의 위치에 따라 전달되는 인자
                ex) def Func(parm0, parm1):
            * Default Argument Values(기본 인자값) : 함수 정의 시에 parameter에 default 값을 할당하는 것
                ex) def Func(parm0, parm1 = 300):
            * Keyword Argument(키워드 인자) : 함수 호출 시에 이름과 함께 값을 전달하는 인자
                ※ 단, keyword argument는 positional argument 뒤에 위치해야 함
                ex) Func(parm1 = 100, parm0 = 200)
            * Arbitrary Argument List(임의의 인자 목록) : 정해지지 않은 개수의 인자를 tuple로 packing하여 처리하는 인자
                ex) def Func(*args):
            * Arbitrary Keyword Argument List(임의의 키워드 인자 목록) : 정해지지 않은 개수의 키워드 인자를 dict로 packing하여 처리하는 인자
                ex) def Func(**kargs):
                    Func(parm0 = 30, parm1 = 'function') >> {'parm0' : 30, 'parm1' = 'function'}
            ※ 권장 작성 순서 : positional - arbitrary - default/keyword - arbitrary keyword
            
            ※ Packing / Unpacking
                Packing : 여러 개의 데이터를 하나의 컬렉션으로 모아 담는 과정
                Unpacking : 컬렉션에 담겨있는 데이터를 개별 요소로 펼쳐 놓는 과정
                    - 함수 호출 시 사용되며 *를 통해 컬렉션을 위치 인자로, **를 통해 dict를 키워드 인자로 전달

- Recursive Function(재귀 함수) : 함수 내부에서 자기 자신을 호출하는 함수
    ※ 문제를 작은 단위의 문제로 분할하고 분할된 문제들의 결과를 조합하여 최종 결과를 도출하는 방법
    - 알고리즘 식의 변수 사용이 줄어들고 가독성이 증가함
    - 단, 메모리 사용량이 높고 속도가 느리며 종료 조건이 잘못되면 스택 오버플로우가 발생하거나 일부 경우에 가독성이 하락할 수 있음
    > 문제의 자연스러운(직관적인) 표현, 코드 간결성, 수학적 문제가 재귀적으로 표현되는 경우

- Built-in Function(내장 함수) : 파이썬이 기본적으로 제공하는 함수

- Scope
    - Global : 코드 어디에서든 참조할 수 있는 공간 (global variable)
    - Local : 함수 내부에서만 참조 가능한 함수가 만든 범위 (local variable)
    
    - variable 수명주기
        * built-in scope : 파이썬 실행 이후부터 영원히 유지
        * global scope : 모듈이 호출된 시점 or 인터프리터가 끝날 때까지 유지
        * local scope : 함수가 호출되며 생성되고 종료될 때까지 유지
    
    - variable name resolution rule (LEGB Rule)
    : local - enclosed - global - built-in > LEGB
        ※ outter scope의 variable에 접근은 가능하나 수정은 불가
        * global : 함수 내에서 변수의 scope를 전역 범위로 지정하기 위해 사용(전역 변수를 수정)
            ※ global 키워드 선언 전 사용 및 parameter에 global 키워드 사용 불가

람다 표현식 : 한 줄로 간단한 익명 함수를 정의 > map()의 logic으로 주로 사용
lambda (parameter): (return)
ex) lambda x, y: x + y
※ map(logic, target) : target의 각 요소에 logic 처리

            
단일 책임 원칙 : '하나의 객체는 하나의 명확한 목적과 책임만을 가진다.' (god object fail by itself)
    > 함수 설계 원칙
        1. 명확한 목적과 하나의 작업만을 수행
        2. 책임 분리
        3. 유지보수성


<실습>

Recursive function
- Base Case : 기저 조건
- Recursive Case : 유도 조건
"""