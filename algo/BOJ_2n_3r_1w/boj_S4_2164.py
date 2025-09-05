card = int(input())

queue = [0] * (card + 1)
head = 0
rear = 0
length = len(queue)

for i in range(1, card + 1):
    queue[rear] = i
    rear = (rear + 1) % length

returnCard = False
while rear - head != 1 and head - rear != length - 1:
    if returnCard:
        queue[rear] = queue[head]
        rear = (rear + 1) % length
    head = (head + 1) % length
    returnCard = not returnCard

print(queue[head])
