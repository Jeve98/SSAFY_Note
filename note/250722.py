"""
[250722]

<Python 라이브 강의>

Data Type
- Sequence Type : str, list, tuple, range
    - list [] : 여러 개의 값을 순서대로 저장하는 변경 가능한(mutable) 시권스 자료형
        ※ 가변성(Mutable) : 생성 이후에도 값을 변경(수정, 추가, 삭제)할 수 있는 성질
        ※ Nested List (중첩 리스트)
        ※ List Comprehension : tmp = [[0 for _ in range(3)] for _ in range(10)]

    - tuple () : 여러 개의 값을 순서대로 저장하는 변경 불가능한 시권스 자료형
        * 불변성을 이용하여 파이썬의 내부 동작과 안전한 데이터 전달에 사용 (안정성과 무결성의 보장)
        ※ 소괄호 없이 쉼표로도 생성 가능
        ※ 단일 요소 튜플의 경우, 반드시 후행 쉼표 필요
            Trailing Comma : Collection의 마지막 요소 뒤에 붙는 쉼표로 일반적으로 선택사항이나 단일 요소 tuple 생성 시에만 필수적
            ※ Python Style Guide : 사용 시에는 각 요소 간 줄바꿈 이용 권장

    - range : 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형
        * 생성된 숫자를 메모리에 저장하는 대신, '시작 값, 끝 값, 간격'이라는 규칙을 사용하여 메모리를 효율적으로 사용
            : 형변환 필요
            ex) range 객체로 반환 - print(range(5)) >> range(5)
            ex) list로 반환 - print(list(range(5))) >> [0, 1, 2, 3, 4]

- Non-Sequence Type : set, dict
    - set {} : 순서와 중복이 없는 변경 가능한 자료형 (수학의 집합과 동일한 연산 처리)
        ※ dict 자료형과의 혼동을 피하기 위해, 빈 set 자료형 생성 시에 반드시 set() 함수 사용

    - dict {} : 'Key: Value'쌍으로 이뤄진 순서와 중복이 없는 변경 가능한 자료형
        ※ Key : 중복 불가, 변경 불가한 자료형만 사용 가능, 존재하지 않는 Key에 접근 시 에러 발생
        ※ 주로 API에서 dict 형태로 Key 제공

- 기타 : boolean, function, none
    - None : '값이 없음'을 표현한 데이터 타입 >> "값이 아직 정해지지 않음"

    - boolean : True / False

※ collection : 다수의 값을 하나로 묶어 관리하는 자료형의 통칭
ex) str, list, tuple, range, set, dict

※ Mutable / Immutable
- Mutable : 변경 가능, 유연성, 효율성 (list, dict, set)
    > 각각의 배열이 메모리 주소를 pointing
    ex) a[2] >> address0( > value), address1( > value)
- Immutable : 변경 불가, 안전성, 예측 가능 (str, tuple, range)
    > pointing 중인 메모리 자체에 값이 저장
    ex) str"value" >> address("value")


형변환
- 암시적 : 파이썬이 연산 중에 데이터 손실을 방지하기 위해 자동으로 데이터 타입을 변환
※ Boolean과 Numeric Type만 가능
- 명시적 : 개발자가 변환하고 싶은 타입을 직접 함수로 지정하여 변환
※ dict 자료형의 경우, str을 제외하고 Key값만 변환


연산자
- 산술 연산자
- 복합 연산자 : 연산과 할당을 동시에 진행
※ python style guide : 코드 축약 < 높은 명시성
- 비교 연산자
    - == : 동등성, 값이 같은지를 비교
    - is : 식별성, 객체 자체(정체성)이 같은지를 비교 (메모리 주소가 같은지를 확인)
        * 통상적으로 Singleton 객체를 비교할 때 사용
        ※ Singleton 객체 : 파이썬 전체에서 단 하나의 객체만 생성되어 재사용되는 특수 객체로 다수의 변수가 해당 값을 지녀도 단 하나의 객체를 pointing
        ex) None, True, False
- 논리 연산자
※ 단축 평가 : 코드 실행의 최적화를 위해 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작
ex) result = True or False, or 연산자 이후의 피연산자는 평가하지 않고 결과를 결정
- 멤버십 연산자 : 특정 값이 Collection 안에 포함되어 있는지 확인하는 연산자
- 시퀀스형 연산자 : 시퀀스형 자료형에서 특별한 의미로 사용되는 연산자
    - + (결합 연산)
    - * (반복 연산)


<실습>
range : 함수(생성자)로 range 타입의 객체를 생성

복사가 아닌 것 / 얕은 복사 / 깊은 복사
- '복사'의 확인 : 객체의 주소값을 확인
ex) id(target)
- 얕은 복사 : 중첩 리스트에서 중첩된 리스트가 pointing 하는 주소가 동일
ex) tmp = target.copy()
ex) target = [1, 2, [1, 2]] > address0, target[2] > address1
ex) tmp = target.copy() > address2, tmp[2] > address1
- 깊은 복사 : copy 모듈의 deepcopy() 함수를 사용하여 중첩된 리스트도 별도로 복사
ex) import copy, tmp = copy.deepcopy(target)

set type은 hash를 이용하여 중복을 검사
※ hash()를 통해 hash 확인 가능
"""