"""
[251126]

<Vue 라이브 강의>

SPA(Single Page Application) : 단일 페이지에서 동작하는 웹 어플리케이션으로 최초 로드 시, 주요 리소스를 전부 다운로드 받은 뒤 페이지 갱신 시에 필요한 데이터만 비동기적으로 전달받아 특정 부분만 갱신
-> CSR(Client Side Rendering) 방식 : 클라이언트 측에서 동적으로 컨텐츠를 생성하고 업데이트하는 방식
>> 페이지 전환이 빠르고 서버 부하를 방지할 수 있으며 사용자 경험이 증대되고 front-back의 명확한 분리가 가능하지만 초기 로드 속도가 다소 느리고 검색 엔진 최적화(SEO) 문제가 발생

※ MPA, SSR : Django (create page, index page, delete page, ...)


Vue : JS 기반의 Client-side Frameworks 중 하나로 반응형 데이터 바인딩을 제공하는 컴포넌트 기반 아키텍처
- CDN
    <script src='https://unpkg.com/vue@3/dist/vue.global.js'></script>

    - Application instance 생성

        const { createApp } = Vue       # 구조 분해 할당 문법

        const app = createApp({
            setup(){}       # 단축 속성 문법
        })

        app.mount('MOUNT_TARGET(SELECTOR)')

    - 반응형 상태 선언 함수 'ref' : .value 속성이 있는 ref 객체로 wrapping 하여 반환하는 함수로 js 내부에서는 .value로 값에 접근이 가능하지만 html에서는 ref 객체로 접근하여도 자동으로 un-wrapping 해줌

        const { createApp, ref } = Vue       # 구조 분해 할당 문법

        const app = createApp({
            setup(){        # 단축 속성 문법
                const message = ref('hello world')

                return {
                    message      # 컴포넌트의 상태는 setup() 내에서 객체로 반환
                }
            }
        })

        app.mount('MOUNT_TARGET(SELECTOR)')

    - 이벤트 리스너

        -html-
        <button v-on: click='increment'>    # v-on으로 이벤트 리스너 생성 및 특정 동작 시에 작동할 함수명 연결

        -JS-
        setup(){
            const number = ref(0)       # 외부에 공개될 변수라면 ref 객체로 생성해야만 하지만, 내부 로직상으로만 사용된다면 일반 변수로 생성해도 무관
            const increment = function(){
                number.value ++
            }

            return {
                number,
                increment       # 동작할 함수를 함께 반환
            }
        }

- NPM : Node.js를 이용한 방법


<실습>


"""
