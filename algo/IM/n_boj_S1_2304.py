# N - pillar count (1 <= N <= 1000)
# ※ not sorting
# L H   - L : left pos, H : height (1 <= L, H <= 1000)
# ...

count = int(input())
pillars = []
for i in range(count):
    x, y = map(int, input().split())
    pillars.append((x, y))  # [0]: x, [1]: y

pillars.sort()
"""
# --- 이후의 기둥이 지속적으로 점점 더 작아진다면 문제가 발생함 ---
nextPillar = 1
vol = 0
index = 0
while index <= count:
    # 현재의 높이가 다음 기둥 높이보다 높은 경우
    if pillars[index][1] > pillars[index + nextPillar][1]:
        nextPillar += 1
        # >> 2 pointer를 기반으로 가장 높은 기둥을 향해 좌우에서 동시에 값을 합쳐나가야 함
        # 이후 가장 높은 기둥은 높이 * 1 로 면접에 포함
        if index + nextPillar == len(pillars):
            vol += (pillars[index + nextPillar - 1][0] + 1 - pillars[index][0]) * pillars[index + nextPillar - 1][1]
            vol += (pillars[index][1] - pillars[index + nextPillar - 1][1]) * 1
            break
    # 현재의 높이가 다음 기둥 높이보다 낮거나 같은 경우
    else:
        vol += (pillars[index + nextPillar][0] - pillars[index][0]) * pillars[index][1]
        index += nextPillar
        nextPillar = 1

"""
# 반례 사이트를 애용하자.
# 결국 양 사이드에서 가장 큰 놈을 찾아야한다.
height = 0
highest = 0
for i in range(len(pillars)):
    if height < pillars[i][1]:
        height = pillars[i][1]
        highest = i

vol = pillars[highest][1]
pointer = highest - 1
target = highest
while pointer >= 0:
    # left
    # 좌측 마지막 기둥까지 간 경우
    if pointer == 0:
        vol += (pillars[target][0] - pillars[pointer][0]) * pillars[pointer][1]
        print(vol, 'left pointer 0')
        break
    else:
        # 앞선 기둥보다 높거나 같을 경우
        if pillars[pointer][1] > pillars[pointer - 1][1]:
            vol += (pillars[target][0] - pillars[pointer][0]) * pillars[pointer][1]
            target = pointer
            pointer -= 1
            print(vol, 'left pointer move')
        # 앞선 기둥보다 낮을 경우
        else:
            pointer -= 1

pointer = highest + 1
target = highest
while pointer < len(pillars):
    # right
    # 우측 마지막 기둥까지 간 경우
    if pointer == len(pillars) - 1:
        vol += (pillars[pointer][0] - pillars[target][0]) * pillars[pointer][1]
        print(vol, 'right pointer 0')
        break
    else:
        # 뒷선 기둥보다 높거나 같을 경우
        if pillars[pointer][1] > pillars[pointer + 1][1]:
            vol += (pillars[pointer][0] - pillars[target][0]) * pillars[pointer][1]
            target = pointer
            pointer += 1
            print(vol, 'right pointer move')
        # 뒷선 기둥보다 낮을 경우
        else:
            pointer += 1

print(vol)
