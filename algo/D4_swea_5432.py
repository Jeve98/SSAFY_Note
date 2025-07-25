T = int(input())

for i in range(T):
    case = input()

    switch = False
    Letter = '('
    count = 0
    total = 0

    for Type in case:
        if Type == '(':
            count += 1

            if Letter == ')':
                Letter = '('
        else:
            count -= 1

            if Letter == '(':
                switch = True
                Letter = ')'

            if switch:
                total += count
                switch = False
            else:
                total += 1
    
    print(f"#{i+1} {total}")