"""
[251103]

<DB 라이브 강의>

Data : 저장/처리를 위해 변환된 정보
- File : 어디에서나 쉽게 사용 가능하지만 데이터를 구조적으로 관리하기 어려움
- Spreadsheet : 테이블의 열과 행을 사용해 데이터 관리하는 방법으로 크기, 단락적인 보안, 데이터 조작의 정확성에서 문제 발생

DB : 체계적으로 정리된 데이터의 모음으로 Create/Read/Update/Delete 기능을 제공
- Relational DB : 데이터 간에 관계가 있는 데이터 항목들의 모음으로 데이터 포인터를 저장하고 이를 통한 액세스를 제공
    ※ 관계 : 여러 테이블 간의 논리적 연결로 이를 통해 다양한 형식으로 데이터 조회가 가능함
        >> Primary Key (기본키), Foreign Key (외래키)를 통한 참조
    * Table (Relation) : 데이터를 기록하는 곳
    * Field (Column, Attribute) : 고유한 데이터 형식이 지정된 열
    * Record (Row, Tuple) : 구체적인 데이터 값이 저장된 행
    * Database (Scheme) : Table의 집합
    * Primary Key : 각 record의 고유한 값으로 RDB에서 record 식별자로 사용
    * Foreign Key : 다른 table의 record를 식별할 수 있는 key로 다른 테이블의 primary key를 참조

DBMS(Database Management System) : DB를 관리하는 sw로 DB, 사용자 간의 인터페이스
- RDBMS : RDB를 관리하는 sw
    ex) SQLite, MySQL, PostgreSQL, Oracle Database, ...
    ※ SQLite : 경량의 오픈 소스 DBMS로 설치 없이 실행 가능해, 모바일 앱/소규모 프로그램에 적합

SQL(Structure Query Language) : table 형태로 구조화 된 RDB에게 하는 요청(질의)로, 각 statement는 세미콜론으로 구분됨
※ 대소문자의 구분은 없으나 대문자 작성을 권장
- SQL Statement : SQL을 구성하는 가장 기본적인 코드 블록으로 DDL(데이터 정의), DQL(데이터 검색), DML(데이터 조작), DCL(데이터 제어)로 구분
    - Filtering Keyword
        * Clause : SQL 문장에서 특정 기능을 수행하도록 지정하는 문장 구성 요소
            - DISTINCT : 조회 결과에서 중복된 record를 제거
            - WHERE : 비교/논리 연산자를 사용하는 구문 (그룹화 이전에 적용)
                ※ SQL의 논리 연산 : TRUE, FALSE, UNKNOWN
                ※ NULL 비교에서 IS가 아닌 =를 사용하는 경우, 값이 존재하지 않음을 비교하게 되므로 T/F가 아닌 UNKNOWN을 반환
            - HAVING : 집계 항목에 대한 세부 조건을 지정 (그룹화 이후에 적용)
            - LIMIT : 하나 또는 2개의 인자(offset, count)를 사용하여 조회하는 record 수를 제한
        * Operator : SQL에서 조건을 비교하거나 데이터를 선택하기 위해 사용하는 명령 기호 또는 키워드
            - 비교/논리 연산자
            - BETWEEN : WHERE 문에서 비교 연산자를 사용할 때, 특정 값의 범위를 대체하여 사용할 수 있는 키워드
            - IN
            - LIKE : 값이 특정 패턴에 일치하는지 확인하는 키워드
                - Wildcard '%' : 0개 이상의 문자열과 일치하는지 확인 (후열 값 앞으로 다수 문자 존재)
                - Wildcard '_' : 단일 문자와 일치하는지 확인 ('_' 1개 당, 후열 값 앞으로 문자 1개)
                ex) LastName Like '%son'
    
    - DQL(Data Query Language) : 데이터 검색
        * SELECT : 조회 대상 field를 1개 이상 지정하여 지정된 field를 조회 (출력 field명 지정, 간단한 연산 가능)
        * ORDER BY : 하나 이상의 field를 기준으로 결과를 오름차순(ASC), 내림차순(DESC)로 정렬
        * GROUP BY : 값에 대한 계산을 수행한 뒤 단일 값을 반환하는 Aggregation Function(집계 함수)를 사용하여 record에 대한 요약본을 생성
    
    ※ 내부 동작 순서 : FROM > WHERE > GROUP BY > HAVING > SELECT > ORDER BY > LIMIT


<실습>

[SQLite CLI 명령어]
sqlite3 File_Name : SQLite - CLI 연결 (DB가 없을 경우, 생성)
.table : table 목록 조회
.schema : table schema 조회
.mode markdown : table 출력 모드를 마크다운 테이블 형식으로 변경
.quit : SQLite CLI 종료
"""