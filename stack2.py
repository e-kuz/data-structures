import linkedlist
from linkedlist import Node


class Stack2:
    def __init__(self):
        self.list = linkedlist.DoublyLinkedList()
        self.size = self.list.getSize()

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size==0

    def push(self,n):
        self.list.addLast(n)
        self.size+=1

    def pop(self):
        if not self.list.isEmpty():
            self.size-=1
            return self.list.removeLast()
        

    def showStack(self):
        res = []
        if self.size ==0:
            return res
        else:
            trav = self.list.head
            for i in range(self.list.size):
                res.append(trav.data)
                trav = trav.next
        return res

# testing
'''
s = Stack2()
print(s.showStack())
s.push(1)
print(s.showStack())
s.push(2)
print(s.showStack())
s.push(3)
print(s.showStack())
s.pop()
print(s.showStack())
s.pop()
print(s.showStack())
s.pop()
print(s.showStack())
s.push(1)
print(s.showStack())
s.push(2)
print(s.showStack())
s.pop()
print(s.showStack())
s.pop()
print(s.showStack())
s.pop()
print(s.showStack())
s.pop()
print(s.showStack())

'''        
    
