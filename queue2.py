import linkedlist
from linkedlist import Node


class Queue2:
    def __init__(self):
        self.list = linkedlist.DoublyLinkedList()
        self.size = self.list.getSize()

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size==0

    def push(self,n):
        self.list.addLast(n)

    def pop(self):
        if not self.list.isEmpty():
            return self.list.removeFirst()

    def showQueue(self):
        return self.list.showList()
# testing
'''
s = Queue2()
print(s.showQueue())
s.push(1)
print(s.showQueue())
s.push(2)
print(s.showQueue())
s.push(3)
print(s.showQueue())
s.pop()
print(s.showQueue())
s.pop()
print(s.showQueue())
s.push(1)
print(s.showQueue())
s.push(2)
print(s.showQueue())
s.pop()
print(s.showQueue())
'''

            
    
