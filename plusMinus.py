#Hacker Rank


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

p,z,ne=0,0,0
for i in range(0,n):
    if arr[i] > 0:
        p += 1
    elif arr[i] < 0:
        ne += 1
    else:
        z += 1 
    
print "%.6f"%(p*1.0/n)
print "%.6f"%(ne*1.0/n)
print "%.6f"%(z*1.0/n)
