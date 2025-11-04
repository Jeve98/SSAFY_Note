"""
[251104]

<DB 라이브 강의>

SQL(Structure Query Language) ※ 대소문자의 구분은 없으나 대문자 작성을 권장
- SQL Statement
    - Filtering Keyword
        * Clause
            - DISTINCT : 조회 결과에서 중복된 record를 제거
            - WHERE : 비교/논리 연산자를 사용하는 구문 (그룹화 이전에 적용)
                ※ SQL의 논리 연산 : TRUE, FALSE, UNKNOWN
                ※ NULL 비교에서 IS가 아닌 =를 사용하는 경우, 값이 존재하지 않음을 비교하게 되므로 T/F가 아닌 UNKNOWN을 반환
            - HAVING : 집계 항목에 대한 세부 조건을 지정 (그룹화 이후에 적용)
            - LIMIT : 하나 또는 2개의 인자(offset, count)를 사용하여 조회하는 record 수를 제한
        * Operator
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
    
    - DDL (Data Definition Language) : 데이터의 기본 구조 및 형식 변경
        * CREATE TABLE table_name : 작성한 field의 타입, 제약조건에 맞춰 table 생성
            ※ Constraints : 데이터의 무결성을 유지하고 DB의 일관성을 보장
                ex) PRIMARY KEY[only INTEGER TYPE], NOT NULL, FOREIGN KEY
        * DROP TABLE table_name : table 삭제
        * ALTER TABLE table_name : table, field 조작
            - ADD COLUMN : field 추가
            - RENAME COLUMN : field 명 변경
            - DROP COLUMN : field 삭제
            - RENAME TO : table 이름 변경
            ※ SQLite는 field의 속성 수정이 불가하므로 새로운 table을 생성한 뒤 데이터를 복사하는 방식으로 사용

    - DML (Data Manipulation Language) : 데이터 조작
        * INSERT INTO table_name(field_name) VALUES value : record 추가
        * UPDATE table_name SET field_name : record 수정
        * DELETE FROM table_name : record 삭제

    - DCL (Data Control Language) : 사용자 권한 제어

    - Multi-Table Query
        * JOIN Clause : 효율적으로 table를 관리하기 위해 분리한 table들의 데이터를 조합하여 검색하는 방법
            - INNER JOIN join_table_name ON join_constraint : 두 table에서 값이 일치하는 record에 대해서만 결과를 반환 
            - LEFT JOIN join_table_name ON join_constraint : 결합된 table의 일치하는 record와 함께 원본 table의 모든 record를 반환
                ※ 결합 이후, 특정 데이터가 NULL인 record 등을 찾을 때 유용


<실습>


"""