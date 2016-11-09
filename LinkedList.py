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
        
    def printList(self):
        current = self.root
        while current.next !=None:
            print current.data 
            current = current.next
            print "->"
        
        print current.data


def main():
    L = LinkedList()
    L.add(5)
    L.add(6)
    L.add(7)
    L.printList()
    

if __name__=="__main__":
    main()
        
        
    
               
        