# Stack 구현
class Stack:
    def __init__(self, size):
        self.top = -1
        self.arr = [0] * size
        self.length = size

    def s_push(self, *data):
        if self.length >= self.top + len(data):
            for i in range(len(data)):
                self.top += 1
                self.arr[self.top] = data[i]
        else:
            print('overflow : ', end='')

    def s_pop(self):
        if self.top >= 0:
            self.top -= 1
            return self.arr[self.top + 1]
        else:
            print('underflow : ', end='')
            return None

    def s_peek(self):
        if self.top >= 0:
            return self.arr[self.top]
        else:
            return None

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def s_clear(self):
        self.top = -1


arr = Stack(10)
print(arr.is_empty())
arr.s_push(10)
print(arr.s_peek())
print(arr.is_empty())
print(arr.s_pop())
print(arr.is_empty())
print(arr.s_pop())
arr.s_push(10, 20, 'a', 'b')
print(arr.s_pop())
arr.s_push([100, 200, 300])
print(arr.s_pop())
print(arr.s_pop())
arr.s_clear()
print(arr.is_empty())
print()


# practice problem2
txt = ['( )( )((( )))', '((( )((((( )( )((( )( ))((( ))))))',
       '())', '(()', ')(']
for i in txt:
    tmp = Stack(len(i))
    for j in range(len(i)):
        if i[j] == '(':
            tmp.s_push(i[j])
        elif i[j] == ')':
            compare = tmp.s_pop()
            if compare != '(':
                print('False')
                break
    else:
        if tmp.is_empty():
            print('True')
        else:
            print('False')
print()
