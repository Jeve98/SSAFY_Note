"""
[251119]

<JS 라이브 강의>

Object : key로 구분된 데이터 집합을 저장하는 자료형 (Python의 Dictionary)
※ property의 key는 문자형만 허용하며 value는 모든 자료형을 허용
- . 표기법, [] 표기법으로 property에 접근 가능하며, [] 표기법의 경우 변수를 통한 접근을 허용
- in 연산자 : 특정 key가 property에 존재하는지 확인하는 연산자로, 프로토타입 체인에 따라 상속된 속성까지 확인하므로 hasOwn() 사용을 권장

- Method : Object 내부에 선언된 함수로 본인이 속한 Object의 다른 property에 접근이 가능함
    FUNCTION_NAME : function(){}
    ※ 일반 함수에서의 this 단순 호출 : 전역 객체
    ※ 객체에서의 메서드 this 호출 : 메서드를 호출한 객체

- 추가 객체 문법
    - 단축 속성 : key name과 value로 사용하는 변수의 이름이 같을 경우 하나로 생략 가능
    - 단축 메서드 : 메서드 선언 시 function 키워드 생략 가능
        FUNCTION_NAME(){}
    - 계산된 속성 : [key]로 선언된 property로, key를 고정된 값이 아닌 변수 값으로 사용
    - 구조 분해 할당 : 배열 또는 object를 분해하여 property를 변수에 쉽게 할당할 수 있는 문법
        {KEY_NAME} = OBJECT_NAME
    - 객체와 전개 구문(Spread Syntax) : 얕은 복사를 통해 객체 내부의 property를 전개하여 활용하지만 항상 새로운 배열을 생성하므로 깊은 복사의 효과를 만듬
    - Optional Chaining : 속성 없는 중첩 객체에 접근할 때 에러 발생 없이 안전하게 접근하는 방법으로 에러 발생 대신 undefined를 반환하며 없어도 괜찮은 대상에게만 사용을 권장
        OBJECT.TARGET_PROPERTY_?.

- JSON
    - JSON.stringfy() : Object -> JSON
    - JSON.parse() : JSON -> Object


Array
- Array Helper Methods : ES6에 추가된 배열 조작을 돕는 메서드로 각 요소에 대해 콜백함수를 호출
    * forEach() : 배열 내 모든 요소에 대해 콜백 함수를 호출하며 반환 값은 없음
        ARRAY.forEach(function (처리할_요소의_임시_이름, [index], [원본_array]){STATEMENT})
        ※ forEach의 인자로 전달된 콜백 함수는 일반 함수로 호출
        >> 화살표 함수를 콜백 함수로 사용하는 것으로 메서드 내에서의 this 호출처럼 변경 가능

    * map() : 배열 내의 모든 요소에 대해 콜백 함수를 호출하며 그 결과를 모아 배열로써 반환
        ARRAY.map(function (처리할_요소의_임시_이름, [index], [원본_array]){STATEMENT})

    * reduce() : 각 요소에 대해 콜백 함수를 호출하며 배열을 원하는 특정 형태의 값으로 변환하여 반환

    ※ 콜백 함수 : 다른 함수에 인자로 전달되는 함수


Class : 객체를 생성하기 위한 템플릿


<실습>


"""
