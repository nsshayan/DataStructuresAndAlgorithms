t = int(input())
for i in range(t):
    n = int(input())
    m = []
    p = []
    a = list(map(int,input().strip().split()))
    i = 0
    last = n-1
    while len(p)+len(m)<n:
        if i < last:
            m.append(a[i])
            p.append(a[last])
            ele_m = a[i]
            ele_p = a[last]
        while ele_m <= ele_p *2:
            i+=1
            m.append(a[i])
            ele_m += a[i]
        last-=1
#         if sum(m)<sum(p)*2:
#             m.append(a[i])
#             i+=1
#         else :
#             p.append(a[last])
#             last-=1
    print('%d %d'%(len(m),len(p)))
    if len(m)>len(p):
        print('Motu')
    elif len(m)==len(p):
        print('Tie')
    else:
        print('Patlu')
