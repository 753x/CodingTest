count = 0

N, M = map(int, input().split())

floor = []
for _ in range(N):
    col = input()
    floor.append(list(col))

for i in range(N):
    string = ''
    for j in range(M):
        if floor[i][j] == '-':
            if floor[i][j] != string:
                count += 1
        string = floor[i][j]

for i in range(M):
    string = ''
    for j in range(N):
        if floor[j][i] == '|':
            if floor[j][i] != string:
                count += 1
        string = floor[j][i]

print(count)
