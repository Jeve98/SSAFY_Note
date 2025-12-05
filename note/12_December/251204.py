"""
[251204]

<Vue 라이브 강의>

Routing : 네트워크에서 경로를 선택하는 프로세스

Vue Router : SPA(Single Page Application)에서 페이지를 나눠주는 도구
※ SPA(Single Page Application) : 하나의 페이지 안에서 내용만 바꿔가며 보여주는 웹 앱

    App.vue : router link 생성
        
        <RouterLink to='PATH'>      // to 속성에 v-bind를 통해 '{name: NAME}'을 통해 PATH에 설정해둔 이름으로 연결 가능
        </RouterLink>

    router/index.js : 연결될 vue 선언 (path, name, component)
        
        routes: [
            {
                path: '/',
                name: 'home',
                component: HomeView,
            },
        ]

    views/~.vue : 보여줄 component(main Canvas) 생성
        
        <script>
            import { useRoute } from 'vue-router';
            import { ref } from 'vue';

            const route = useRoute()
            const userId = ref(route.params.id)
        </script>

- Dynamic Route Matching : URL의 일부를 변수로 사용하여 경로를 동적으로 매칭하는 기술

    path: '/PATH/:VARIABLE'

- Nested Routes : 중첩된 일부 component만 수정

    routes: [
        {
            path: '/',
            component: HomeView,
            children : [
                {   
                    // children이 있는 경우, 통일성을 위해, 기본 페이지를 children에 추가
                    path: '',
                    name: 'home',
                    component: DEFALUTPAGE
                },
                {
                    path: 'child',
                    name: 'child',
                    component: CHILD,
                }
            ]
        },
    ]

- Programmatic Navigation : <RouterLink>를 통한 링크 클릭 대신 JS 코드를 사용하여 페이지를 이동시키는 것
    router.push() : 다른 위치로 이동 (history stack에 추가)
    router.replace() : 현재 위치 변경 (history stack의 top 값을 재할당)

- Navigation Guard : Vue router를 통해 특정 URL에 접근할 때, 다른 URL로 redirect하거나 취소하여 navigation을 보호
    - Globally : 전역 가드, 어플리케이션 전역에서 모든 라우트 전환에 적용

        router.beforeEach((to_이동할route객체, from_현재route객체) => {
            CALLBACK_FUNCTION       // return이 없을 경우, to로 이동
        })

        // 비동기 컴포넌트의 로드 및 모든 가드의 통과가 완료된 상태에서 마지막으로 확인할 때 사용
        router.beforeResolve()

        // URL 변경 및 화면 렌더링 종료 후에 호출 (로깅 및 후처리 작업 시에 사용)
        router.afterEach()

    - Per-route : index.js의 router 내부에 선언되는 라우터 가드, 특정 라우트에만 적용

        // 다른 URL에서 탐색해 올 때만 동작
        beforeEnter: (to, from) => {
            CALLBACK_FUNCTION
        }

    - In-component : 각 컴포넌트의 <script> 내부에 선언되는 컴포넌트 가드, 컴포넌트 내에서만 적용

        // 다른 라우터로 이동하기 전에 실행
        onBeforeRouteLeave()

        // 같은 라우터 내에서 업데이트 되기 전에 실행
        onBeforeRouteUpdate()


<실습>


"""