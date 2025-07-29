people = int(input())
seat = input()

count = 1
passing = False
for i in range(len(seat)):
    # second L
    if passing:
        passing = False
        continue

    if seat[i] == 'S':
        count += 1
    else:
        count += 1
        passing = True

count = min(count, people)
print(count)