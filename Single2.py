
def generic_exception_handler(trace=False):
    from sys import exc_info
    excName,excData,excTb=exc_info();
    print(excName,excData,sep=':,flush=True')
    if trace is True:
        from traceback import print_tb
        print_tb(excTb)
        
class SNode:
    def __init__(self,init_data:int):
        if type(init_data)!=int and init_data is not None:
            raise TypeError(f'{init_data} is not of type int')
        self.data=init_data
        self.next=None
        
class SinglyLinkedList:
    def __init__(self): 
        '''
        An attribute named 'head_node' will be created in a newly allocated 
        object of class SinglyLinkedList. The attribute name will be assigned 
        to a newly allocated dummy node object of class SNode. (Note that 
        the dummy node is the one whose 'data' attribute is None)
        '''
     self.headNode = SNode(None)
     
     
    def insertStart(self,newData:int):
        '''
        @input: 
            @newData: new data to be insert at the starting position of the linked list
        newData will be encapsulated in a new SNode object and the newly allocated SNode 
        object will be positioned at the beginning after the linked list (immediately 
        next to the head node)
        '''
        if type(newData)!=int:
            raise TypeError(f'{newData} is not of the type int')
        newNode=SNode(newData)
        newNode.next=self.headNode.next 
        self.headNode.next=newNode
        
    def insertEnd(self,newData:int):
         if type(newData)!=int:
            raise TypeError(f'{newData} is not of the type int')
         run = self.headNode 
         while run.next is not None: 
            run = run.next 
         run.next = SNode(newData)
    
    def showList(self):
        print('[START]->',end='')
        run=self.headNode.next 
        while run is not None:
            print(f'[{run.data}]->',end='')
            run=run.next
        print('[END]')
 
    def searchNode(self,searchData:int):
        run=self.headNode.next
        runPrev=self.headNode
        while run is not None:
            if run.data==searchData:
                return (run,runPrev) 
            runPrev=run
            run=run.next
        return(None,None)
    
    def insertAfter(self,excitingData:int,newData:int): 
        excitingNode=self.searchNode(excitingData)
        if excitingNode is None:
             raise TypeError(f'SinglyLinkedList.insertafter():exictingData:{excitingData} not found')
        newNode=SNode(newData)
        newNode.next=excitingNode.next
        excitingNode.next=newNode
        
    def insertBefore(self,excitingData:int,newData:int):
        excitingNode,excitingNodePrev=self.searchNode(excitingData)
        if excitingNode is None:
            raise ValueError(f'SinglyLinkedList.insertAfter():existingData:{excitingData} not found')
        newNode=SNode(newData)
        excitingNodePrev.next=newNode
        newNode.next = existingNode
        
    def getStart(self) -> int: 
         if self.headNode.next is None: 
            raise ValueError('getStart() cannot be applied on empty list') 
         return self.headNode.next.data
    
    def getEnd(self) -> int:
        if self.headNode.next is None: 
            raise ValueError('getEnd() cannot be applied on empty list')
        run = self.headNode 
        while run.next is not None: 
            run = run.next 
        return run.data 
    
    def popStart(self) -> int: 
        if self.headNode.next is None: 
            raise ValueError('popStart() cannot be applied on empty list')
        fisrtNodeWithData = self.headNode.next 
        firstData = fisrtNodeWithData.data
        self.headNode.next = fisrtNodeWithData.next
        del fisrtNodeWithData
        return firstData  
    
    def popEnd(self) -> int:
        if self.headNode.next is None: 
            raise ValueError('popEnd() cannot be applied on empty list')
        runPrev = self.headNode 
        run = self.headNode.next 
        while run.next is not None: 
            runPrev = run 
            run = run.next
        lastData = run.data
        runPrev.next = None 
        del run  
        return lastData 
    
    def removeStart(self):
        if self.headNode.next is None: 
            raise ValueError('removeStart() cannot be applied on empty list')
        fisrtNodeWithData = self.headNode.next 
        self.headNode.next = fisrtNodeWithData.next
        del fisrtNodeWithData 
        
    
    def removeData(self, rData: int):
        rNode, rNodePrev = self.searchNode(rData)
        if rNode is None: 
            raise ValueError(f'Data to be removed {rData} does not exist in the list')
        rNodePrev.next = rNode.next 
        del rNode
    
    def find(self, fData: int) -> bool:
         existingNode, _ = self.searchNode(fData) 
         return existingNode is not None
     
    def length(self) -> int: 
        counter = 0 
        run = self.headNode.next 
        while run is not None: 
            counter += 1 
            run = run.next
            
        return counter
    
    def isEmpty(self) -> bool:
        return self.headNode.next is None 
    
    
