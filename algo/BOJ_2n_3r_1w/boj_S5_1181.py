wordCount = int(input())

# 최대 50글자
words = [[] for _ in range(51)]
for i in range(wordCount):
    word = input()

    # 중복 제거
    if word not in words[len(word)]:
        # 글자 수를 index로 하여 추가
        words[len(word)].append(word)

# 사전 순 정렬
for i in range(51):
    words[i].sort()

for i in range(51):
    for j in range(len(words[i])):
        print(words[i][j])
