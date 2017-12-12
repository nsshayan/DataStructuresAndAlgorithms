S = list(raw_input())

L = 0

E = ''

for i in range(len(S)-1,-1,-1):
    if int(S[i])%2==0:
        L+=1
    E = str(L) + ' ' + E
print E
    
        