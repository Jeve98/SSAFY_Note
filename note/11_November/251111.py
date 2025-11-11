"""
[251111]

<DB 라이브 강의>

Fixtures : Django 개발 시, DB의 기본 데이터를 미리 세팅할 수 있도록 추출한 초기 데이터 파일
    * dumpdata : DB의 데이터 추출 명령어로, 특정 모델 혹은 앱 전체의 데이터를 JSON 형태로 추출
        ex) python manage.py dumpdata [option] [app_name.model_name] > file_name.json
    * loaddate : DB에 추출한 데이터를 저장하는 명령어로 한번에 다수의 데이터를 불러올 때는 Django가 알아서 우선순위에 맞게 동작하나 개별적으로 불러올 경우, 모델 관계에 맞춰 순서를 맞출 필요가 있음
        ex) python manage.py loaddata file_path
        ※ file_path의 기본 경로 준수 : app_name/fixtures/...


Improve Query : 최적화를 위해 DB에 보내는 query 개수를 줄여서 조회하는 방법으로 N+1 문제를 해결
※ N+1 문제 : 1개의 query로 데이터를 가져왔더라도 관련 데이터를 추가로 가져오기 위해 추가 쿼리 N개가 더 실행되는 상황
- annotate : GROUP BY 연산을 기반으로 추가 연산된 결과를 별도의 field로 추가하여 함께 반환
    ex) Model.objects.annotate(fields_name=집계함수)
- select_related : N에서 1을 참조할 때 JOIN을 통해 전체 테이블을 반환
- prefetch_related : 1에서 N 혹은 M에서 N을 역참조할 때 JOIN을 통해 전체 테이블을 반환


<실습>


"""