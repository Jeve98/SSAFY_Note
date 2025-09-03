result = 0

end = False
for i in range(10):
    num = int(input())
    
    if not end:
        if (result + num) <= 100:
            result += num
        else:
            left = 100 - result
            right = result + num - 100
        
            if left >= right:
                result += num

            end = True

print(result)