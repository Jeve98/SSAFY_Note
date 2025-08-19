people = int(input())
data = list(map(int, input().split()))
data.sort()

prefix = [0 for _ in range(people + 1)]
for i in range(1, people + 1):
    prefix[i] = prefix[i-1] + data[i-1]

print(sum(prefix))