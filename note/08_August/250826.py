"""
[250823]

<web 라이브 강의>

Web page
- HTML
- CSS
    * Style
    * 구조 및 문법
    * Box Model
        - 구조 : Margin, Content, Padding, Border
        ※ shorthand 속성

    * 레이아웃 : 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
        ※ Normal Flow : 레이아웃을 변경하지 않은 일반적인 웹 페이지 요소가 배치되는 방식
        - disply 속성 : 대표적으로 Block, Inline으로 나뉘며 배치 흐름 및 다른 박스와 관련하여 동작하는 방식이 달라짐
            -- outer display 타입
            - Block : 하나의 독립된 덩어리처럼 동작하는 요소로 다른 요소가 옆에 끼어들 수가 없기 때문에 web page의 큰 구조와 단락을 구성하는데 사용됨
                1. 항상 새로운 행으로 나뉨 (너비 100%)
                2. width, height, margin, padding 속성을 모두 사용 가능
                3. padding, margin, border로 인해 다른 요소를 상자로부터 밀어냄
                4. width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함
                ex) h1 ~ h6, p, div, ul, li, ...
                ※ div : 다른 html 요소들을 그룹화하여 레이아웃을 구성하거나 스타일링을 적용하며 헤더, 푸터, 사이드바 등 웹 페이지의 다양한 섹션을 구조화하는 데 가장 많이 쓰이는 요소
                ※ margin collapsing : 두 block 요소의 margin이 맞닿아 있을 때, 더 큰 margin 값만 적용되는 현상 - 일관성, 단순성 부여
            - Inline : 문장 안의 단어처럼 흐름에 따라 자연스럽게 배치되는 요소
                1. 줄바꿈이 일어나지 않기 때문에 컨텐츠의 크기만큼만 영역을 차지함
                    > width, height 속성 사용 불가
                2. 수직 방향으로 padding, margin, border가 적용은 되지만 다른 요소를 밀어낼 수 없음
                3. 수평 방향으로 padding, margin, border가 적용되어 다른 요소를 밀어낼 수 있음
                ex) a, img, span, strong, ...
                ※ span : 자체적인 시각적 변화는 없으나 텍스트 일부만 조작하기 위해 사용
            - Inline-Block : inline과 block의 특징을 모두 가진 속성값으로 줄바꿈 없이 요소의 크기 지정이 가능
                1. padding, margin, border로 인해 다른 요소를 밀어낼 수 있음
            - None : 화면에 표시하지 않고 공간조차 부여되지 않은 요소로 on/off와 같이 2가지 레이아웃이 필요할 때 사용
            
            -- inner display 타입 : 박스 내부의 요소들이 어떻게 배치될지 결정
            - Flexbox : 요소를 행과 열로 배치하는 1차원 레이아웃 방식 (공간 배열, 정렬의 관점)
                - main(horizontal) / cross(vertical) axis : flexbox에서 요소들이 배치되는 주축과 교차축
                - flex container : diplay : flex(inline-flex)가 설정된 부모 요소로 자식 요소를 배치하는 주체
                    * flex-direction : default로 row 값을 가지며 -reverse로 지정할 수도 있고 column으로 변경할 수도 있음
                    * flex-wrap : item 목록이 container의 크기를 초과할 경우, 다른 행에 배치할지 여부 결정
                    * justify-content : 주 축을 따라 item을 정렬하고 간격을 조절
                    * align-items : item들의 교차축 정렬 방법을 지정
                    * align-content : container에 다수의 item 줄이 있을 때, 그 줄들 사이의 공간을 어떻게 분배할 지 지정 (wrap 설정 필수)
                - flex item : flex container의 내부 요소로 flexbox 레이아웃의 영향을 받음
                    * order
                    * flex-grow : container의 여백을 item들에게 분배하는 양
                    * flex-basis : item의 기본 크기 >> 기본적으로 컨텐츠의 크기에 맞춰짐
                    * align-self : 교차 축을 따라 item을 개별적으로 정렬
                > 배치 : flex-direction, flex-wrap
                > 공간 분배 : justify-content, align-content
                > 정렬 : align-items, align-self
            > 반응형 레이아웃 작성에 용이
        
        - position 속성 : 요소를 normal flow에서 제거하여 다른 위치로 배치하는 것
            - 기본 속성 : top, bottom, left, right, z-Axis(요소의 쌓이는 순서로 숫자가 클수록 위에 위치하며 static이 아닌 요소에만 적용됨)
            - static : 기본값으로 normal flow에 따라 배치됨 (기본 속성이 적용되지 않음)
            - relative : normal flow에 따라 배치된 후, 자신의 원래 위치를 기준으로 기본 속성에 따라 위치를 조정 (기존 영역은 유지하기 때문에 다른 요소의 레이아웃에 영향을 주지 않음)
            - absolute : normal flow에서 요소를 제거하여 가장 가까운 relative 부모 요소 혹은 body 태그를 기준으로 이동 (기존 영역 제거)
            - fixed : normal flow에서 요소를 제거하여 현재 화면영역(viewport)를 기준으로 이동
            - sticky : relative와 fixed의 혼합형으로 스크롤 위치가 임계점에 도달하기 전에는 relative로 동작하지만 임계점에 도달한 경우 fixed로 화면에 고정됨 (다음 sticky 요소가 나오면 이전 sticky 자리를 대체)
        > 공간 배분, 정렬이 어려움
        
- Javascript


<실습>

html-요소 type
- block [display : "block"] : 무조건 한 줄을 차지하는 요소
ex) h1 ~ h6, p, div, ul, li, ...
- inline [display : "inline"] : 자신의 크기만큼만 차지하는 요소
ex) a, img, span, strong, ...














2. box-sizing: content-box vs. border-box
7. flexbox의 모든 속성, 옵션
    - 만약 튀어나온 부분을 다음 줄로 내리고 싶으면? flex-wrap: wrap
    - flex-direction: row-reverse... 단답형으로 물어볼 가능성이 있으므로 정확한 스펠링까지 알아둘것.....
9. bootstrap..
10. 시맨틱 태그의 의미와 중요성, 다음 중 시맨틱 태그가 아닌 것은?
div -> main
div -> article
11. CDN
12. flex의 align-items: center, start, end, stretch
1. margin, padding: 값이 4개, 3개, 2개, 1개 - 순서 암기
3. order 속성: 값이 작을수록 앞에 오지만, flex-direction이 reverse인지 아닌지 확인
4. 반응형 웹디자인 만들기: flex-basis, flex-grow
6. CSS 상속의 특징: border는 상속 x, font-size, color 상속 o
8. bootstrap의 Grid system 코드를 주고
offset이 적용된 모습 예측하기(언제 오프셋이 생기고 사라지는지)
9. grid system에서는 기본적으로 column 12개로 나눔. 몇 개의 column?
10. bootstrap의 spacing 지정 방법
m : margin / p : padding
t: top, b: bottom, s: start, e: end, x: 좌우, y: 상하
ms-5 : 왼쪽에 5만큼 마진
pe-3 : 오른쪽에 3만큼 패딩
ms-auto : 앞쪽에 줄 수 있는 만큼 마진 주기
11. button, navbar, modal
"""