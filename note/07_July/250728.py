"""
[250728]

<Python 라이브 강의>

Data Structure(자료구조) : 여러 데이터를 효과적으로 사용, 관리하기 위한 구조로 프로그램의 성능, 효율성, 유지보수성에 큰 영향을 미침
- Sqenece
    - String
        * .find(x) vs .index(x) : x의 첫 번째 위치를 반환하되, 없을 경우 -1을 반환하거나 error가 발생하거나
        * .isalhpa() : 알파벳 뿐만 아니라 유니코드 상의 문자면 모두 True 반환
        * 문자열 조작 메서드 : 새로운 문자열 반환
            ex) .replace(old, new[, count]) : 바꿀 대상 글자를 새로운 글자로 바꿔 반환
                ※ [count] - 선택인자 (바꿀 개수)
            ex) .strip([chars]) : 문자열의 '시작'과 '끝'에 있는 지정한 문자를 제거
            ex) .split(sep=None, maxslpit=-1)
            ex) 'separator'.join(iterable) : iterable의 문자열을 연결하여 반환
    
    - List
        * .extend(m) : iterable m의 모든 항목을 리스트 끝에 추가
        * .pop() : 마지막 요소를 반환 후 제거
            ※ .pop(i) : i번째 요소를 반환 후 제거
        * .insert(i, x) : i번째에 요소를 삽입
        * .remove(x) : 첫 번째 x를 제거하되 없으면 error 발생

메서드 : 각 데이터 구조의 데이터를 효울적으로 조작하거나 특정 기능을 수행하기 위해 Class에 정의되어 객체에 속한 함수
※ Object(객체) : 특정 데이터와 그 데이터를 처리하는 기능을 하나로 묶은 것
- method chaining : 다수의 메서드를 연속하여 호출하는 방식
ex) method0().method1() == method0()_return.method1()
- 문자 유형 판별 method
ex) isdecimal() : 모두 숫자 문자로 이루어져 있어야 True 반환
ex) isdigit() : 유니코드 숫자(①)도 인식
ex) isnumeric() : 분수, 지수, 루트 기호 등 일부의 유니코드 문자들을 인식


변수 할당 : 새로운 객체를 생성하거나 기존 객체에 대한 참조를 생성
- 가변 : 참조하는 영역의 값을 변경하므로 깊은 복사를 하지 않으면 동일한 객체를 참조함
- 불변 : 새로운 객체를 생성하고 참조하므로 서로 다른 객체를 참조함
    ※ 성능 최적화
        * 가변 > 내용 수정이 빈번할 때, 기존 객체를 직접 수정
        * 불변 > 여러 변수가 동일한 객체를 안전하게 공유 (메모리 사용의 최소화)

복사
- 얕은 복사 : 객체의 '최상위 요소'만 새로운 메모리에 복사 (중첩된 객체는 그 객체의 참조를 복사)
    >> 1차원 리스트는 얕은 복사로 충분히 독립적인 복사본을 만들 수 있으나 중첩 리스트는 참조를 복사하므로 불가
    ex) list slicing, copy() 메서드, list() 함수
- 깊은 복사 : 객체의 '모든 수준의 요소'를 새로운 메모리에 복사
    >> 완전한 독립성 보장
    - copy.deepcopy(target)


Comprehension : Pythonic한 코드 (간결하고 효율적인 List/Dict 생성 방법)
※ Comprehension의 남용 금지 - "Simple is better than complex"
- List Comprehension
    ex) ls = [_ for _ in iterable if 조건]
    ※ List 생성법
    1. comprehension
    : 가장 pythonic하고 대부분의 경우 우수한 성능을 보임
    2. for loop
    : 일반적으로 가장 느리지만 크게 차이 나지 않고 복잡한 조건문, 예외 처리 등이 필요할 때의 유일한 선택지
    3. map
    : 내장 함수와 함께 사용하는 등의 특정 상황에서 가장 빠르나 일반적으로 comprehension과 유사한 성능을 보임
        ex) ls = list(map(lambda i: 0, range(10)))
- Dict Comprehension
    ex) dic = {key:val for key,val in (dictionary.items() or zip(iterable, iterable)) if 조건}



<실습>

method : OOP에서 객체가 갖는 행위
"""
