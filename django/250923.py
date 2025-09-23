"""
[250923]

<Django 라이브 강의>

Design Pattern
ex) MVC
    - Model : 데이터 및 비즈니스 로직
    - view : 사용자에게 보이는 화면
    - controller : 사용자의 입력을 받아 model, view를 제어
ex) MTV
    - Model : 데이터 및 비즈니스 로직으로 DB와 Python 객체로 추상화된 형태로 상호작용
        * Model Class : DB 테이블을 정의하고 데이터를 조작할 수 있는 기능 제공 (1 Class == 1 Table, APPNAME_CLASSNAME)
            - Model Field : DB 테이블의 column(field)를 정의하고 데이터 타입 및 제약 조건 명시
            ex) data = models.Field_Types(Field_Options)
                * Field_Types : models 모듈의 클래스로 정의되어 있으며 데이터 종류를 정의함
                ex) CharField : 제한된 길이의 문자열 저장
                ex) TextField : 길이 제한 없는 대용량 문자열 저장
                * Field_Options : 필드의 동작 및 제약 조건 정의
                ex) null : Null 값 허용 여부 (default : False)
                ex) blank : form에서 빈 값 허용 여부 (default : False)
                ex) default : 필드의 기본값을 설정

        * Migrations : Model Class의 변경사항을 DB에 최종 반영하는 방법
            - python manage.py makemigrations : migration file 생성
            - python manage.py migrate : 생성된 migration file을 기반으로 DB에 반영

        ※ record가 존재하는 시점에서 새로운 field를 추가할 경우, 기존 record의 해당 field에 대한 기본값 설정이 필요
            1. model class 수정
            2. makemigrations
                2-1. Django의 추천 값을 사용 혹은 대화창에서 직접 기본값을 작성
                2-2. model.py에서 기본값 작성
            3. migrate

Admin site
- Admin Interface : Django에서 자동으로 제공하는 인터페이스로 DB 모델의 CRUD(생성, 읽기, 업데이트, 삭제) 작업을 간편하게 수행 가능하고 프로토타이핑, 비개발자 데이터 관리, 내부 시스템 구축을 도움
- python manage.py createsuperuser : 관리자 계정 생성
※ admin.py에 생성한 model을 등록해야 admin site에서 확인 가능


<실습>


"""