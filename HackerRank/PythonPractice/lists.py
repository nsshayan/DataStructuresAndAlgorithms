if __name__ == '__main__':
    N = int(input())
    elements = []
    for _ in range(N):
        command = input().strip().split(' ')
        if command[0] == 'insert':
            elements.insert(int(command[1]), int(command[2]))
        elif command[0]=='print':
            print(elements)
        elif command[0]=='remove':
            
