N,M = map(int,raw_input().split())
mat = []
for i in range(N):
    mat.append(map(int,raw_input().split()))

mat = zip(*mat)

for i in range(len(mat)):
    matElements = ''
    for j in range(len(mat[i])):
        matElements += str(mat[i][j])
        matElements += ' '
    print matElements    
 