import sys

lines = sys.stdin.readlines()

e = int(lines[0])
nums = str.split(lines[1],' ')


#node for numbers to be put into Linked List
class NumberNode:
    def __init__(self,value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
    def getValue(self):
        return self.value
    
#circular LL
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def insert(self, value):
        #empty list
        if self.head == None:
            self.head = NumberNode(value,None,None)
            self.tail = self.head
        
        #nonempty list
        else:
            #make new node
            n = NumberNode(value,self.tail,None)
            #assign tails right to new node
            self.tail.right = n
            #new node is the lists new tail
            self.tail = n
            #new tail's right points to head
            self.tail.right = self.head
            #head's left points to tail
            self.head.left = self.tail
            
        #increase length after every insert
        self.length +=1
        
    def MthFromLast(self,m):
        n = self.head
        for i in range(m,0,-1):
            n = n.left
        return n.getValue()

LL = LinkedList()
    

if e > len(nums) or e <=0: 
    sys.stdout.write('NIL')
else:
    for n in nums:
        LL.insert(n)
    if e > len(nums): sys.stdout.write('NIL')
    else: sys.stdout.write(LL.MthFromLast(e))
