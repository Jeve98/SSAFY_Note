"""
[251120]

<JS 라이브 강의>

event : 무언가 일어났다는 신호 또는 사건
- event object : DOM에서 event가 발생했을 때, 브라우저가 생성하는 해당 event에 대한 정보 객체
- event handler : 특정 이벤트가 발생했을 때 실행되는 이벤트 처리기(콜백 함수)
    * addEventListener(EVENT_TYPE, CALLBACK_FUNCTION, CAPTURING_OPTION) : 특정 DOM 요소에 지정한 이벤트가 발생했을 때 실행할 event handler를 등록하는 메서드

    ※ Bubbling : 한 요소에 event 발생 시, 해당 요소의 handler가 동작한 후 최상단 조상 요소를 만날 때까지 부모 요소의 handler가 뒤이어 동작하는 현상
        >> event.currentTarget(현재 이벤트 발생지) / event.target(이벤트 발생 원류)를 이용하여 관리
        >> 각자 다른 동작을 수행하는 버튼이 다수 존재할 경우, 공통 조상에 event handler를 추가한 뒤 콜백 함수에서 로직을 분화
    ※ Capturing : event가 최상위 조상에서 타겟 요소까지 하위로 전파되는 현상


lodash : 모듈성, 성능 및 추가 기능을 제공하는 JS 유틸리티 라이브러리
    <script src='https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js'></script>



<실습>


"""
