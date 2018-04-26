T = int(raw_input())
for i in range(T):
    S = raw_input()
    suvo = 0
    suvojit = 0
    for i in range(0,len(S)):
        print "loop:",i
        if i<=len(S)-4 and S[i]=='S' and S[i+1]=='U' and S[i+2]=='V' and S[i+3]=='O':
            if i<len(S)-6 and S[i+4] == 'J' and S[i+5]=='I' and S[i+6]=='T':
                suvojit += 1
                print "incrementing suvojit:",suvojit
            else :
                suvo += 1
                print "incrementing suvo:",suvo
                
            
            
    print "SUVO = %d, SUVOJIT = %d " % (suvo,suvojit)