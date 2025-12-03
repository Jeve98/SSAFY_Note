"""
[251203]

<Vue 라이브 강의>

Props : 부모가 자신의 직계 자식에게 데이터를 전달하기 위해 사용하는 사용자 지정 특성으로 부모 데이터의 업데이트에 따라 데이터가 자동으로 갱신
>> 하향식 단방향 바인딩 (One-Way Data Flow)

    -Parent-
    <template>
        <CHILD ATTRIBUTE_NAME="MESSAGE"/>
    </template>

    -Child-
    <template>
        {{ATTRIBUTE_NAME}}
    </template>
    <script setup>
        defineProps({ATTRIBUTE_NAME: DATA_TYPE})     // HTML : 케밥 케이스, JS : 카멜 케이스
    </script>

!Emit : 자식이 이벤트를 발생시켜 데이터를 전달하는 기능


<실습>

Props
- 부모 : 데이터를 전송
- 자식 : 전송 받을 데이터를 정의(defineProps)하고 사용
※ ':'(v-bind)를 이용하여 동적 객체(ref)로 사용 가능

Emit
- 부모 : @자식이벤트='핸들러' 형태로 자식의 이벤트를 수신하여 정의한 함수를 실행
    
    <template>
        <TARGET @event='doit'/>
    </template>

    <script>
        const doit = function(){
            ...
        }
    </script>

- 자식 : defineEmits를 이용하여 정의한 뒤, emit으로 특정 이벤트를 발생
    
    <script>
        const emit = defineEmits(['event'])
        emit('event')
    </script>
"""