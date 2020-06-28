class Node:
    def __init__(self,data,right,left):
        self.data=data
        self.right=right
        self.left=left
    def setData(self,data):
        self.data=data
    def setRight(self,right):
        self.right=right
    def setLeft(self,left):
        self.left=left
    def getData(self):
        return self.data
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
            self.root=self.insertion(data,self.root,None)
            
    def insertion(self,data,node,parent):
        if(node==None):
            return Node(data,None,None)   
        elif(data!=node.getData):
            if(data>node.getData()):
               node.setRight(self.insertion(data,node.getRight(),node))
            else:
                node.setLeft(self.insertion(data,node.getLeft(),node))
        return node
    def getMax(self):
        var=self.gettingMax(self.root)
        if(var==None):
            return var
        return var.getData()

    def gettingMax(self,node):
        if(node==None or node.getRight()==None):
            return node
        return self.gettingMax(node.getRight())
    def getMin(self):
        var=self.gettingMin(self.root)
        if(var==None):
            return var
        return var.getData()

    def gettingMin(self,node):
        if(node==None or node.getLeft()==None):
            return node
        return self.gettingMin(node.getLeft())
    def delete(self,data):
        self.root=self.deletion(data,self.root)

    def deletion(self,data,node):
        if(node==None):
            print("No se encontro el dato")
            return None
        elif(node.data==data):
            NewNode=None
            if(node.getRight()==None and node.getLeft()==None):
                return None
            elif(node.getRight()!=None):
                NewNode=self.gettingMin(node.getRight())
                node.setRight(self.deletion(NewNode.getData(),node.getRight()))
            else:
                NewNode=self.gettingMax(node.getLeft())
                node.setLeft(self.deletion(NewNode.getData(),node.getLeft()))
            node.setData(NewNode.getData())
            
        
                
        elif(data>node.data):
            node.setRight(self.deletion(data,node.getRight()))
        else:
            node.setLeft(self.deletion(data,node.getLeft()))
        return node
    def printPreOrden(self):
        self.printingPreOrden(self.root)
    def printingPreOrden(self,node):
        if(node==None):
            return
        print(node.getData())
        self.printingPreOrden(node.getLeft())
        self.printingPreOrden(node.getRight())
    def printInOrden(self):
        self.printingInOrden(self.root)
    def printingInOrden(self,node):
        if(node==None):
            return
        self.printingInOrden(node.getLeft())
        print(node.getData())
        self.printingInOrden(node.getRight())
    def printPostOrden(self):
        self.printingPostOrden(self.root)

    def printingPostOrden(self,node):
        if(node==None):
            return
        self.printingPostOrden(node.getLeft())
        self.printingPostOrden(node.getRight())
        print(node.getData())
        
t=BinaryTree()
t.getMax()
t.getMin()
t.insert(22)
t.insert(15)
t.insert(14)
t.insert(16)
t.insert(40)
t.insert(32)
t.insert(50)
print("pre orden")
t.printPreOrden()
print("In orden")
t.printInOrden()
print("post orden")
t.printPostOrden()
print("Max : "+str(t.getMax()))
print("Min : "+str(t.getMin()))
print("Deleting 22")
t.delete(22)
print("printing inorder to check")
t.printInOrden()
t.delete(50)
t.delete(14)
print("Deleting 50 and 14")
print("printing inorder to check")
t.printInOrden()
print("trying to delete 99 (no in tree)")
t.delete(99)
print("printing inOrder")
t.printInOrden()

print("Trying another tree")
p=BinaryTree()
p.insert(90)
p.insert(80)
p.insert(70)
p.printInOrden()

print("Deleting 80")
p.delete(80)
print("printing inorder to check")
p.printInOrden()


               
