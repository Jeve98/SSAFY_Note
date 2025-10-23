"""
[251023]

<AI 라이브 강의>


<실습>

PEFT : 신규 parameter를 추가하여 해당 parameter만 학습
- Adapter Tuning
- Prompt Tuning
- LoRA : hyperparameter 'r' * n size의 두 행렬을 학습하고 행렬곱하여 pre-trained parameter에 근사한 행렬을 만들어 연산하는 방법
- QLoRA : 양자화하여 경량화한 모델에 LoRA를 적용


모델 경량화
- 양자화 : 완성된 모델을 축소하는 방법으로 기본 16 bit의 값 중 일부를 4 bit 값으로 근사시켜 사용
- Pruning
"""