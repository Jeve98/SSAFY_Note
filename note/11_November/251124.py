"""
[251124]

<JS 라이브 강의>

Synchronous : 프로그램의 실행 흐름이 순차적으로 진행되는 방식 (순차적 수행)
Asynchronous : 특정 작업의 완료를 기다리지 않고 다음 작업을 즉시 실행하는 방식 (병렬적 수행)

JS : single-thread 언어로 브라우저, Node.js를 통해 비동기 처리를 구현
- w.브라우저
    - Call Stack : 함수 호출이 순서대로 쌓이는 작업 공간으로 single-thread 작업 처리
    - Web API : 브라우저에서 제공하는 runtime 환경으로 비동기 작업 처리
    - Task Queue : Web API에서 처리가 완료된 작업들의 대기열
    - Event Loop : Call Stack을 주기적으로 확인하며 빈 순간 Task Queue의 작업을 Call Stack으로 이전

    setTimeout(function FUNCNAME(){STATEMENT}, TIME)


AJAX (Asynchronous JS And XML) : 비동기적인 웹 어플리케이션 개발을 위한 기술로 현재는 XML보다 JSON 형식을 사용
- 비동기 통신
- 부분 업데이트 : DOM의 일부만 업데이트 하여 사용자 경험 향상
- 서버 부하 감소

>> 개념이자 접근 방식


Axios : 브라우저, Node.js 환경에서 사용할 수 있는 Promise 기반 HTTP 클라이언트 라이브러리
    src='https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js'

※ XHR 객체 생성 및 요청 > 응답 데이터 생성 > JSON 데이터 응답 > Promise 객체를 통해 DOM 조작
- XHR 객체 : 비동기 통신을 가능하게 하는 JS 객체
- Promise 객체 : JS의 비동기 작업 처리를 위한 객체로 최종 완료 상태와 그 결과값을 나타냄
    axios({
        method:
        url:
    })  # promise 객체
    .then((response) => {성공 시 콜백 함수})
    .catch((error) => {실패 시 콜백 함수})

    ※ then/catch는 그 동작의 결과로 또 다른 Promise 객체를 반환

>> 실현하는 구체적인 도구


비동기 콜백 : 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있도록 비동기 작업 간의 순서와 동작을 제어하는데 사용
> 콜백 지옥(pyramid of doom) 발생 : 유지보수성, 가독성 저하
>> Promise 객체를 통해 다수의 비동기 작업을 chaining하여 해결
    work1()
    .then((result1) => {
        return result2
    })
    .then((result2) => {
        return result3
    })
    ...


! 워터폴 현상


<실습>


"""
