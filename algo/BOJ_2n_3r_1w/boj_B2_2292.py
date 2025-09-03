num = int(input())

index = 0
boundary = 1
while True:
    if num <= boundary:
        print(index+1)
        break

    index += 1
    boundary += index * 6