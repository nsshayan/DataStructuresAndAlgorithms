s = raw_input()
s = list(s)
print s
if len(s)==1 and s[0] == '?':
    s[0]='a'
    
if len(s) > 1 :
    for i in range(len(s)):
        if i==0 and s[i]=='?':
            if s[i+1]=='b':
                s[i]='a'
            elif s[i+1]=='a':
                s[i]='b'
            else:
                s[i]='a'
                
        if i == len(s)-1 and s[i]=='?':
            if  s[i-1]=='a':
                s[i]='b'
            else :
                s[i]='a'
        
        if s[i]=='?':
            if s[i-1]!='a' and s[i+1]!='a':
                s[i]='a'
            else :
                s[i]='b'

print ''.join(s)