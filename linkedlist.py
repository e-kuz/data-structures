class Node:
    def __init__(self,data,prev,next):
        self.data = data
        self.prev = prev
        self.next = next

        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def showList(self):
        res = []
        if self.size ==0:
            return res
        else:
            trav = self.head
            for i in range(self.size):
                res.append(trav.data)
                trav = trav.next
            return res
        
    
    def addLast(self,n):
        if self.size ==0:
            self.head = self.tail = Node(n,None,None)
        else:
            self.tail.next = Node(n,self.tail,None)
            self.tail = self.tail.next
        self.size +=1

    def addFirst(self,n):
        if self.size ==0:
            self.head = self.tail = Node(n,None,None)
        else:
            self.head.prev = Node(n,None,self.head)
            self.head = self.head.prev
        self.size +=1

    def removeFirst(self):
        if self.size!=0:
            # get the data
            res = self.head.data
            
            # reset head one forward, maybe head is null
            self.head = self.head.next
            self.size -=1
            if self.size ==0:
                self.tail = None
                self.head = None
            # if head is a Node, set this node's prev to none
            else:
                self.head.prev = None
            return res


    def removeLast(self):
            
        if self.size!=0:
            res = self.tail.data

            # reset tail backwards, maybe tail is null
            self.tail = self.tail.prev
            self.size -=1
            if self.size ==0:
                self.head = None
                self.tail = None
            else:
                self.tail.next = None
            return res
            
            

    def clear(self):
        trav = self.head
        while trav != None:
            travnext = trav.next
            trav.prev = None
            trav.next = None
            trav.data = None
            trav = travnext
        self.head = self.tail = None
        self.size = 0

    def removeNode(self,node):
        if node.prev == None:
            return DoublyLinkedList.removeFirst(self)
        elif node.next == None:
            return DoublyLinkedList.removeLast(self)
        else:
            res = node.data
            node.next.prev = node.prev
            node.prev.next = node.next
            self.size -=1
            return res

    def removeAt(self,index):
        if index<self.size/2:
            trav = self.head
            for i in range(index):
                trav = trav.next
        else:
            trav = self.tail
            for i in range(self.size-1,index-1,-1):
                trav=trav.prev
        return DoublyLinkedList.removeNode(self,trav)
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size==0
                
        

# testing
'''
dl = DoublyLinkedList()
print(dl,dl.tail)
dl.addLast(5)
dl.addLast(6)
dl.addLast(7)
dl.addFirst(4)
dl.addFirst(3)
dl.addFirst(2)
dl.addFirst(1)
print(dl,dl.showList())
dl.removeFirst()
print(dl,dl.showList())
dl.removeLast()
print(dl,dl.showList())
print(dl.head.data,dl.tail.data)

'''



        
