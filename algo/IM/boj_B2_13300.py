studentCount, maxPeople = map(int, input().split())

students = [[0, 0] for _ in range(6)]
for student in range(studentCount):
    sex, grade = map(int, input().split())
    students[grade - 1][sex] += 1

room = 0
for grade in range(6):
    for sex in range(2):
        tmpRoom = students[grade][sex] // maxPeople
        if students[grade][sex] % maxPeople > 0:
            tmpRoom += 1
        room += tmpRoom

print(room)
