# import sys
# sys.stdin = open('../input.txt', 'r')

people, term = map(int, input().split())

length = people + 3
queue = [0] * length
head = 0
rear = 0
for i in range(1, people + 1):
    queue[rear] = i
    rear = (rear + 1) % length

count = 1
ans = []
while head != rear:
    if count % term == 0:
        ans.append(queue[head])
        head = (head + 1) % length
    else:
        queue[rear] = queue[head]
        rear = (rear + 1) % length
        head = (head + 1) % length
    count += 1

print(f'<{ans[0]}', end='')
for i in range(1, len(ans)):
    print(f', {ans[i]}', end='')
print('>')
