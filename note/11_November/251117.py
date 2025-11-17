"""
[251117]

<JS 라이브 강의>

V8 자바스크립트 엔진 : 웹을 문서에서 어플리케이션 플랫폼으로 바꾸는데 결정적인 역할을 한 엔진으로 기존의 인터프리터 작업을 JIT 형식으로 변경
※ JIT : 많이 사용되는 코드에 대해 사전에 번역을 완료해두는 것으로 코드 실행의 속도를 극적으로 향상시킨 방법

ECMAScript(ES) : 표준화된 스크립트 프로그래밍 언어 명세로, JS의 전체 코드를 공개하기 어려워 이에 대한 표준을 제공하기 위해 개발
※ JS는 ES6를 기준으로 var 대신 let, const 등이 생기고 class가 적용되어 객체지향 프로그래밍 언어로써 발돋음을 시작


변수명 작성 규칙 : 문자, '$', '_'로 시작, 예약어는 사용 불가
- camelCase : 변수, 객체, 함수
- PascalCase : 클래스, 생성자
- SNAKE_CASE : 상수

변수 선언 키워드
- let : 재선언이 불가하고 재할당이 가능한 블록 스코프의 지역 변수 선언 시 사용
    >> 필요한 순간에 유연성 확보를 위해 const 변수를 전환
- const : 재선언, 재할당이 불가한 변수 선언 시 사용
    >> 코드 의도의 명확화 및 의도치 않은 값 변경으로 인한 버그 방지
- var : 재선언/재할당이 가능한 함수 스코프의 변수 선언 시 사용했던 키워드로 현재는 Hoisting 문제로 사용 불가
    ※ Hoisting : 변수의 선언문이 코드의 최상단으로 끌어올려지는 듯한 현상으로 let, const도 hoisting 작업이 이루어지지만 변수가 만들어지는 내부 과정이 var와 다르기에 문제를 방지


DOM(Document Object Model) : 웹 페이지를 구조화된 객체로 제공하여, 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
- DOM API : 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작할 수 있도록 페이지 요소들을 객체 형태로 제공하며 관련 메서드를 함께 제공하는 API
    >> HTML 구조와 내용을 조작하는 명령어의 모음
    
    - DOM 요소 선택
        * .querySelector(_selector_) : 선택자와 일치하는 첫 번째 element를 반환 (없을 경우, null 반환)
        * .querySelectorAll(_selector_) : 선택자와 일치하는 다수의 element를 NodeList로 반환
    
    - DOM 조작
        - 클래스 속성 조작 : 스타일링 및 상태 제어를 위한 클래스 목록을 동적으로 추가/제거
            * 'classList' property : 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
                ex) element.classList.add() : 지정한 클래스 값 추가
                ex) element.classList.remove() : 지정한 클래스 값 제거
                ex) element.classList.toggle() : 존재하는 클래스라면 제거 후 false 반환, 존재하지 않다면 추가 후 true 반환
        - 일반 속성 조작 : id, href 등 요소의 모든 HTML 속성 값을 직접 설정/조회
            ex) element.getAttribute() : 지정된 값을 반환 (조회)
            ex) element.setAttribute(name, value) : 지정된 요소의 속성값을 지정하며 이미 존재한다면 갱신
            ex) element.removeAttribute() : 지정된 값을 제거
        - HTML 콘텐츠 조작
            * 'textContent' property : 요소의 텍스트 콘텐츠를 표현 (태그를 제거하여 순수한 텍스트 데이터만 추출)
        - DOM 요소 조작
            ex) document.createElement(tagName) : 작성한 tagName의 HTML 요소를 생성하여 반환
            ex) Node.appendChild() : 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입한 후 추가된 객체를 반환
            ex) Node.removeChild() : DOM에서 자식 Node를 제거한 후 반환
        - 스타일 조작
            * style property : 해당 요소의 모든 style 속성을 직접 추가/수정하는 방법
        
- DOM Tree
    - document Object : 웹 페이지를 나타내는 최상위 객체
    - element Object : HTML 요소(태그)를 나타내는 특별한 유형의 Node
    
    ※ Node Object : DOM의 기본 구성 단위
    ※ NodeList Object : DOM 메서드로 선택한 Node의 목록으로 배열과 유사한 구조를 가지며 JS의 배열 메서드를 사용할 수 있으나 DOM의 변경사항을 실시간 반영하지는 않음

- Parsing : 브라우저가 문자열을 해석하여 DOM Tree를 만드는 과정
    

<실습>


"""