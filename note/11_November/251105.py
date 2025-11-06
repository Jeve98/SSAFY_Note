"""
[251105]

<DB 라이브 강의>

1:1 relation : 한 table의 record는 다른 table의 한 record와 연결
N:1 relation : 한 테이블의 0개 이상의 record가 다른 table의 하나의 record와 연결
N:M relation : 다수의 record가 다수의 record와 연결된 것으로 중간 table을 사용해 구현

외래키 : 통상적으로 N의 위치에 생성되어 1에 해당하는 table의 primary key를 사용
- .ForeignKey(reference_class, on_delete) [Django]
    * on_delete 속성
        - CASCADE : 참조 된 부모 객체 삭제 시, 이를 참조하는 모든 자식 객체 삭제
        - PROTECT : 부모 객체 삭제 불가
        - SET_NULL : 부모 객체 삭제 시, 해당 field 값이 null로 지정
    
    ※ 서로 다른 app의 model을 참조하는 경우, 특정 클래스 생성 시점을 보장할 수 없으므로 직접 import 하는 것이 아니라 settings의 값을 이용함
        ex) user

- 일반적으로 외래키를 보유하고 있지 않은 table의 역참조는 어렵기 때문에 related manager[className_set]를 통해 두 table을 join하여 역참조 실행
※ 참조 : 직접 대상의 정보를 저장하고 필요할 때 활용하는 것
※ 역참조 : 누가 나를 참조하는지 거꾸로 조회하는 것


<실습>

역참조의 경우, html에서도 동작
"""