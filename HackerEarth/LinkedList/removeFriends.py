T = int(input())

for i in range(T):
    DeleteFriend = False
    N,K= [int(k) for k in input().strip().split()]
    popularity = list(map(int,input().strip().split()))
    deleteList = []
    i = 0
    while i < len(popularity)-1:
        if popularity[i]<popularity[i+1]:
            popularity.remove(popularity[i])
            DeleteFriend = True
            i = 0
    if DeleteFriend==False:
        popularity.remove(popularity[len(popularity)-1])
        
    print(popularity)    
    
        
#         if popularity[j]<popularity[j+1]:
#             deleteList.append(popularity[j])
#     for j in range(K):
#         popularity.remove(deleteList[j])
#      
#     print(str(popularity))  