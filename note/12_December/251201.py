"""
[251201]

<Vue 라이브 강의>

computed(CALLBACK_FUNCTION) : '계산된 속성'을 정의하는 함수로 한 번 계산된 값을 캐싱하여 의존 중인 데이터의 변경 이전까지 사용하므로 성능을 향상시킴
※ vs Method : 캐싱 유무에 따른 성능 차이

    <p>{{ restOfTodos }}</p>
    
    setup(){
        const {createApp, ref, computed} = Vue

        const restOfTodos = computed(() => {
            return todos.value.length > 0 ? 'still exist' : 'finish'    // 반환되는 값은 계산된 ref로 의존된 반응형 데이터를 자동으로 추적하고 의존하는 데이터 변경 시에만 재평가됨
        })
    }

watch(value, (newValue, oldValue) => {CALLBACK_FUNCTION}) : 하나 이상의 반응형 데이터를 감시하고 해당 데이터가 변경되면 콜백 함수를 호출

Directive
    v-attribute:Argument.Modifiers="Value"
        - Argument : 속성명, 이벤트명 등 바인딩 하고자 하는 대상
        - Modifiers : directive가 특별한 방식으로 바인딩되어야 할 경우, 이에 대한 특수 접미사를 붙이는 것으로 추가적인 동작을 지시

    v-bind (Attribute Bindings)

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

    v-on

    v-model

        <input v-model='inputText'>

        setup(){
            const inputText = ref('')

            return {
                inputText
            }
        }  
    
    v-if (v-else-if) : 표현식 값의 T/F를 기반으로 요소를 조건부로 렌더링하는 방법 (렌더링 자체를 결정)
    ※ 단, v-else-if 블록의 경우, 앞선 v-if(v-else-if) 블록과 연이어서 사용해야함

        <p v-if='isSeen'> True? </p>

        setup(){
            const isSeen = ref(true)

            return {
                isSeen
            }
        }

    v-show : 표현식 값의 T/F를 기반으로 요소의 가시성을 전환 (CSS의 display 속성을 변화)

    v-for : 소스 데이터를 기반으로 요소 또는 템플릿 블록을 반복 랜더링하며 value, key, index를 조합하여 순회할 수 있음
    ※ key를 통해 고유한 값으로 식별이 가능

        <p v-for='item in items' : key='item.id'> {{ item.name }} </p>

Lifecycle Hooks : Vue 컴포넌트가 생성되고 DOM에 마운트되어 업데이트 되고 소멸하는 각 생애 주기 단계에서 실행되도록 제공되는 함수
    
    onMounted(){
        // HTML에 올라온 순간
    }


<실습>


"""