people = int(input())
shirt = list(map(int, input().split()))
shirtMin, penMin = map(int, input().split())

shirtAns = 0
for i in range(len(shirt)):
    shirtAns += shirt[i] // shirtMin
    if shirt[i] % shirtMin > 0:
        shirtAns += 1

penAns = people // penMin

print(shirtAns)
print(penAns, people % penMin)
