"""
[251118]

<JS 라이브 강의>

데이터 타입
- 원시 자료형 : 값 자체가 변수에 직접 저장되는 자료형으로 불변하며 변수 간 할당 시 값이 복사됨
    - number : 문자열 + 연산 시 자동으로 형 변환을 해주며 정수와 실수의 구분 없이 단일 타입으로 처리
        ※ NaN : Not a Number를 나타내는 값
    - string : + 연산을 통해 문자열 간 결합을 지원
        ※ Template Literals : Python의 f-string과 같은 기능을 제공하는 문자열 작성 방식으로, Backtick을 이용하여 여러 줄의 문자열 정의가 가능하며 그 내부에 ${}를 통해 변수 접근이 가능
    - boolean
        ※ 빈 object(ex. [], {})의 경우, 주소값을 보유하고 있기 때문에 true를 반환
    ※ null vs undefined
        : Null이 프로그래머가 의도적으로 값이 없음을 나타낸다면, Undefined는 아직 값이 할당되지 않음을 나타냄
        >> return이 없거나 인자가 전달되지 않은 매개변수에 대해서는 Undefined가 할당되며 산술 연산 시, Null은 0으로 취급되지만 Undefined는 NaN 값을 만듬

- 참조 자료형 : 데이터가 저장된 메모리의 주소가 변수에 저장되는 자료형으로 가변하며 변수 간 할당 시 주소가 복사됨
ex) object, array, function

연산자
- 할당 연산자 : 단축 연산자 지원
- 증감 연산자 : ++, --
- 비교 연산자
- 논리 연산자 : 단축 평가 지원
- 동등 연산자 == : 암묵적 타입 변환을 통해, 타입의 비교 없이 값만을 비교하며 피연산자가 모두 객체일 경우, 메모리의 같은 객체를 바라보는지 판별
- 일치 연산자 === : 값뿐만 아니라 타입까지 비교
- 삼항 연산자 : (condition) ? expression1 : exression2
- Null 병합 연산자 ?? : ES2020에 추가되었으며 대상이 null/undefined인지만을 확인
ex) let score = 0; score = score ?? 50; : score가 null/undefined일 경우에만 default value를 사용

반복문
- while
- for
- for ... in : 객체의 열거 가능한 속성의 키에 대한 반복 [객체에 대한 순회] >> 배열 순회 시 index 출력
ex) dictionary의 key를 순회
- for ... of : 반복 가능한 객체의 값에 대한 반복 [값에 대한 순회] >> dictionary와 같은 객체 순회 시 type error 발생

함수 : 참조 자료형에 속하며 모든 함수는 function object에 속함
- 선언식 : 함수는 호이스팅되며 코드의 구조와 가독성 면에서 장점을 가짐
    function NAME (PARAMETER){
        STATEMENTS

        return VALUE
    }

- 표현식 : 변수에 함수를 할당하는 방법으로 호이스팅 되지 않아 예측 가능성이 높고, 익명 함수로써 사용이 가능하여 유연성이 높으며 스코프 관리에 유리함
※ 익명 함수 : 이름 없이 필요할 때 즉시 만들어서 사용하는 일회용 함수
    const FUNCTION_NAME_변수명 = function() {
        STATEMENTS
    }

- 화살표 함수 표현식 : 함수 표현식의 간결한 표현법
    const FUNCTION_NAME_변수명 = (PARAMETER) => {return VALUE}

- 매개변수
    - 기본 함수 매개변수 : 함수 호출 시 인자 미전달 혹은 undefined 전달 시, 지정된 기본값으로 매개변수를 초기화하는 방법
        >> 그 외의 누락된 매개변수는 undefined로 할당
    - 나머지 매개변수 : 정해지지 않은 개수의 인자들을 배열로 모아서 전달하는 방법으로, 함수 정의 시 매개변수 앞에 ...(spread syntax)을 추가 (Python의 *과 동일)
        ※ Spread Syntax : 반복 가능한 항목들을 개별 요소로 펼치는 전개 구문으로 함수, 객체, 배열에서 각각 다르게 사용됨


<실습>


"""
