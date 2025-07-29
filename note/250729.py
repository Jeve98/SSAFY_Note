"""
[250729]

<Python 라이브 강의>

Data Structure(자료구조)
- None Sqenece
    - Dictionary
        ※ 해시 테이블을 이용하므로 삽입, 삭제, 검색이 데이터 크기와 관계 없이 매우 빠름
            > Key는 hashable한 고유의 값이어야 함
        * .get(key[, value]) : key와 연결된 값을 반환, key가 존재하지 않으면 None/value를 반환
            ※ 일반적인 접근 방식(dic[key])의 경우, key가 존재하지 않을 경우 error 발생
        * .keys() : key를 모은 객체를 반환
            ※ 반환되는 객체는 실시간으로 동기화되는 view 객체로 Dictionary에 변화가 생길 경우 이를 추적해서 출력
        * .values() : value를 모은 객체를 반환
        * .items() : key, value를 tuple 형태로 모은 객체를 반환
        * .pop(key[, default]) : key를 제거하고 연결된 value를 반환, key가 존재하지 않으면 error 발생 혹은 default를 반환
        * .clear() : 모든 key/value 쌍을 제거
        * .setdefault(key[, default]) : key와 연결된 value를 반환, key가 존재하지 않으면 default와 연결하여 추가하고 default를 반환
        * .update([other]) : other가 제공하는 key/value 쌍으로 Dictionary를 갱신하고 기존 키는 덮어씀

    - Set
        ※ 해시 테이블을 이용하여 고유성을 효율적으로 보장하며 속도가 매우 빠름
        * .add(x)
        * .update(iterable) : iterable 요소를 추가
        * .clear()
        * .remove(x) vs .discard(x) : x를 제거하되 없을 경우 error 발생하거나 아무런 변화가 없거나
        * .pop() : 임의의 항목을 반환하고 해당 항복을 제거
            ※ random X : 임의는 맞으나 무작위는 아님
            > bucket 위치에 따라 반환
            "Arbitary don't mean Random"
        * 집합 연산 메서드
            ex) .difference() or - : 차집합
            ex) .intersection() or & : 교집합
            ex) .issubset() or <= : 부분집합
            ex) .issuperset() or >= : 전체집합
            ex) .union() or | : 합집합

Hash Table : key와 value를 짝지어 저장하는 자료구조로 key를 해시 함수를 통해 hash value로 변환하여 index처럼 사용
Hash : 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
※ 가변 객체는 기본적으로 해시가 불가능
: 값이 변하면 Hash value도 함께 변할 수 있어, Hash Table의 무결성을 해침
    - Hashable 객체
        : Hash Table 기반 자료구조에 사용, 불변성을 통한 일관된 해시값이 제공하는 무결성, 안정성 및 예측 가능성 유지
- Hash function : 인터프리터 시작과 함께 설정되는 난수 시드와 임의 길이 데이터를 입력 받아 고정 길이 정수로 변환해주는 일방향 함수
    ※ 정수 값은 해시 값이 숫자 자기 자신과 동일하거나 단순 계산으로 고정
    ※ 문자열은 해시 난수화가 적용되어 매 실행마다 다른 bucket에 위치
- Hash value : Hash function의 결과로써 나온 고정 길이 정수
- Buckets : Hash value에 대응하여 Hash Table 내부에 존재하는 저장 장소
    ※ bucket의 위치가 요소의 위치를 결정하므로 순서는 보장하지 않음


EBNF 표기법 : BNF를 확장한 표기법으로 서로 다른 프로그래밍 언어, 데이터 형식, 프로토콜 등의 문법을 통일하여 정의
- [] : 선택적 요소
- {} : 0번 이상 반복
- () : 그룹화


<실습>

bit mask in hash : target & (bucket size - 1)
"""