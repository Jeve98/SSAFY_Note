"""
[251017]

<AI 라이브 강의>

Foundation Model : 다양한 작업에 폭넓게 활용될 수 있도록 대규모 데이터로 사전 학습된 범용 대형 AI 모델
- Creation > Curation > Training > Adaptation > Deployment
    >> 새로운 모델 '학습' 패러다임에서 학습된 모델에 대한 '활용' 패러다임으로의 시프트
- [대규모] : Transformer 모델 구조에 쉬운 데이터 수집을 기반으로 대규모 언어 데이터를 학습
- [적응성] : 높은 파인튜닝 성능
- [범용성] : 다양한 작업과 한정되지 않는 출력 지원

- 적응 활용
    - Zero-Shot : 처음 보는 문제를 추가 학습 없이 바로 적용하는 것
    - Few-Shot : 예제 일부만 제공한 뒤, 적용하는 것
    - Fine-Tuning : 모델 자체에 대한 업데이트, 최신 정보에 대한 최적화

    ex) 프롬프트 엔지니어링/튜닝, 적응 학습, 파인튜닝, ...
    - fine tuning
        - PEFT(Paremeter-Efficient Fine-Tuning) : 프롬프트 튜닝, Adaptor 모듈 추가 학습
        - Partial Fine Tuning : 일부 layer의 parameter만 변화
        - Full Fine Tuning : 모델 전체의 parameter가 변화하지만 성능 향상을 위해서는 막대한 양의 데이터 요구


VLM(Vision-Language Model)_멀티모달 언어 모델 : foundation Image/Text Encoder/Decoder를 별도 학습을 진행하는 Linear Projection으로 연결
- 멀티모달 정합 (Multi-Modal Alignment) : 서로 다른 2가지 이상의 모달리티 간의 공통된 임베이딩 벡터 공간을 구성하는 것으로 이들 간의 유사도 비교가 가능
    - ImageBIND : 각종 모달리티 공간을 공유하도록 학습

- SoM(Set of Mark) : 부족한 시각 능력을 보완하여 비약적인 성능 향상을 일으키는 트릭으로 물체 탐지, 세그멘테이션을 해줄 별도의 foundation model을 이용하여 본 이미지에 오버레이 시키는 방법 (입력의 전처리)


- CLIP(Contrastive Language Image Pre-training) : ViT 멀티모달 Foundation Model로 언어와 이미지의 유사도를 기준으로 학습되어 있으며 오디오를 포함한 6가지 모달리티 관계 학습으로 확장 가능
    - 인터넷 데이터를 통한 대조 학습 기반의 언어/이미지를 지도 학습 기반으로(HTML-img tag's alt text) 사전 학습하여 자연어 기반 시각 개념을 학습
    ※ 대조 학습 : cos 유사도를 기반으로 목표 이미지(앵커)를 대응하는 텍스트와 가깝게, 일치하지 않는 텍스트는 멀게 위치
        >> 생성된 유사도를 손실함수로 사용하여 각 입력에 대한 역전파를 수행할 경우, 크로스 모달 모델(이미지 캡셔닝, 이미지 생성)로의 변환이 가능

- SigLIP : softmax 대신 sigmoid 기반 손실함수를 사용한 모델
    >> 학습에 중요한 것은 양성인 것의 거리를 줄이는 것이지만 CLIP에서는 음성인 것과의 거리를 떨어트리는 것에 집중하는 경향이 발생하는데 이를 sigmoid 함수를 통해 영향력 제한을 걸어줌


- LLaVA : 이미지 인식과 텍스트 생성을 결합하고 fine-tuning을 적용하여 시각적 질문 응답 작업에서 뛰어난 성능을 보이고 학습이 상대적으로 쉬움

- Qwen-VLM : 다수의 이미지 입력 및 multi-language 지원이 가능한 모델
    - M-RoPE(Multi-Modal Rotary Position Embedding) : 1D 텍스트, 2D 시각, 3D 비디오에 대한 위치 민감 정보를 부여할 수 있는 기술

- InternVL : 오픈소스 VLM


sVLM
ex) smolVLM, Moondream, 갤럭시 온디바이스 AI


<실습>


"""