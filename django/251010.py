"""
[251010]

<Django 라이브 강의>

Static Files : 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
ex) CSS, JavaScript, 이미지, 폰트, ...

- Default Path : app_folder/static/...
    templates.html -> {% load static %}, <link href='{% static 'path' %}'>

- Additional Path : project/setting.py -> STATICFILES_DIRS 에 문자열로 추가 경로 설정


Media Files : 사용자가 웹사이트를 통해 직접 업로드하는 파일
    project/setting.py -> MEDIA_ROOT, MEDIA_URL 생성 -> 
    ※ MEDIA_ROOT : 업로드한 파일을 저장할 서버의 절대 경로
    ※ MEDIA_URL == STATIC_URL : 웹 페이지에서 접근할 때 사용할 URL 주소

    project/urls.py -> from django.conf import settings, from django.conf.urls.static import static, + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    templates.html -> <form enctype='multipart/form-data'>
        ※ form tag의 경우, 기본적으로 text만 전송하므로 encrypt type 변경이 필요
    views.py -> form = Form_NAME(request.POST, request.FILES)
        ※ file의 경우, request.POST에 위치하지 않고, request.FILES에 위치
    
    ※ Advanced upload_to
    - upload_to='%Y/%m/%d/' : 날짜를 기준으로 폴더 생성 및 저장
    - 함수를 생성하여 지정
        upload_to=imagePath
        def imagePath(instance, filename): return f'image/{instance.user.name}/{filename}'


AWS(Amazon Web Services)
- EC2 : 가상서버
- S3 : 파일 저장소
- RDS : DB


<실습>


"""