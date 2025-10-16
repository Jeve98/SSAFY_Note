"""
[251015]

<AI 라이브 강의>

one-hot encoding : 벡터 공간에서 1인 한 원소을 제외하고 모든 원소가 0인 벡터를 의미하며 단어를 one-hot 표현으로 바꾸는 과정을 의미
- 차원의 저주 : 차원이 커질 수록 데이터가 점점 더 희소해져 활용이 어려움
- 의미적 정보 부족 : 단어 간의 유사도 측정이 불가

Word encoding : 단어를 단어 사이의 의미적 관계를 포착할 수 있는 밀집되고 연속/분산적 벡터 표현으로 나타내는 방법으로 의미적 유사성 반영이 가능
ex) Word2Vec : SG + CBOW
    - Skip-gram(SG) : 중심 단어를 통해 주변 단어를 예측하는 알고리즘으로 중심 단어 주변의 윈도우 크기만큼의 단어를 문맥으로 해석하며 작은 데이터에도 잘 동작하고 희귀 단어나 구 표현에 강하지만 학습이 느림
    - Continuous Bag of Words(CBOW) : 주변 단어를 통해 중심 단어를 예측하는 알고리즘으로 학습 속도가 빠르고 자주 나오는 단어에 강하지만 희귀 단어 표현에 약함


Sequential Data : 데이터의 입력 순서와 순서를 통해 입력되는 데이터 사이의 관계가 중요한 데이터로 순서가 중요하며 장기 의존성을 띄고 가변 길이를 가짐
ex) 오디오, 텍스트, 비디오
>> 고정된 입력 길이를 가지며 장기 의존성이 떨어지는 기존의 모델로는 처리가 난해하여 Sequential Model의 필요성 대두
    - RNN : 가변 길이를 입력으로 받을 수 있고 이전 시점의 정보를 담는 hidden state를 가진 아키텍처로 각 시점마다 recurrence 수식을 적용하여 hidden state를 업데이트하여 장기 기억을 구현함
        >> 기울기 소실 문제 : 역전파 시 앞쪽 층의 기울기가 0에 가까워져 장기 의존성 학습이 어려워지는 현상 (과거 시점의 오차 신호에 대한 더 작은 기울기)
    - LSTM : 기울기 소실 문제를 해결한 RNN 모델로 hidden state 뿐만 아니라 cell state를 추가하여 장기 정보를 별도로 저장하며 forget/input/output gate를 통해 cell state의 정보를 어떻게 사용할지 결정함


언어 모델 : 단어 시퀀스 전체에 확률을 부여하여 문장의 자연스러움을 측정하며 자연어를 생성하는 AI 모델
- N-gram 언어모델 : 연속된 n개의 단어 묶음이 얼마나 자주 등장하는지 통계를 수집하고 이를 통해 다음 단어를 예측하는 통계적 기법
- Neural Machine Translation : 인공 신경망을 이용해 기계 번역을 수행하는 방법
    - Seq2Seq : 종단 간 학습이 가능한 encoder, decoder 등 2개의 LSTM으로 이루어진 신경망 구조로 번역 뿐만 아니라, 요약, 대화, 코드 생성 등 다양한 태스크에 적용 가능한 모델
        * greedy interface : 가장 확률이 높은 단어를 선택하는 토큰 출력 방식으로 잘못된 선택을 해도 되돌릴 수 없음
        * beam search : 매 단계마다 k개의 유망한 후보를 유지하여 완성된 문장을 리스트에 추가한 후 각 후보군의 점수를 로그 확률의 합으로 구해 최종 선택하는 토큰 출력 방식
        >> 초반의 떨어지는 예측 능력을 보충하기 위해 정답 단어를 decoder 입력으로 강제로 넣어주는 teacher forcing 기법을 이용
        >> Bottleneck problem : encoder는 입력 문장 전체를 하나의 벡터로 요약하여 마지막 hidden state에 문장의 모든 의미 정보가 담기는데 이때 발생할 수 있는 정보 손실을 의미
    
        - Attention : decoder가 hidden state를 생성할 때마다 encoder의 각 hidden state와의 비교를 통해 더 적합한 단어를 생성
            >> 성능 향상 뿐만 아니라 모델의 의사결정 과정에 대한 해석 가능성을 제공하고(AI 신뢰성 향상) word alignment의 별도 학습이 필요가 없음

        - Self-Attention : RNN이 하던 정보 전달을 각 단어 간의 관계 matrix(query, key, value 벡터)와 Attention으로 대신 처리하여 장기 의존성 문제를 해결하고 병렬화를 이룸
            - QUERY Vector : 다른 단어와의 관계를 확인하고자 하는 현재 선택된 단어
            - KEY Vector : 선택된 단어와 다른 단어 간의 관련 정도
            - Value Vector : 각 단어들의 실제 의미
            
            >> 순서 정보 부재, 비선형성 부족, 미래 참조 문제 발생
                * 입력
                    - Positional Encoding : 위치 벡터를 단어 임베딩 값에 더해 최종 입력으로 사용하는 것으로 순서 정보 부재 해결
                    - Feed-Forward Network : Fully Connected + ReLU 층을 추가하여 비선형적인 표현으로 확장
                * 출력
                    - Masked Self-Attention : 미래 단어에 해당하는 항목을 마스킹하여 계산을 수행할 때 반영되지 않도록 함

    - Transformer : encoder[입력 문장의 의미적 표현으로의 변환]-decoder[인코더 표현과 지금까지 생성한 단어를 입력으로 다음 단어 예측] 구조로 설계된 신경만 모델로 n개의 decoder 블록으로 이루어짐
        * Multi-Headed Attention : 다수의 attention을 통해 다양한 관점에서 동시에 정보 파악
        * Residual Connection : 깊은 층의 학습을 위해 layer가 전체를 예측하는 것이 아닌 기존 입력과의 차이만을 학습
        * Layer Normalization
        
        >> 기존의 encoder, decoder에 사용하던 RNN을 self-attention으로 대체한 것


<실습>

tensor : torch(파이토치)의 자료구조로 np.ndarray와 유사하나 gpu를 지원하고 자동 미분 엔진과 연결되어 연산 추적을 통한 자동 미분이 가능


역전파 : 예측값의 변화에 따라 각 퍼셉트론의 weight와 bias의 변화를 계산하는 것으로 tensor를 이용할 경우, 미분값을 자동 계산하므로 해당 미분값을 이용하게 됨
>> 출력 y의 변화에 weight와 bias의 변화가 영향을 얼마나 미쳤는지를 계산하는 과정
※ 자동 미분(requires_grad=True) 중인 tensor의 경우, 값을 임의로 수정할 수 없으므로, 수동 갱신 과정에서는 with torch.no_grad(): ~~를 이용하여 자동 미분을 잠시 끌 필요가 있음


Simple Nerual Network
1. 더미 데이터 준비 (가상 함수 생성 및 정답 데이터 생성(+노이즈))
2. 파이토치의 nn.Linear를 이용하여 Shallow Nerual Network 생성
3. 파이토치의 nn에서 손실 함수 정의
4. 파이토치의 optim에서 w, b 업데이트를 위한 optimizer 정의
5. 하이퍼 파라미터 설정 및 학습 시작
    - 매 단계에서 optimizer의 미분값 초기화 (.zero_grad())
    - 모델을 통해 예측값 생성
    - loss 계산
    - loss에서 역전파 실행
    - optimizer에서 업데이트


Deep Nerual Network (Multi-Layer Perceptron)
- 활성화 함수 : 히든 레이어의 각 퍼셉트론에 적용되어 비선형성을 제공하는 함수로, 선형 퍼셉트론을 적층하기만 한다면 단순 선형 조합으로 인해 하나의 거대한 선형 조합을 생성하는 것과 다르지 않으므로 이를 방지하기 위함
1. MLP 클래스 생성
    - nn.Module 상속
    - SNN으로 layer 정의 (input, 활성화 함수, output)
    - forward 정의 (self.layers(x) 선언)
2. MLP instance 생성
※ Drop-Out : 학습 중에 히든 레이어의 일부 퍼셉트론을 정해진 비율만큼 꺼버리는 것으로 특정 퍼셉트론의 과대적합, 과소적합을 제거하기 위해 사용
"""