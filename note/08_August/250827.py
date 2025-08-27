"""
[250827]

<Web 라이브 강의>

Web page
- HTML
- CSS
    * Style
    * 구조 및 문법
    * Box Model
        - 구조 : Margin, Content, Padding, Border
        ※ shorthand 속성
    * 레이아웃
        ※ Normal Flow
        - disply 속성
            -- outer display 타입 : Block, Inline, Inline-Block, None
            -- inner display 타입 : Flexbox > 반응형 레이아웃 작성에 용이
        ※ Unnormal Flow
        - position 속성 : static, relative, absolute, fixed, sticky
            - 기본 속성 : top, bottom, left, right, z-Axis
            > 공간 배분, 정렬이 어려움
    
    * Bootstrap : CSS 프론트엔드 프레임워크 툴킷으로 미리 만들어진 다양한 디자인 요소들을 제공
        ※ CDN(Content Delivery Network) : 지리적으로 가까운 CDN 서버에서 컨텐츠를 전송하여 서버와 사용자 사이의 물리적인 거리를 줄여 컨텐츠 로딩에 소요되는 시간을 최소화하는 방법
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">

        - 기작성된 스타일 및 레이아웃 클래스 이름 규칙 : {property}{sides}-{size}
        ex) mt-5 (margintop-3rem(48px)), ms-5(marginstart(left)-3rem(48px))

        - @media(조건){ selector{} } : 화면 크기, 기기 종류에 따라 반응형 웹 디자인을 만들어주는 미디어 쿼리

        - Reset CSS : 모든 html 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 시트
            - 브라우저 별 user agent style sheet가 존재하는데 이를 모두 똑같은 스타일 상태로 만들기 위해 사용
            ex) Normalize CSS : 웹 표준을 기준으로 브라우저 중 하나가 불일치 하고 이를 수정하지 못한다면 차이가 있는 브라우저를 기준으로 수정하는 방법

- Javascript

Semantic Web : 웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식으로 요소의 시각적 측면이 아닌 목적과 역할에 집중하는 방식
- Semantic in html : 외형 보다는 요소 자체의 의미에 집중하는 것
    - html semantic element : 기본적인 외형과 기능 이외의 의미를 가지는 html 요소로 검색엔진 및 개발자가 이를 이해하기 쉽게 해줌
    ex) p 태그의 font-size를 키운 것과 h1 태그의 외형은 비슷할 수 있으나, 둘이 가지는 의미는 다름
    ex) block에 의미를 부여한 header, nav, main, article, aside, footer

css 방법론 : css를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인
    - OOCSS (Object Oriented CSS) : 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론으로 구조와 스킨을 분리한 뒤, 컨테이너와 컨텐츠를 분리하여 진행

    
<실습>


"""