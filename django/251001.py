"""
[251001]

<Django 라이브 강의>

Authentication
- Django Authentication System
    - User Model >> Custom User Model 사용 권장
    - Session 관리
    - 기본 인증

- Login
>> CRUD 中 Create (Session 생성)
    - 인증된 사용자 접근 제한
        * is_authenticated [속성] : 인증 여부를 알 수 있는 읽기 전용 속성
            ex) 비인증 사용자의 경우, AnonymousUser를 상속 중이므로 해당 속성이 False로 되어있음
            >> 주소를 알고 있는 경우, 비로그인 상태로도 접근 가능하므로 view 함수 수정을 요함
        * login_required [데코레이터] : 비인증 사용자의 경우, /accounts/login/ 주소로 redirect 시킴
            >> 주소를 알고 있더라도 view 함수 자체적으로 접근을 방지하므로 접근 불가

- Logout : 요청에 대한 서버의 세션 데이터를 비우고 클라이언트의 세션 쿠기를 삭제
>> CRUD 中 Delete (Session 제거)

- 회원가입 
>> CRUD 中 Create (DB 내 User 생성)

- 회원탈퇴 : 통상적으로 일정 기간 비활성화로 사용
>> CRUD 中 Delete (DB 내 User 제거)

- 회원정보 수정
>> CRUD 中 Update

- 비밀번호 변경 : 인증된 사용자의 Session 데이터를 Update 하는 과정
>> CRUD 中 Update


※ 비밀번호 암호화
D: hash > A: rainbow table(자주 사용하는 pw 모음집) > D: add salt > A: brute-force > D: key stretching(연산을 의도적으로 반복시켜 연산 속도 하락)


※ 추상 기본 클래스 : DB 테이블을 만드는데 사용되지 않으며 다른 모델의 기본 클래스로 사용
- AbstractBaseUser class : 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스로 필요 최소한의 기능만 제공
- AbstractUser class : 관리자 권한과 함께 완전한 기능을 가지고 있는 user model을 구현하는 추상 기본 클래스로 모든 필드가 기구현되어 있음


※ context processor : 자주 사용되는 데이터 목록을 미리 전역으로 템플릿에 로드해둔 것


<실습>


"""