"""
[250723]

<Python 라이브 강의>

Python 가상환경
- python -m venv venv : 가상환경 모듈 실행 (가상환경 생성)
- source venv/Scripts/activate : 가상환경 실행 (이후 동작은 가상환경에서 동작)

Jupyter notebook : D.S.에서 많이 활용되는 파이썬 개발 환경으로 웹 브라우저에서 동작하며 코드 실행, 텍스트 문서 작성, 시각화를 하나의 문서에 통합하여 작업 가능
- esc(명령 모드) && enter(실행 모드)
- shift enter : 다음 cell로 이동하며 동작
- ctrl enter : 현재 cell에서 머무르며 동작
- m : cell to markdown
- y : cell to code block
- dd : selected cell delete

Data Science : 다양한 데이터로부터 새로운 지식과 정보를 추출하기 위한 과학적 방법론, 프로세스, 알고리즘, 시스템 등의 융합 분야
- 정보 추출 5단계 : 문제 정의 > 수집 > 전처리 > 분석 > 결과 해석 및 공유
    * 데이터 수집 : 웹 스크래핑/크롤링, Open API, 데이터 공유 플랫폼(ex. 캐글, 데이콘, 공공데이터포털, ...)
        ※ csv : 몇 가지 필드를 쉼표로 구분한 텍스트 데이터 및 파일로 처리 가능한 프로그램이 다양하고 저장, 전송 및 처리 속도가 빠름
    * 데이터 전처리 : 데이터 품질 개선, 중복 데이터 제거, 분석하기 적절한 형식으로 변환
        ※ Numpy : 수학 계산용 패키지로 다차원 배열의 처리를 쉽고 효율적으로 할 수 있게 지원하지만 유연성이나 그룹화, 피벗과 같은 구조화가 부족
        ※ Pandas : 원하는 데이터만 추출하거나 데이터를 분석할 때 활용되는 패키지
        ※ Matplotlib : 데이터 시각화 패키지


외부에 공개되면 안되는 값 > 환경변수로 관리 (ex. API KEY)
- .env 파일 + gitIgnore
- python-dotenv 패키지 : 환경변수 관리 패키지
    - dotenv > load_dotenv() : .env 파일을 자동으로 read
    - os > getenv(변수명) : 변수에 해당하는 값을 .env 파일에서 load
        

<실습>


"""