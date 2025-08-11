days, interval = map(int, input().split())
temperature = list(map(int, input().split()))

prefix = [0] * (days + 1)

for i in range(1, days + 1):
    prefix[i] = prefix[i - 1] + temperature[i - 1]

ans = -2100000000
for i in range(interval, days + 1):
    tmpMax = prefix[i] - prefix[i - interval]
    if ans < tmpMax:
        ans = tmpMax

print(ans)
