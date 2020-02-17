class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

        
class BinaryTree:
    def __init__(self):
        self.size=0
        self.root = None

    def contains(self,root,elem):
        if root == None:
            return False
        if elem==root.data:
            return True
        elif elem>root.data:
            return BinaryTree.contains(self,root.right,elem)
        elif elem<root.data:
            return BinaryTree.contains(self,root.left,elem)

    def add(self,elem):
        if BinaryTree.contains(self,self.root,elem):
            print("contains",elem)
            return False
        else:
            self.root = BinaryTree.privadd(self,self.root,elem)
            self.size +=1
        

    def privadd(self,root,elem):        
        if root ==None:
            root = Node(elem,None,None)
        else:
            if elem<root.data:
                root.left = BinaryTree.privadd(self,root.left,elem)
            elif elem>root.data:
                root.right = BinaryTree.privadd(self,root.right,elem)
        return root
        

    def showTree(self):
        queue2 = [self.root]
        res = []
        for q in queue2:
            if q ==None:
                res.append("none")
            else:
                res.append(q.data)
                ql = "no left"
                if q.left !=None:
                    ql = q.left.data
                qr = "no right"
                if q.right !=None:
                    qr = q.right.data
                # print(q.data,ql,qr)
                
                queue2.append(q.left)
               
                queue2.append(q.right)
        while len(res) != 0 and res[-1]=="none":
            res = res[:-1]
        return res
        
    def findMax(self,root):
        if root ==None:
            return None
        while root.right != None:
            root = root.right
        return root
    
    def remove(self,elem):
        if not BinaryTree.contains(self,self.root,elem):
            print(elem, " not in tree")
            return False
        else:
            self.root = BinaryTree.privremove(self,self.root,elem)
            self.size -=1
    
    def privremove(self,root,elem):
        if root == None :
            return None
        
        if elem<root.data:
            root.left = BinaryTree.privremove(self,root.left,elem)
        elif elem>root.data:
            root.right = BinaryTree.privremove(self,root.right,elem)
        else:
            # found the node we eant to remove, now subcases
            if root.left ==None:
                return root.right
            elif root.right ==None:
                return root.left
            else:
                # both subtrees exist, take largest val of left tree as new root
                newroot = BinaryTree.findMax(self,root.left)
                root.data =newroot.data
                # now remove the new root from it's original place
                root.left=BinaryTree.privremove(self,root.left,newroot.data)
        return root


            
                
                
             
# testing
'''
t1 = BinaryTree()
print(t1.showTree())
t1.add(1)
print(t1.showTree())
t1.add(0)
print(t1.showTree())
t1.add(2)
print(t1.showTree())
t1.add(2)
print(t1.showTree())
t1.add(1.5)
print(t1.showTree())
t1.add(3)
print(t1.showTree())
t1.add(4)
print(t1.showTree())
t1.add(-5)
print(t1.showTree())
t1.remove(2)
print(t1.showTree())
t1.remove(-7)
print(t1.showTree())
'''
                        
            
        
        
        
            
        
        
        
        
    
