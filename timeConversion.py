time = raw_input().strip().split(":")



if 'AM' in time[2]:
    t=''
    if int(time[0]) == 12:
           time[0]='00'
    for i in range(len(time)-1):
        t+=time[i]+':'
    t+=time[2].split("AM")[0]

else :
    t=''
    time[2]=time[2].split("PM")[0]
    k = int(time[0])+12
    if k == 24:
        k = 12
    time[0]=str(k)
    for i in range(len(time)-1):
        t+=time[i]+':'
    t+=time[2].split("PM")[0]
    
print t