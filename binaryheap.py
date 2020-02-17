from linkedlist import Node

class binaryHeap:
    def __init__(self,arr=None):
        if arr ==None:
            self.heap = []
            self.size = 0
        else:
            self.size=len(arr)
            self.heap = arr
            self.heap=binaryHeap.heapify(self,arr)
            
    def heapify(self,arr):
        # for (int i = Math.max(0, (heapSize / 2) - 1); i >= 0; i--) sink(i);
        for i in reversed(range(self.size//2)):
            print("reversed, ",i)
            binaryHeap.siftDown(self,i)
        return self.heap

    # i,j are indices but compares values of elements there
    def less(self,i,j):
        return self.heap[i]<self.heap[j]

    # i,j are indices
    def swap(self,i,j):
        temp = self.heap[i]
        self.heap[i]=self.heap[j]
        self.heap[j]=temp
        print("swapping ",self.heap[i],self.heap[j],self.heap)
        
    # n is index
    def siftDown(self,n):
        while True:         
            leftchild = 2*n+1
            rightchild = 2*n+2
            smallerchild = leftchild
            if rightchild<self.size and binaryHeap.less(self,rightchild,leftchild):
                smallerchild = rightchild
            if leftchild>=self.size or self.heap[n]<self.heap[smallerchild]:
                break
            print("n:",self.heap[n],", smallerchild:",self.heap[smallerchild])

            binaryHeap.swap(self,n,smallerchild)
            n =smallerchild

    # n is index
    def siftUp(self,n):
        parent = (n-1)//2
        while n>0 and binaryHeap.less(self,n,parent):
            binaryHeap.swap(self,parent,n)
            n=parent
            parent = (n-1)//2

    # elem is data, added to first free slot = end of array
    def add(self,elem):
        print(self.heap)
        self.heap.append(elem)
        self.size+=1
        binaryHeap.siftUp(self,self.size-1)

    # n is index
    def removeAt(self,n):
        if self.size==0:
            return
        
        binaryHeap.swap(self,n,self.size-1)
        self.heap = self.heap[:-1]
        # we don't know which direction
        self.size-=1
        elem = self.heap[n]
        # get value, try sifting down
        binaryHeap.siftDown(self,n)
        # if value still the same at the same spot, try sifting up
        if  self.heap[n]== elem:
            binaryHeap.siftUp(self,n)
        
            
            
        
   
        
    

# testing
'''
a=[9,7,8,6,1,4,3,2,5]
h =binaryHeap(a)
print(h.heap)
h.add(0)
print(h.heap)

h2=binaryHeap([5])
print(h2.heap)
h2.add(0)
h2.add(4)
h2.add(6)
h2.add(1)
h2.add(0)
h2.add(9)

h2.add(2)
h3=binaryHeap([5,0,4,6,1,0,9])
print("full h3 ",h3.heap)
h3.removeAt(0)
print(h3.heap)
h3.removeAt(1)
print(h3.heap)
'''


