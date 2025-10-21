"""
[251021]

<AI 라이브 강의>

Pre training : 방대한 인터넷 속 데이터를 이용한 Self-Supervised Learning을 통해 언어 패턴, 지식 등을 학습
>> 다음 단어 예측에는 강점을 보이나 질문에 대한 답변을 한다는 보장이 없음

Post training : 사람이 원하는 방식으로 대화하고 안전하고 유용하게 만드는 단계
- Instruction Tuning : 언어모델이 사람이 내린 지시문을 따르도록 학습하는 단계로 정답 레이블을 기반으로 fine-tuning하여 다양한 태스크를 풀 수 있도록 적응하는 것에 집중
    - MMLU (Massive Multitask Language Understanding) : 사실 기반 지식, 추론 능력, 이해력에 관한 AI 벤치마크
    >> 개방형/창의적 생성과 같은 태스크에는 정답이 존재하지 않으며 사람이 생성한 정답 레이블이 최적이 아닐 수 있음 
    
- RLHF(Reinforcement Learning from Human Feedback) : 인간의 선호를 반영한 최적화
    -> 일관성이 떨어지는 인간의 판단 대신 응답 간의 비교를 통한 방식을 이용
    >> 리워드 모델링의 한계 발생 (리워드 해킹)

- DPO(Direct Preference Optimization) : 선호되는 출력과 선호되지 않는 출력을 모델이 비교하여 더 나은 것에 최적화되도록 하는 방법

- RLVR(Reinforcement Learning with Verifiable Reward) : 검증 가능한 문제에서 정답인 것과 아닌 것을 기반한 reward를 통한 강화학습
ex) Deepseek


ㅁㅁRAG(Retrieval-augmented Generation) : 정보 검색부터 답변 생성까지의 프레임워크
- Information Retrieval (정보 검색) : Query에 맞는 정보를 Datastore에서 찾아 제공하는 과정
    ex) Recommender System, 검색 증강 생성(검색된 결과-Non Parametric Knowledge를 활용한 더 정확한 답변 생성)
    - Sparse Retriever (어휘적 유사도 기반) : Query와 Non Parametricc Knowledge 간의 유사도, 관련도를 기반으로 검색하는 방법
    - Dense Retriever (의미적 유사도 기반) : 임베딩 모델을 기반으로 단어, 문장의 의미를 중심으로 검색하는 방법

검색 증강 언어 모델 (Retrieval-augmented Language Model) : 추론 시 외부 데이터 저장소(Datatore)를 활용하는 언어 모델
>> 높은 비용의 현재 지식 편집을 보다 낮은 비용으로 실행 가능하며 답변에 대한 해석이 가능하지만 검색 노이즈에 취약하고 검색 모델 성능에 의존도가 높으며 LLM의 사전지식과 컨텍스트 간의 충돌이 발생할 수 있음


Agent : 센서를 통해 환경을 인지하고 Actuator를 통해 환경에 대해 액션을 취해 영향을 미치는 것으로 간주될 수 있는 모든 것
- 도구 : 언어 모델 외부에서 실행되는 프로그램에 연결되는 함수 인터페이스로 Physical interaction-based, GUI based, Program based tool로 나뉨
    ㅁㅁ- tool learning : 모방학습

    - MCP(Model Context Protocol) : 외부 툴 활용이 급증하며 이로 인한 호환성 부족이나 낮은 재사용성을 보완하기 위한 표준화된 프로토콜
        - MCP 아키텍처
            * Host : 다수의 MCP client를 조정하고 관리하는 AI application
            * Client : MCP server로부터 컨텍스트를 가져오는 구성요소
            * Server : client에게 컨텍스트를 제공하는 프로그램
        
        - MCP Layer
            * Data : client-server 간 통신을 위한 JSON-RPC 기반 프로토콜
            * Transport : client-server 간 데이터 교환을 위한 통신 메커니즘과 채널
        
        >> 표준화, 확장성, 호환성, 재사용성, 투명성 제공

- 추론/계획 
    - Local Planning : 추론과 액션을 결합하여 환경과 상호작용하는 방식으로 매 스탭마다 하나의 툴을 결정하는 방식으로 단순하고 직관적이지만 장기 의존성 문제 발생
    - Global Planning : 실행 가능한 전체 계획 경로를 한번에 생성하여 다수의 툴을 조합한 시퀀스 형태로 결정하는 방법으로 효율적이지만 복잡한 환경에서는 문제 발생
    
    - Reflextion : 에러에서 회복하는 방법으로 수행한 궤적 평가 후, 잘못된 부분을 분석하여 재시도하는 방식
    - 계획 재검토 : 실행 도중 계획을 재검토하고 수정하는 것으로 2개의 에이전트가 서로 협력하여 오류 발생 시 재계획과 피드백을 수행하는 방식으로 장기 작업에서 안전성과 성공률이 향상됨

- 환경 표현 : 이미지, 텍스트 기반 웹 등을 통한 실시간 환경과의 상호작용
- 환경 이해 : 환경 특화 프롬프트, RAG 기반 비지도 프롬프트 유도, 탐색 기반 궤적 기억(명령어 샘플링하여 실행한 뒤, 더 정확한 새로운 명령어로 궤적을 재라벨링하며 탐색과 자기 교정을 통해 데이터 생성)을 통한 환경 이해

- 상호작용 및 의사소통


- Langchain 


<실습>

데이터 증강 : 데이터에 변형을 가해 모수를 2~3배 가량으로 증가시키는 방법
- temperature : 확률 분포의 모양을 결정 짓는 값으로 값이 낮을 수록 확률 분포의 모양이 날카로워져 같은 문양이 반복되고 반대의 경우에는 단어 선택 후보군이 넓어지는 대신 품질이 낮아짐
- top-p : 누적 p%만큼 선택하는 후보군 k의 갯수를 정하는 방법

합성 데이터 : AI와 예시를 통해 생성한 데이터
※ LLM as a judge : 주로 벤치마크 용도로 사용하나 합성 데이터의 적합성 파악에도 사용 가능


httpx : Python용 클라이언트의 HTTP 비동기 처리를 위한 라이브러리
"""