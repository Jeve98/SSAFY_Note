"""
[250919]

<Django 라이브 강의>

Django
- Template System : 파이썬 데이터(Context)를 HTML 문서(Template)와 결합하여 로직과 표현을 분리한 채 동적인 웹페이지를 생성하는 도구
    >> 동일한 구조(Template)를 가진 다른 내용(Context)의 페이지 구현이 가능
    
    - DTL (Django Template Language) : Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템
        * Variable 
        ex) view : context(변수 - Dictionary)를 선언하고 render의 세 번째 파라미터로 전송
        ex) templates : {{ 변수명 / 변수명.속성값 }} 을 통해 view에서 선언한 변수를 동적으로 사용
        
        * Filters : 60여개의 built-in filter를 기반으로 표기할 변수를 수정할 때 사용 
        ex) templates : {{ 변수|filter }}
        
        * Tags : 20여개의 built-in tag를 기반으로 반복 / 논리 구조를 생성
        ex) templates : {% tag %} / {% start_tag %} ~~ {% end_tag %}

        * Comments : 주석
        ex) templates : {# ~ #} / {% comment %} ~~ {% endcomment %}

        
    - Template 상속 : 다수의 template이 공통 요소를 공유할 수 있게 하는 기능
        1. 공통 요소를 포함한 parents template(관례적으로 base.html) 생성
        2. parents template 내에 재정의 할 수 있는 공간 block tag로 정의
        3. child template의 최상단에서 extends tag로 상속 선언 후 (최대 1개) block tag만으로 내용 작성

        
Request / Response
- HTML Form Element(Tag) : 사용자와 어플리케이션 간의 상호작용을 위해 데이터(text, password, checkbox, ...)를 전송할 때 사용하는 요소
    <form action='서버 주소' method='GET / POST'>
        <input type='text' name='_KEY_' id='' ...>
        <input type='submit' value=''>
    </form>

    - form_tag
        * action : 데이터를 전송할 주소
        * method : 전송할 방식 (GET : 조회, POST : 생성, 삭제, 수정)
    
    - input_tag
        * name : 서버가 입력 데이터에 접근할 Key
        * placeholder : 입력창 내부의 기본값

        
URL
- Query String Parameters : URL 주소에 파라미터를 통해 입력 데이터를 서버로 보내는 방법으로 기본 URL과 ?로 구분되어, Key=value 형태로 전송

- Variable Routing : URL의 일부만 변경되는 경우, 해당 부분을 변수로써 사용하는 것
    path('_url_/<path_converter: varibale_name>/', views._function_)

- APP URL mapping : 각 앱의 urls.py에서 각 앱의 URL을 관리하는 것으로 프로젝트의 유지보수성이 높아지고, URL 생성 부담이 줄어듬
    urls.py : path('_separateURL_', include('APP.urls'))
    
    ※ Naming URL patterns : 각 페이지의 실 URL이 아닌, 해당하는 name으로 접근하여 사용할 수 있도록 하는 기술로 유지보수성을 높일 수 있음
        html : <a href="{% url 'app_name:path_name' variable_routing0 variable_routing1 %}"></a>

        urls.py : 
            app_name = 'app_name'
            path('_separateURL_', include('APP.urls'), name='')


<실습>


"""