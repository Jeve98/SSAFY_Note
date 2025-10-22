"""
[251022]

<AI 라이브 강의>

부호 크기 표현 : 최상위 sign bit 사용
-> 덧셈에서 문제 발생

2의 보수 표현

비트 폭 확장
- 부호 확장 : 최상위 비트를 복사해 상위 비트를 채움
- 제로 확장 : 상위 비트를 0으로 채움

고정 소수점 체계 : 정수부와 소수부를 n-bit 패턴에서 함께 표현하기 위해 고정된 m-bit를 소수부로 사용
-> 아주 크거나 작은 수 표현에서 과도한 양의 bit 사용 문제 발생

부동 소수점 체계 : 유효 숫자와 지수를 통해 정확함을 다소 포기하되 bit 사용량을 효과적으로 감소시킴


※ 연산 속도 : 덧셈/뺄셈 < 곱셈 < 나눗셈
- 양변에 동일한 값을 곱셈한 뒤, 마지막에 나눗셈을 1회만 동작하는 트릭만으로도 속도 향상을 구현할 수 있음
※ 부동 소수점의 경우, 곱셈 < 덧셈/뺄셈 < 나눗셈


모델 경량화 : 거대 모델 등장과 함께 더 높은 자본력이 요구되는 현재에 필요로하는 요소로 성능과의 trade-off 조절이 필요
- GPU와 궁합이 좋은 기법
    ㅁㅁ* 양자화 : 연산과 메모리 부하를 줄이는 가장 직관적인 방법
            ex) QAT, PTQ
    * Pruning : 불필요한 weight를 제거하는 방법으로 GPU상에서 속도 향상을 보기 어렵기 때문에 전용 가속기 설계가 필요
        - Unstructured : 랜덤한 weight에 대해 진행하는 pruning으로 많은 양을 pruning하여도 accuracy 보장이 가능하지만 GPU가 효과적으로 동작하기 어려움
        - Structured 
    * 지식 증류 : 매우 큰 모델에서 출발하여 이들을 teacher-student 모델에 적용하여 효과적인 작은 모델을 생성
    * Fine Tuning
        ex) LoRA(Low-Rank Adaptation) : 원본 weight를 고정하고 추가되는 low-rank weight만 학습
- GPU와 궁합이 나쁜 기법 : 전용 가속기로 효과 극대화 필요


<실습>

AI Workflow : 입력 데이터에 맞춰 AI 및 도구들을 거쳐 출력을 생성해내는 데이터 처리 flow
- LangChain : AI Workflow
    1. Prompt 입력
        - from_template : role을 user로 설정한 프롬프트만 입력값으로 사용
        - from_messages : role과 프롬프트를 각각 설정하여 입력값으로 사용하며 few-shot prompting이 가능
    2. LLM의 처리
    3. LLM의 출력을 파싱하여 출력
    ~ non-essential ~
    4. RunnableLambda : Chain 내에서 직접 구성한 함수를 사용할 수 있게 해주는 컴포넌트
    
    ※ RunnablePassthrough : 전달받은 입력값을 그대로 사용하기 위한 함수


RAG (검색 증강 생성) : LLM에 사용자 프롬프트 뿐만 아니라 검색된 관련 정보를 함께 입력값으로 추가하는 기술
>> 사내 LLM에 RAG를 도입하는 것으로 기술 유출 없이 사내 AI 활용이 가능


AI Agent : 상황에 맞는 도구를 사용하여 이를 기반으로 주어진 문제를 해결하는 것
"""