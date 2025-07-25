"""
[250723]

<Python 라이브 강의>

모듈 : 특정한 기능을 하는 변수와 함수를 모아 작성한 파이썬 파일
※ 내장 함수 help()를 이용하여 모듈 내에 무엇이 있는지 확인 가
- 내장 모듈 : 파이썬에 미리 작성해둔 모듈
ex) import module, from module import target, import module as AKA, from module import target as AKA
※ import문 : 모듈을 코드 내에서 사용하기 위해 가져오는 방법으로 '. 연산자'를 이용하여 같은 이름의 함수가 여러 모듈에 있을 때 충돌을 방지할 수 있음
※ from절 : 모듈에서 특정 요소만을 import하는 방법으로 정의된 모듈이 없으므로 명시적이지 않고 기선언한 요소와 겹칠 수 있음
    - double underscore로 시작하는 것을 제외한 모든 요소를 import하는 '* 표기'는 비권장
    ※ double underscore : 파이썬 내부적으로 사용하는 변수 혹은 함수 앞뒤에 표기
※ as절 : import하는 모듈에 별칭을 부여

- 사용자 정의 모듈


파이썬 표준 라이브러리(PSL) : 파이썬 언어와 함께 제공되는 모듈, 패키지의 모음
ex) math, os, sys, random
- Package : 연관된 모듈들을 하나의 디렉토리에 모아놓은 것
    - Python Style Guide : folder/file name은 소문자 + 언더스코어를 사용

    
파이썬 외부 패키지 : 'pip 명령어'를 이용하여 웹(ex. PyPi)에서 설치해서 쓰는 패키지
ex) requests : 파이썬에서 API를 통해 요청/응답을 쉽게 받을 수 있게 하는 패키지
- pip : pip install Package(연산자)(version)
ex) pip install package>=1.0.5
※ pip freeze > requirements.txt 명령을 기반으로 버전 정보 저장을 권장 (호환성 보장)


제어문 : 상황에 따라 코드를 제어하기 위한 문장
- 조건문 : 조건식의 검사는 순차적으로 진행

- 반복문
    - for문 : 반복 가능한 객체(iterable)의 요소들을 반복
        ※ Python Style Guide : 반복 변수의 경우, 단수형 명칭을 권장
        ※ Iterable : 요소를 하나씩 반환할 수 있는 모든 객체
        ※ Iterator : 값을 하나씩 꺼낼 수 있는 Stream을 가진 객체로 next()를 이용하여 다음 값을 생성할 수 있으나 한 번 소비하면 다시 사용이 불가함
            ★ 지연평가 : 메모리 효율성을 위하여 Iterator 패턴을 사용하여 값을 요청할 때마다 하나만 계산하여 반환
            ex) map 객체, range 객체, zip 객체
                ※ zip(*iterable) : 다수의 Iterable을 인자로 받아, 각 요소를 tuple로 묶어주는 Iterator를 반환
        * 비시퀀스 자료형의 경우, 반복 순서를 보장하지 않음
        * dict 자료형의 경우, 기본적으로 key를 반환
    - for-else : for 루프가 정상 종료되었을 경우, else 블록 동작 > 주로 검증 로직에서 활용

    - while문 : 조건식(탈출 조건)이 False가 나올 때까지 반복
    - while-else : while 루프가 정상 종료되었을 경우, else 블록 동작 > 주로 검증 로직에서 활용

    - 반복 제어
        - break : 해당 반복문을 탈출
        - continue : 해당 반복을 멈추고 다음으로 진행

※ pass : 아무 동작도 하지 않음을 명시적으로 표시하는 것으로 코드 틀을 유지하거나(빈 코드 블록이면 오류 발생) 이후의 작성을 위한 블록을 채우기 위함


내장 함수 enumerate(iterable, start=0)
: iterable 객체의 각 요소에 대해 index, value를 함께 반환


<실습>

dir() : 현재 코드 혹은 인자의 namespace를 반환

package도 module의 한 종류
"""