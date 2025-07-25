'''
[250721]

<Python 라이브 강의>

In AI, Why Python?
- 압도적인 전문 라이브러리
- 쉬운 문법 높은 생산성
- 강력한 커뮤니티, 생태계

표현식(Expression)
: 하나의 값으로 평가될 수 있는 모든 코드
※ 평가 : 표현식을 계산하여 그 결과인 값을 만들어내는 과정
※ 값 : 표현식이 평가된 결과로 더 이상 계산되거나 평가될 수 없는 프로그램의 가장 기본적인 데이터 조각
※ 모든 값은 그 자체로 가장 단순한 형태의 표현식이지만 모든 표현식이 값은 아니다.

변수 (Variable) - 특정 객체를 가리키는(pointer, reference) 이름표
: 값을 재사용하기 위해 저장한 이름이 붙은 공간
※ 영문 알파벳, 언더스코어, 숫자로 구성되되, 숫자로 시작할 수 없음
※ 내부 예약어는 변수로 사용 불가

할당 (Assignment)
: 표현식이 만들어낸 값을 변수에 저장하는 과정

객체 (Object) - vlaue + type + address를 가지고 있는 모든 데이터의 실체
: 데이터와 그 데이터와 관련있는 알고리즘을 묶어 놓은 것
- 데이터 : 멤버 변수, 변수
- 알고리즘 : 멤버 메서드, 메서드
※ heap : 객체를 저장하는 메모리 영역

문장 (Statement)
: 동작을 지시하는 실행 가능한 코드의 최소 단위
※ 값이 남으면 표현식, 남지 않으면 문장

Style Guide (PEP 8)
: 코드 일관성, 가독성을 위한 규칙 및 권장 사항의 모음
ex) 직관적인 변수명
ex) 공백 4칸을 이용한 들여쓰기
ex) 한 줄의 길이를 79자로 제한하며 그 이상은 줄바꿈 사용
ex) 문자와 밑줄을 사용하여 함수, 변수, 속성명 작성
ex) 함수 및 클래스 정의 등의 블록 사이에는 빈 줄을 추가

주석 단축키 : ctrl + /

Type - '피연산자 + 연산자'로 구성

Data Type
: 값의 종류와 그 값으로 할 수 있는 연산을 결정하는 속성
- Numeric Type : int, float, complex
※ 지수 표현법 : 아주 크거나 작은 실수를 간결하게 표현하기 위한 방식
ex) 1.23e4 == 1.23 * 10^4
※ 부동 소수점의 반올림 오차 (유한 정밀도 - 연산 과정의 오류 발생)
: 2진법 사용으로 인해 무한 소수가 발생하므로 근사값을 저장함
    - Decimal 모듈 : 실수를 10진수로 연산하여 정확한 값을 제공

- Sequence Type : str, list, tuple, range
※ Sequence : 여러 데이터가 정해진 순서대로 일렬로 늘어선 자료 구조
    - 공통 특징
    1. 순서 (정렬 X)
    2. 인덱싱
    3. 슬라이싱 : 설정된 범위의 값을 새로운 sequence로 반환
    ex) list[start:end:step]
    ※ 단, end는 포함하지 않음
    4. 길이
    5. 반복 : 반복문을 이용하여 순회 가능

    - str "" : 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형
        * f-sting : 문자열 보간법
        ex) f'안녕하세요, 제 이름은 {name}이고 나이는 {age}살입니다.'
        * 불변성(Immutable) : 생성 이후 상태나 값을 변경할 수 없음 (재할당 != 변경) 
        
- Non-Sequence Type : set, dict

- 기타 : bool, function, none


<실습>

Git lab : privit Git server
- lab.ssafy.com || project.ssafy.com > link

Clone pw : ja2025!!

VS Code
- ctrl shift p : 명령 팔레트 열기

파이썬 인터프리터 : python.exe (실행 파일)
- Windows 한정, py.exe 파일이 존재 (명령어, python >> py || python.exe를 환경변수_Path에 등록)

git pull > local에 추가적인 변경이 있으면 에러가 난다? >> 확인 필요

'''