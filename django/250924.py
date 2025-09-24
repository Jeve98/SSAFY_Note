"""
[250924]

<Django 라이브 강의>

ORM(Object-Relational-Mapping) : 객체 지향 프로그래밍 언어의 객체와 DB의 데이터를 매핑하는 기술로 개발자 친화적인 DB 인터페이스
>> DB 추상화를 통한 생산성 향상 및 객체 지향적 접근이 가능함

- in Django) QuerySet API : DB의 SQL 쿼리문을 python 코드로 다룰 수 있게 해주는 번역 API
    >> Django -> (QuerySet API) -> DB -> (QuerySet-다중 || Instance-단일) -> Django

    - python manage.py shell : QureySet API 사용을 위해 Django shell로 입장

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

    * 구조 : Model_Class.Manager(objects).QuerySet_API_Method

    * in view function
    
Ipython : 자동 완성과 같은 편리한 작업환경을 제공하는 도구
- pip install ipython


<실습>


"""