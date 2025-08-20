# Linear Queue
class LinearQueue:
    def __init__(self, size):
        # 마지막으로 삭제된 위치 or 가장 앞 요소의 위치
        self.front = -1
        # 마지막으로 추가된 위치
        self.rear = -1
        self.arr = [0] * size

    def enqueue(self, *args):
        for i in args:
            if self.is_full():
                print(f'Data size over Queue - fail enqueue {i}')
                break

            self.rear += 1
            self.arr[self.rear] = i

    def dequeue(self):
        if not self.is_empty():
            self.front += 1
            return self.arr[self.front]
        else:
            print('Queue is empty - fail dequeue')

    def qpeek(self):
        if not self.is_empty():
            return self.arr[self.front + 1]
        else:
            print('Queue is empty - fail qpeek')

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def is_full(self):
        if self.rear == len(self.arr) - 1:
            return True
        else:
            return False


test = LinearQueue(3)
test.enqueue(1, 2, 3, 5)
print(test.dequeue())
print(test.dequeue())
print(test.dequeue())
print(test.dequeue())
print()
test = LinearQueue(3)
test.enqueue('a', 'b')
print(test.qpeek())
print(test.dequeue())
print(test.dequeue())
test.enqueue('c')
print(test.qpeek())
print(test.dequeue())
print()


# Circular Queue
class CircularQueue:
    def __init__(self, size):
        # 공백, 포화 상태 구분을 위해 항상 빈자리를 의미
        self.front = 0
        self.rear = 0
        # front를 항상 빈자리로 둘 것이기 때문에 요청한 사이즈보다 1 크게 생성
        self.arr = [0] * (size + 1)

    def enqueue(self, *args):
        for i in args:
            if self.is_full():
                print(f'Data over queue size - fail enqueue {i}')
                break

            self.rear = (self.rear + 1) % len(self.arr)
            self.arr[self.rear] = i

    def dequeue(self):
        if self.is_empty():
            print(f'Queue is empty - fail dequeue')
            return

        self.front = (self.front + 1) % len(self.arr)
        return self.arr[self.front]

    def qpeek(self):
        if not self.is_empty():
            return self.arr[(self.front + 1) % len(self.arr)]

    def is_empty(self):
        if self.rear == self.front:
            return True
        else:
            return False

    def is_full(self):
        if (self.rear + 1) % len(self.arr) == self.front:
            return True
        else:
            return False


test = CircularQueue(3)
test.enqueue(1, 2, 3, 4)
print(test.dequeue())
print(test.dequeue())
print(test.dequeue())
print(test.dequeue())
test.enqueue('a', 'b')
print(test.qpeek())
print(test.dequeue())
print(test.dequeue())
