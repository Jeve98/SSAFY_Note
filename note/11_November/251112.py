"""
[251112]

<DB 라이브 강의>

API(Application Programming Interface) : sw 간의 통신을 매개하는 메커니즘

REST(Representational State Transfer) : API 서버 개발을 위한 sw 설계 방법론
- RESTful API : REST 설계 디자인 원리에 따라 자원을 정의하고 자원에 대한 주소를 지정하여 작성한 API

- 자원의 식별 : URI
    ※ URI(Uniform Resource Identifier) : 통합 자원 식별자
        - URL(Uniform Resource Locator) : 통합 자원 위치
            <Scheme>http :// <Domain_Name>www.@.@ / <Port>80 / <File_Path>/path/to/file.html ? <Parameter>key=value # <Anchor>SomeWhereInTheDocument
            * Scheme : 일반적으로 http 사용, 메일을 위한 mailto, 파일 전송을 위한 ftp 등이 존재
            * Domain Name : IP 주소를 대체하는 이름 (w.DNS)
            * Port : HTTP_80, HTTPS_443을 표준으로 사용하며 표준 포트만 작성 시, 생략 가능
            * File Path : 과거에는 파일의 물리적 위치를 표기했으나 현대에는 추상화된 구조를 표현
            * Parameter : '&'로 구분되는 key-value 쌍으로 웹 서버에 제공하는 추가적인 데이터
            * Anchor : 위치에 대한 북마크 역할을 하는 브라우저의 특정 지점에 있는 콘텐츠로, 서버에 전송되지 않으며 브라우저가 이를 해석하여 이동

- 자원의 행위 : HTTP Request Methods (GET, POST, ...)
    - HTTP Request Methods
        * GET : 서버에 리소스의 표현을 요청 (검색)
        * POST : 데이터를 지정된 리소스에 제출, 서버 수정을 요청
        * PUT : 요청한 주소의 리소스 전체를 수정 (partial=False - Default)
        * PATCH : 요청한 주소의 리소스 일부를 수정 (partial=True)
        * DELETE : 지정된 리소스를 삭제
    - HTTP Response Status Codes
        * 100 : 요청 진행 중
        * 200 : 요청의 정상 처리
        * 300 : 요청한 리소스가 다른 위치로 옮겨졌을 경우
        * 400 : 클라이언트 요청에 문제 발생
        * 500 : 서버 내부 문제로 요청 처리 실패

- 자원의 표현 : JSON 데이터 권장 (데이터 결과물)
    ※ 서버의 변화 : SSR(Server-Side Rendering) > REST API Server

>> 자원을 중심으로, 동작을 명확하게 구성하고 응답을 일관된 포맷으로 제공할 수 있도록 설계


DRF(Django REST Framework) : Django에서 RESTful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- Serialization [직렬화] : 여러 시스템에서 활용하기 위해 데이터 구조, 객체 상태를 재구성할 수 있는 포맷으로 변환하는 과정
    - Serializer : 직렬화를 통해 serialized data를 반환해주는 클래스
    - ModelSerializer : Django Model과 연결된 Serializer 클래스
        ※ MTM 관계에서 save 이전에 외래키에 대한 검증이 진행되어 문제가 발생하므로 해당 field에 read-only 설정을 해줌
        ※ read_only_fields : 클라이언트의 직접 수정이 불가하고 서버 로직에 의해 자동 생성/관리되는 응답 전용 field로, 입력은 받지 않으나 정보를 제공하는 경우 혹은 새로운 field 값을 생성하여 제공하는 경우에 사용
        
        - Nested Relationships : 역참조한 값을 직렬화하기 위해서 명령어로만 존재하는 역참조 매니저를 serializer class 내부에서 새로운 fields로 선언하며, 이때 역참조 대상에 대한 serializer class로 할당

        - 신규 field 추가 : views에서 annotate(improve query)를 활용하여 새로운 field를 추가한 뒤, 집계함수로 계산한 값을 할당하고 serializer에서 SerializerMethodField로 인스턴스 정의 및 해당 인스턴스에 값을 할당하기 위해 get_instance_name 함수를 생성
            ex) num_of_commnets = serializer.SerializerMethodField(), def get_num_of_commnets(self, obj): return obj.num_of_commnets
                ※ obj : 직렬화 class에서 사용하는 model을 의미

                
※ get_object_or_404(model, pk) : 단일 객체 조회 시, 없는 데이터에 접근에 대한 오류 코드를 500 대신 404로 변경
※ get_list_or_404(model, pk) : 전체 조회 시, 없는 데이터에 접근에 대한 오류 코드를 500 대신 404로 변경


API 문서화
- OAS(OpenAPI Specification) : RESTful API를 설명하고 시각화하는 표준화된 방법
    - Swagger / Redoc : 오픈소스 프레임워크 [pip install drf-spectacular, settings.py에 등록]
        

<실습>

Social Login : Django-allauth
"""