"""
[251110]

<DB 라이브 강의>

N:M Relationships : 한 table의 0개 이상의 record가 다른 table의 0개 이상의 record와 관련된 경우
- 중개 모델 : 제 1 정규화를 만족시키고 N:M 관계의 두 모델을 연결하는 모델로 각 table에 대한 외래키를 보유
    ※ 제 1 정규형 : table의 모든 칸에는 더 이상 쪼갤 수 없는 하나의 값만이 존재
    <Django>
    - ManyToManyField() : OOP의 관점에서 각 객체(Table)이 중심이 되기 위해, 중개 모델이 관계를 형성하지 않고 각자 생성할 수 있도록 표현하는 방법으로 중개 table에 대한 정의가 필요 없음
        ex) models.ManyToManyField(Target_Model)
        * .add() : 관계 추가 [object.model.add() || object.model_set.add()]
        * .remove() : 관계 삭제 [object.model.remove() || object.model_set.remove()]
        
        >> 단 추가 정보를 구성할 수 없으므로 추가 정보가 필요한 경우, 중개 table을 정의한 뒤 through 속성을 사용
            ex) models.ManyToManyField(Target_Model, through='중개테이블')
            * .add() : 관계 추가 및 추가 필드값 제공 [object.model.add(through_defaults={'field': 'data', })]
        
        ※ 속성
        - through : 추가 데이터를 중개 모델에 지정
        - related_name : 역참조 시, 사용하는 manager name을 변경
        - symmetrical : 관계 설정 시, 생성된 데이터의 대칭 유무 설정 (default : True)

    
<실습>


"""