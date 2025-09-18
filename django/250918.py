"""
[250918]

<Django 라이브 강의>

Web Application(Web Service) : 인터넷을 통해 사용자에게 제공되는 서비스

Server-Client Structure
- Client : 서비스를 request하는 주체
- Server : client의 request에 response하는 주체

- Frontend : UI 구성 및 사용자의 상호작용을 위한 구현
    ex) HTML, CSS, JavaScript, frontend framework(Veu, React, ...)
- Backend : request에 대한 처리 및 DB와의 상호작용 구현
    ex) 서버 언어, backend framework(Django, spring, ...), DB, API, 보안
※ Framework : 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공하는 도구


가상환경 : 하나의 컴퓨터 내부에 또 다른 독립된 환경
- 생성
    python -m venv(디렉토리-변경불가) venv(가상환경명) : 현재 디렉토리 내부에 venv 폴더 생성후 venv 이름의 가상환경 생성
- 활성화
    source venv/Scripts/activate
    (source venv/bin/activate - 리눅스/mac)
    
    ※ 가상환경 전부를 공유하지 않고(.gitignore) 의존성 기록, 'requirements.txt'만을 공유
    pip install -r requirements.txt
- 종료
    'terminal shut-down' or deactivate

의존성 : 하나의 sw가 동작하기 위해 필요로 하는 다른 sw, 라이브러리
- 의존성 패키지 : 프로젝트가 의존하는 개별 라이브러리
    - 확인
        pip list : 설치된 라이브러리 목록 출력
    - 의존성 기록
        pip freeze > requirements.txt : 설치된 모든 패키지를 버전과 함께 특정한 형식으로 출력

        
Django : Python 기반의 대표적인 web framework로 Spotify, Instagram, Dropbox 등 대규모 트래픽 서비스에서도 안정적인 서비스를 제공 중
- 다양성, 확장성, 보안, 커뮤니티 지원

- 생성
    pip install django : django 설치
    django-admin startproject firstpjt(프로젝트명) .(현재 디렉토리 기준) : 현재 디렉토리에 django project 생성
- 서버 실행
    python manage.py runserver
    ※ manage.py : django 관련 명령어 제공 파일
- 서버 종료
    'ctrl C'

- Project && App : 1개의 project 내에 각각의 독립적인 기능을 담당하는 모듈로써 App이 다수 존재
    1. 생성
        python manage.py startapp articles(복수형 이름으로 작성 권장) : 프로젝트 내에 app 생성
    2. 등록 : Django의 내부 구동 순서를 고려하여 사용자 생성 app은 상단부터 작성하는 것을 권장
        settings.py - INSTALLED_APPS에 추가
        
※ PROJECT 구조
    - settings.py : 프로젝트의 모든 설정을 관리
    - urls.py : 요청 들어오는 URL에 따라 해당하는 views를 연결
    - __init__.py : 해당 폴더를 패키지로 인식하도록 설정
    - asgi.py : 비동기식 웹 서버와의 연결 설정
    - wsgi.py : 웹 서버와의 연결 설정
    - manage.py : 프로젝트와 상호작용하는 CLI 유틸리티

※ APP 구조
    - templates 디렉토리 : template이 저장되어 있는 디렉토리로 templates 이름을 필수로 지니며 위치한 app 이름을 아래 디렉토리 구조로 지님
    - admin.py : 관리자 페이지 설정
    - models.py : MTV의 model을 정의
    - views.py : MTV의 view를 정의 (view 함수를 통해 요청을 처리하고 요청에 대한 응답 반환)
        * 모든 view 함수는 첫 번째 인자로 request 객체를 필수적으로 받음
            ex) def fuction(request): return render(request, template_path)
    - apps.py : 앱 정보
    - tests.py : 프로젝트 테스트 코드 작성

>> 요청 - urls.py - views.py - models.py / templates - views.py - 응답
    ※ 구현 순서 역시 위 순서를 맞추는 것을 권장 (디버깅 편의성)


Design Pattern : sw 설계에서 반복적으로 발생하는 문제에 대한 검증되고 재사용 가능한 일반적인 해결책이자 관행
ex) MVC : 하나의 어플리케이션을 구조화하는 대표적인 구조적 디자인 패턴으로 Model, View, Controller로 구분됨
    - Model : 데이터 및 비즈니스 로직
    - view : 사용자에게 보이는 화면
    - controller : 사용자의 입력을 받아 model, view를 제어
ex) MTV : Django에서 어플리케이션을 구조화하는 디자인 패턴으로 Model, Template(== View), View(== Controller)로 구분됨 (명칭만 다르게 정의)


<실습>


"""