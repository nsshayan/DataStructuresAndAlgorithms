import node

class BinaryTree():

    def __init__(self):
        self.root=None
    
    def add(self,data):
        newNode=node.node(data)
        if self.root == None:
            self.root= newNode
        else:
            self.addNode(self.root,newNode)
    
    def addNode(self,rootNode,newNode):
        if newNode.data < rootNode.data:
            if rootNode.left is not None:
                self.addNode(rootNode.left,newNode)
            else:
                rootNode.left = newNode
                return
        elif newNode.data >= rootNode.data:
            if rootNode.right is not None:
                self.addNode(rootNode.right,newNode)
            else:
                rootNode.right = newNode
                return
    
    
    def getRoot(self):
        return self.root

    def inorder(self,root=None):
        
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self,root=None):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self,root=None):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

def main():
    L = BinaryTree()
    L.add(5)
    L.add(7)
    L.add(6)
    L.add(3)
    L.add(4)
    L.add(2)
    L.inorder(L.getRoot())
    L.preorder(L.getRoot())
    L.postorder(L.getRoot())

if __name__=="__main__":
    main()

            
          

        
        
