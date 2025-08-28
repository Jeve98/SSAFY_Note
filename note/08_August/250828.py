"""
[250823]

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
    
    * Bootstrap
        - Grid System (!= CSS' grid) : 웹 페이지의 레이아웃을 조정하는 데 사용되는 12개 컬럼과 6개의 breakpoint로 구성된 시스템으로 다양한 기긱에서 반응형 디자인을 지원
            ※ 반응형 웹 디자인 : 디바이스 종류나 화면 크기에 상관없이 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술
            - Container : 전체 column을 담는 공간
            - Row : 내부에 총 12개의 column 영역이 구성됨
            - Column : 실제 컨텐츠를 포함하는 부분
            - Gutter : column 사이의 상하좌우 여백 영역으로 padding, margin을 대신함
                * column의 제한이 있으므로 x축은 padding, y축은 margin으로 생성
            
            - Breakpoint : 특정 너비 이상의 화면에서 다음 container width size로 변경하는 지점
                ex) xs(default), sm, md, lg, xl, xxl

            - Nesting (중첩) : 하나의 column 안에 또 다른 row 추가가 가능
            - Offset (상쇄) : 일부 column의 생략

    position : normal flow에서 벗어날 필요가 있는 경우 (relative-absolute, fixed, sticky)
    flex box : 공간 내 요소 정렬
    grid system : 반응형 디자인을 기반으로 가장 큰 layout 형성

- Javascript


UX(User Experience) : 제품, 서비스를 이용하는 사람들이 느끼는 전체적인 경험 및 만족도 개선, 최적화하기 위한 디자인과 개발 분야
- 리서치 > 데이터 설계 및 정제 > 유저 시나리오 > 프로토타입 설계
- UX researcher, user researcher
> 인문학

UI(User Interface) : 서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소들을 개발하고 구현하는 분야
- product designer, interaction designer
> 기술

>> UI 개발은 UX를 기반으로 구현되어야 함


<실습>


"""