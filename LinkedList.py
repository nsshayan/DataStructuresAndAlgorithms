import node

class LinkedList():
    def __init__(self):
        self.root=None
        
    def add(self,data):
        if self.root==None:
            self.root =  node.node(data)
        else:
            self.addListEnd(data)
            
    def addListEnd(self,data):
        current = self.root
        while current.next!=None:
            current = current.next
        
        newNode = node.node(data)
        current.next = newNode
        
    def addListBegin(self,data):
        newNode = node.node(data)
        newNode.next = self.root
        self.root=newNode
        
    def printList(self):
        current = self.root
        printLinkedList = ""
        while current.next !=None:
            printLinkedList += str(current.data) + "->" 
            current = current.next
           
        
        print printLinkedList + str(current.data)
    
    def addListPos(self,position,data):
        current = self.root
        newNode = node.node(data)

        if position == 1:
            newNode.next = self.root
            self.root = newNode
            return
        
            
        for i in range(1,int(position)-1):
            print i
            current = current.next
        
        newNode.next = current.next
        current.next = newNode
        
        
        
    def listLength(self):
        current = self.root
        length=1
        while current.next != None:
            current=current.next
            length +=1
            
        return length
        


def main():
    L = LinkedList()
    L.add(5)
    L.add(6)
    L.add(7)
    L.addListBegin(10)
    L.printList()
    print L.listLength()
    position = raw_input("Please enter the position of the element to be inserted")
    data = raw_input("Enter the element to be inserted")
    L.addListPos(position,data)
    L.printList()


if __name__=="__main__":
    main()
        
        
    
               
        