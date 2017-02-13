#Toggle String(HE)

S = raw_input()

print S

toggle = ''
for i in range(len(S)):
    if ord(S[i]) >= 65 and ord(S[i]) <= 90 :
        toggle += chr(ord(S[i])+32)
    
    else :
        toggle += chr(ord(S[i])-32)

print toggle
