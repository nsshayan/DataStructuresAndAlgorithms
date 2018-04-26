import fileinput

f = fileinput.input()

T = int(f.readline())
for i in range(T):
    num = f.readline()
    isTidy(num)
        
