"""
[251127]

<Vue 라이브 강의>

Template Syntax : DOM을 컴포넌트 인스턴스의 데이터에 선언적으로 바인딩하기 위해 사용하는 HTML 기반 템블릿 구문
※ 선언적 바인딩 : JS 상태 변화에 따라 자동으로 DOM이 업데이트 되는 것
- Text Interpolation : 데이터 바인딩의 가장 기본적인 형태로, mustache syntax '{{}}', 'v-text'로 구현
- Raw HTML : Text Interpolation의 경우, 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML 출력을 위해 사용하며 'v-html'로 구현되나 보안상 이유로 권장하지 않음
- Attribute Bindings : HTML의 속성값을 vue의 dynamicId 속성과 동기화 되도록 하는 방법으로 'v-bind.속성값'으로 구현
- JS Expressions : 데이터 바인딩 내에서 JS 표현식의 기능을 지원하기 위한 방법으로 mustache syntax 내에 JS 표현식, v-로 시작하는 특수 속성의 값을 통해 사용
    ※ 각 바인딩 당 하나의 단일 표현식만 포함되며 선언식은 지원하지 않음


Directive : v- 접두사가 있는 특수 속성으로 v-for, v-on을 제외한 모든 속성값은 단일 JS 표현식이어야 함

    v-attribute:Argument.Modifiers="Value"
        - Argument : 속성명, 이벤트명 등 바인딩 하고자 하는 대상
        - Modifiers : directive가 특별한 방식으로 바인딩되어야 할 경우, 이에 대한 특수 접미사를 붙이는 것으로 추가적인 동작을 지시

    v-bind (Attribute Bindings): 하나 이상의 속성 또는 데이터를 동적으로 바인딩하는 directive로, :을 약어로 사용

        <img v-bind:src='imgSrc1'>
        <img :src='imgSrc2'>
        <p :[dynamic_attr]='dynamicVal'></p>        # [] 내부의 이름은 소문자로만 적용 가능
        <div :class='{className: isActive}'></div>
        <div :class='classObj'></div>

        setup(){
            const imgSrc1 = ref('my-id');
            const imgSrc2 = ref('test-id');
            const dynamic_attr = ref('title');
            const dynamicVal = ref('value');
            const isActive = ref(false);
            const classObj = ref({
                active: true,
                className: true
            })

            return {
                imgSrc1,
                imgSrc2,
                dynamic_attr,
                dynamicVal,
                isActive,
                classObj
            }
        }

    v-on : DOM 요소에 이벤트 리스너를 연결하는 directive로, @를 약어로 사용

    v-model : form을 처리할 때, 사용자가 input으로 입력한 값을 실시간으로 JS 상태에 동기화하기 위한 directive으로 form input요소에 대한 양방향 바인딩 구현

        <input v-model='inputText'>

        setup(){
            const inputText = ref('')

            return {
                inputText
            }
        }


<실습>


"""
