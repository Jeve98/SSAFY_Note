"""
[250920]

<Django 라이브 강의>

ORM(Object-Relational-Mapping) >> DB 추상화를 통한 생산성 향상 및 객체 지향적 접근이 가능함
- in Django) QuerySet API
    - python manage.py shell : QureySet API 사용을 위해 Django shell로 입장
    
    - 구조 : Model_Class.Manager(objects).QuerySet_API_Method
    ※ QuerySet : Django ORM을 통해 만들어지는 자료형으로 DB로부터 전달받은 객체 목록이자 순회가 가능한 1개 이상의 데이터
    ※ Query : DB의 특정 데이터에 대한 요청
        - CRUD : 생성, 조회, 수정, 삭제
            * Create
                1. 빈 객체 생성 후 값 할당 및 저장
                    Instance_Name = Class_Name()    # instance 생성
                    Instance_Name.variable = Data   # instance variable에 데이터 할당
                    Instance_Name.save()            # 할당한 값을 기반으로 DB 저장
                2. 초기값과 함께 객체 생성 및 저장
                    Instance_Name = Class_Name(variable=Data)   # instance에 데이터를 할당한 채로 생성
                    Instance_Name.save()                        # 할당한 값을 기반으로 DB 저장
                3. create() 메서드로 한 번에 생성 및 저장
                    Class_Name.objects.create(variable=Data)    # instance 생성 없이 바로 DB에 데이터 생성

            * Read
                1. QuerySet 반환
                    - Class_Name.objects.all()
                    - Class_Name.objects.filter(parameter 기반 조건) : 조건을 만족하는 데이터가 없어도 동작
                2. instance 반환
                    Class_Name.objects.get(parameter 기반 조건) : 조건을 만족하는 데이터가 없거나 다수 조회시 에러 발생
                    >> 고유성을 보장하는(식별자) 조회
                ※ Field lookups : 단순 동치 비교를 넘어 더 상세한 조건으로 데이터를 조회할 수 있는 기능
                    Class_Name.objects.filter(변수__조회조건=조건)

            * Update
                1. 조회 > 변경 > 저장
                    Instance_Name = Class_Name.objects.get(pk=target)   # 조회
                    Instance_Name.variable = Data                       # instance variable 데이터 변경
                    Instance_Name.save()                                # 변경한 값을 기반으로 DB 업데이트
            
            * Delete
                1. 조회 > 삭제
                    Instance_Name = Class_Name.objects.get(pk=target)   # 조회
                    Instance_Name.delete()                              # 대상 데이터 반환하며 삭제

    - in view function


HTTP request methods : 데이터에 대해 수행을 원하는 작업을 나타내는 것
※ HTTP : 네트워크 상에서 resource를 주고 받기 위한 프로토콜
- GET : 조회를 위한 메서드로 브라우저 히스토리에 저장되고 캐싱이 가능하지만 URL에 데이터가 노출되고 URL 최대 길이에 따라 데이터 길이가 제한되며 텍스트를 제외한 데이터의 전송이 불가함
- POST : 데이터 생성/전송을 위한 메서드로 요청 본문에 데이터가 포함되어 URL을 통한 노출이 없음
    > 서버 상태 변경을 위한 요청이므로 form 태그 내부에 CSRF Token이 필수적으로 필요
    
    ※ 저장 후, 페이지 응답은 POST 요청에 대한 적절한 응답은 아님
        - 기술 : POST 요청은 데이터 생성/변경에 사용되며 동일 요청이 반복되면 안됨
        - UX : 후속 행동 유발로 예기치 않은 동작 발생 가능
        >> Redirect : 서버가 클라이언트를 직접 다른 페이지로 보내는 것이 아닌 클라이언트가 GET 요청을 다시하도록 유도
    
    * CSRF(Cross-Site-Request-Forgery) : 일반 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행동을 요청하게 만드는 해킹 방식
    1. 일반 사용자의 정상 로그인 > 세션 발급
    2. 해커의 미끼 링크에 접속
    3. 미끼 링크의 숨겨둔 요청을 발급된 세션과 함께 전송
    >> CSRF 토큰을 기반으로 방어
        1. 서버 측에서 페이지 전송 시, 토큰을 포함하여 전송
        2. 해당 페이지에서 요청 전송 시, 해당 토큰이 포함되어 전송
        3. 토큰 인증 >> 위조 사이트, 정상적이지 않은 요청에 대한 방어

HTTP response status code : 서버가 클라이언트의 요청에 대한 처리 결과를 나타내는 3자리 숫자로
ex) 403_Forbidden(권한에 의한 거절), 404_Notfound(요청받은 페이지 없음)


<실습>


"""