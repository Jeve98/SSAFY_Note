# words length = N
# R * C = N, R <= C

import math

string = input()
length = len(string)

rowCount = 0
colCount = 0
for i in range(1, int(math.sqrt(length)) + 1):
    if length % i == 0:
        colCount = i
        rowCount = length // colCount

index = 0
encode = [[_ for _ in range(colCount)] for _ in range(rowCount)]
for row in range(rowCount):
    for column in range(colCount):
        encode[row][column] = string[index]
        index += 1

encodedString = ''
for column in range(colCount):
    for row in range(rowCount):
        encodedString += encode[row][column]

print(encodedString)