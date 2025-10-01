"""
[250929]

<Django 라이브 강의>

HTML 'form' : 사용자의 데이터를 제출하기 위한 방법으로 자체적인 필터링이 불가
※ 유효성 검사 : 수집한 데이터가 정확하고 유효한지 확인하는 과정

Django Form : 사용자 입력 데이터를 수집하고 처리 및 유효성 검사를 수행하기 위한 도구로 form 태그를 통해 HTML의 label-input set를 대체함
- forms.Form : GET - 입력 데이터를 DB에 저장하지 않음 (검색, 로그인, ...)
    >> form 상속 시, formName(request, request.POST)

- forms.ModelForm : POST - 입력 데이터를 DB에 저장함 (게시글 작성, 회원가입, ...)
    - Meta class : ModelForm의 정보를 작성하는 곳으로 연결될 model, 사용할 fields, widgets을 선언
        ※ exclude(FieldName) : 최종 출력에서 해당 Field를 제외
    - instance : 기존 데이터를 사용하기 위해서는 key-word 인자, instance로 데이터에 해당하는 변수를 함께 제공
    - is_valid() : 유효성 검사 method로 False 발생 시, 에러 메세지를 함께 반환
    - save() : DB 객체를 만들고 저장/갱신하는 method로 생성된 객체를 반환
    >> ModelForm 상속 시, formName(request.POST)

- widgets : HTML input의 표현 담당으로 Form의 경우, Field의 파라미터로 사용되고 ModelForm의 경우, 상속된 model의 정보 외에는 Meta의 widget 변수의 값으로 사용


<실습>


"""