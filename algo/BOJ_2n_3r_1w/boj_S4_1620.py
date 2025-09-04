pocket, problem = map(int, input().split())
dic = {}
for i in range(pocket):
    name = input()
    dic[str(i + 1)] = name
    dic[name] = i + 1

for i in range(problem):
    q = input()
    print(dic[q])
