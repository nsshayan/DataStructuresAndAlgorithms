N = int(raw_input())

table = map(int, raw_input().split(' '))
shelf = map(int, raw_input().split(' '))

time = 0
for i in table:
    if i in shelf:
        shelf.remove(i)
        continue
    minShelf = min(shelf)
    time += abs(i-minShelf)
    shelf.remove(minShelf)
    
print time
    

    