"""
[251106]

<DB 라이브 강의>

Decorator
- Allowed HTTP methods : view가 허용하는 HTTP 요청 방식을 제한하는 decorator로 보안을 강화하고 코드 역할을 명확히 분리할 수 있음
    ex) require_http_methods([_method_]), require_safe()_GET_HEAD_허용, require_POST()_POST_허용


ERD(Entity-Relationship Diagram) : DB 구조를 시각적으로 표현하는 도구로 시스템의 논리적 구조를 모델링하는 다이어그램
- Entity : DB에 저장되는 객체/개념으로 table로 표현
- Attribute : Entity가 가지는 고유한 데이터 항목으로 field로 표현
- Relationship : Entity 간 연관성으로 선으로 표현
    - Cardinality : Entity 간의 수적 관계를 나타내는 표현


<실습>


"""