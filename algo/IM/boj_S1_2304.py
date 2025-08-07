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

nextPillar = 1
vol = 0
index = 0
while index <= count:
    # 현재의 높이가 다음 기둥 높이보다 높은 경우
    if pillars[index][1] > pillars[index + nextPillar][1]:
        nextPillar += 1
        # --- 이후의 기둥이 지속적으로 점점 더 작아진다면 문제가 발생함 ---
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

print(vol)
