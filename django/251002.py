"""
[251002]

<PJT>

Django
- Model
    - choices 속성 : 모델 필드에 미리 정해진 선택지를 부여하는 속성으로 사용자에게 드롭다운 메뉴를 제공
    in model)
        CHOCIES = [('TODOS', '할 일'), ('DOING', '진행 중'), ('DONE', '완료')]  # 0번 문자열로 DB 저장, 1번 문자열로 유저에게 출력
        status = model.CharField(chocies=CHOCIES, default='TODOS')

    - Blank 속성 [서류 양식에 대한 규칙] : 빈 값의 허용 여부 >> 빈 값으로 제출 가능
        ex) DB에서 빈 문자열로 저장이 되지 Null로 저장되지 않음

    - Null 속성 [서류 보관함에 대한 규칙] : 'null 데이터'의 허용 여부 >> 빈 값으로 제출 불가능
        ex) DB의 구조상 Null을 허용하는 것이지 Form 검증에서 이를 허용하는 것이 아님 (통상적으로 default와 함께 사용)

    ※ 빈 문자열 vs Null
        - 빈 문자열 '' : 길이 0의 문자열 값이 존재
        - Null : DB 수준에서 값이 존재하지 않음
    
    - PositiveInteger 필드 : 0을 포함한 양의 정수만 저장할 수 있도록 강제하는 django 모델 필드

- Form
    - form.as_table : form의 출력을 table 형태로 출력
    - form.as_<tag> : form의 출력을 <tag> 형태로 출력
    ※ default : div

    - cleaned_data 속성 : 유효성 검사를 통과한 데이터를 담고 있는 파이썬 dictionary로 반드시 is_vaild()의 True 반환 이후에만 접근 가능하며 추가적인 로직 수행 시에 사용

    - MultipleChoice 필드 : Form에서 다수의 선택지를 동시에 선택할 수 있는 필드로 해당 값들은 파이썬 list 형태로 처리


<실습>


"""