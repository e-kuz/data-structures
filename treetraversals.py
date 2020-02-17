from binarytree2 import BinaryTree
from stack2 import Stack2

tr = BinaryTree()
tr.add(5)
tr.add(6)
tr.add(8)
tr.add(0)
tr.add(1)
tr.add(4)
tr.add(2)

tr.add(11)
tr.add(7)
tr.add(7)
tr.add(-2)
tr.add(-1)
tr.add(-3)
print(tr.showTree())

tr2=BinaryTree()
tr2.add(11)
tr2.add(6)
tr2.add(15)
tr2.add(3)
tr2.add(8)
tr2.add(13)
tr2.add(17)
tr2.add(1)
tr2.add(5)
tr2.add(12)
tr2.add(14)
tr2.add(19)
print(tr2.showTree())


# preorder - root, then left, then right - root is "pre"
def preOrderRecursive(root,res):
    res.append(root.data)
    if root.left !=None:
        preOrderRecursive(root.left,res)
    if root.right !=None:
        preOrderRecursive(root.right,res)
    return res

def preOrderIterative(root):
    res = []
    stack = Stack2()
    stack.push(root)
    while stack.getSize()!=0:
        currentnode = stack.pop()
        res.append(currentnode.data)
        if currentnode.right!=None:
            stack.push(currentnode.right)
        if currentnode.left!=None:
            stack.push(currentnode.left)
    return res   
                
print("preorder recursive: ",preOrderRecursive(tr.root,[]))
print("preorder iterative: ",preOrderIterative(tr.root))
print("preorder recursive tr2: ",preOrderRecursive(tr2.root,[]))
print("preorder iterative tr2: ",preOrderIterative(tr2.root))



# inorder - left, root, right - in order
def inOrderRecursive(root,res):

    if root.left !=None:
        inOrderRecursive(root.left,res)
    res.append(root.data)
    if root.right !=None:
        inOrderRecursive(root.right,res)
    return res


def inOrderIterative(root):
    currentnode = root
    res = []
    stack = Stack2()
    stack.push(root)
    currentnode = root
    while stack.getSize()!=0 :
            pr = stack.showStack()
            pr2 = []
            for p in pr:
                if p !=None:
                    pr2.append(p.data)
                else:
                    pr2.append("none")
            if currentnode !=None:
                while currentnode.left !=None:
                    currentnode = currentnode.left
                    stack.push(currentnode)  
            currentnode = stack.pop()
            if currentnode !=None:
                res.append(currentnode.data)            
                stack.push(currentnode.right)
                currentnode = currentnode.right
    return res


print("inorder recursive: ",inOrderRecursive(tr2.root,[]))
print("inorder iterative tr2: ",inOrderIterative(tr2.root))

# postorder - left,  right, root
def postOrderRecursive(root,res):

    if root ==None:
        return res
    postOrderRecursive(root.left,res)
    postOrderRecursive(root.right,res)
    res.append(root.data)
    return res

def postOrderIterative(root,res):
    res = []
    stack = [root,]
    current = root
    
    while current.left!=None:
        current = current.left
        stack.push(current)
        
    while current.left!=None:
        current = current.left
        stack.push(current)
    

    current = stack.pop()
    res.append(current.data)
        
        

print("postorder recursive: ",postOrderRecursive(tr2.root,[]))
