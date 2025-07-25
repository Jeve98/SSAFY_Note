"""
test = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(test[::-1])

# list의 요소를 역으로 넣되, 해당 요소도 list이므로 이를 해체해서 제공
print(list(map(list, zip(*test[::-1]))))
"""
def letter_convension(*args):
    result = ''
    for letter in args:
        result += str(letter)
    
    return result

T = int(input())

for i in range(T):
    size = int(input())

    arr = []
    for j in range(size):
        oneLine = list(map(int, input().split()))
        arr.append(oneLine)
    
    degree90 = list(map(list, zip(*arr[::-1])))
    degree180 = list(map(list, zip(*degree90[::-1])))
    degree270 = list(map(list, zip(*degree180[::-1])))

    print(f"#{i+1}")
    
    # 간소화
    for case in range(len(degree90)):
        print(f"{letter_convension(*degree90[case])} {letter_convension(*degree180[case])} {letter_convension(*degree270[case])}")

"""
1
3
1 2 3
4 5 6
7 8 9
"""