print('----------------Creating a new SinglyLinkedList object-----------------')
L = SinglyLinkedList() 
print('----------------Testing for empty list----------------')
try: 
    data = L.getStart() 
except: 
    generic_exception_handler() 

try: 
    data = L.getEnd() 
except: 
    generic_exception_handler() 

try: 
    data = L.popStart() 
except: 
    generic_exception_handler() 

try: 
    data = L.popEnd() 
except: 
    generic_exception_handler() 

try: 
    data = L.removeStart() 
except: 
    generic_exception_handler() 

try: 
    data = L.removeEnd() 
except: 
    generic_exception_handler() 

n = L.length() 
print(f'Length of empty list:{n}')

b = L.isEmpty() 
print(f'L is empty: {b}')

print('----------------Testing insertStart()----------------')
for data in range(1, 6): 
    L.insertStart(data * 10) 

print('Showing list after L.insertStart():')
L.showList() 

print('----------------Testing insertEnd()----------------')
for data in range(6, 11): 
    L.insertEnd(data * 10)

print('Showing list after L.insertEnd():')
L.showList() 

print('----------------Testing insertAfter() for non-existent data----------------')
try: 
    L.insertAfter(-50, 1000)
except: 
    generic_exception_handler()

print('----------------Testing insertAfter() for middle node----------------')
L.insertAfter(10, 500)
L.showList() 

print("----------------Testing insertAfter() for the last node(boundary condition testing)----------------")
L.insertAfter(100, 1000)
L.showList() 

print('----------------Testing insertBefore() for non-existent data----------------')
try: 
    L.insertBefore(-50, 1000)
except: 
    generic_exception_handler()

print('----------------Testing insertBefore() for middle node----------------')
L.insertBefore(10, 600)
L.showList() 

print("----------------Testing insertBefore() for the first node(boundary condition testing)----------------")
L.insertBefore(50, 5000)
L.showList() 

print('----------------Testing getStart(), getEnd() on non-empty list----------------')
firstData = L.getStart() 
lastData = L.getEnd() 
print(f'First Data:{firstData}, Last Data:{lastData}')
print("Showing list after L.getStart() and L.getEnd() to prove that start and end nodes are not removed")
L.showList()

print('----------------Testing popStart(), popEnd() on non-empty list----------------')
firstData = L.popStart() 
lastData = L.popEnd() 
print(f'First Data:{firstData}, Last Data:{lastData}')
print("Showing list after L.popStart() and L.popEnd() to prove that start and end nodes are removed")
L.showList()

print('----------------Testing removeStart() and removeEnd() on non-empty list----------------')
L.removeStart() 
L.showList() 
L.removeEnd() 
L.showList() 

print('----------------Testing removeData() for non-existing data value----------------')
try:
    L.removeData(-400)
except: 
    generic_exception_handler() 

print('----------------Testing removeData() for the middle data----------------')
L.removeData(60)
L.showList() 

print('----------------Testing removeData() for the first node (boundary condition testing)----------------')
L.removeData(L.getStart())
L.showList() 

print('----------------Testing removeData() for the last node(boundary condition testing)----------------')
L.removeData(L.getEnd())
L.showList()

print('----------------Testing length()/isEmpty() on non-empty list----------------')
n = L.length() 
print(f'Length of list:{n}')

b = L.isEmpty() 
print(f'L is empty: {b}')

print('----------------END----------------')

        
        
        
        
        
                  
    