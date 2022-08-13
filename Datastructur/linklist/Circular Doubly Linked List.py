class DNode:
    def __init__(self,dataval=None) -> None:
        self.prev=None
        self.data=dataval
        self.next=None

    def append(self,dataval):
        if self.data==None:
            self.data=dataval
        else:
            temp=self
            while temp.next!=None:
                temp=temp.next
            newnode=DNode(dataval)
            newnode.next=temp.next
            temp.next=newnode
            newnode.prev=temp

    def __str__(self) -> str:
        datalist=[]
        if self.data==None:
            return(str(datalist))
        else:
            temp=self
            datalist.append(temp.data)
            while temp.next!=None:
                temp=temp.next
                datalist.append(temp.data)
            return(str(datalist))

    def insert_at_biginning(self,dataval):
        if self.data==None:
            self.data=dataval
        else:
            newnode=DNode(dataval)
            self.data,newnode.data=newnode.data,self.data
            newnode.next=self.next
            self.next=newnode
            newnode.prev=self
            newnode.next.prev=newnode

    def insert_at_end(self,dataval):
        self.append(dataval)

    def reverse_print(self):
        datalist=[]
        if self.data==None:
            print(datalist)
        else:
            temp=self
            while temp.next!=None:
                temp=temp.next
            datalist.append(temp.data)
            while temp.prev!=None:
                temp=temp.prev
                datalist.append(temp.data)
            print(datalist)

    def insert_before(self,dataval,key):
        if self.data==None:
            return
        else:
            temp=self
            while temp.data!=key:
                if temp.next==None:
                    return
                else:
                    temp=temp.next
        newnode=DNode(dataval)
        newnode.prev=temp.prev
        temp.prev=newnode
        newnode.next=temp
        newnode.prev.next=newnode
    
    def insert_after(self,dataval,key):
        if self.data==None:
            return
        temp=self
        while temp.data!=key:
            if temp.next==None:
                return
            else:
                temp=temp.next
        newnode=DNode(dataval)
        nxt=temp.next
        temp.next=newnode
        newnode.next=nxt
        newnode.prev=temp
        nxt.prev=newnode
    
    def insert_at_position(self,dataval,pos):
        if pos==1:
            self.insert_at_biginning(dataval)
        elif pos<1:
            return
        else:
            count=1
            temp=self
            while count<pos+1:
                temp=temp.next
                count+=1
        newnode=DNode(dataval)
        newnode.prev=temp.prev
        temp.prev=newnode
        newnode.next=temp
        newnode.prev.next=newnode

    def delete_first(self):
        if self.data==None:
            return
        elif self.next==None:
            self.data=None
        else:
            self.data,self.next.data=self.next.data,self.data
            self.next=self.next.next
            self.next.next.prev=self
    
    def delete_end(self):
        if self.data==None:
            return
        elif self.next==None:
            self.data=None
        else:
            temp=self
            while temp.next!=None:
                temp=temp.next
        temp.prev.next=None
        temp.prev=None
        
    def delete_before(self,key):
        if self.data==None:
            return
        elif self.next.data==key:
            self.delete_first()
        else:
            temp=self
            while temp.next.next.data!=key:
                temp=temp.next
        temp.next=temp.next.next
        temp.next.next.prev=temp
    
    def delete_after(self,key):
        if self.data==None:
            return
        elif self.next.data==key:
            self.delete_end()
        else:
            temp=self
            while temp.data!=key:
                temp=temp.next
        temp.next=temp.next.next
        temp.next.next.prev=temp
    
    def delete_position(self,pos):
        if self.data==None:
            return
        elif pos==0:
            self.delete_first()
        else:
            temp=self
            count=0
            while count!=pos-1:
                temp=temp.next
                count+=1
        temp.next.next.prev=temp
        temp.next=temp.next.next

print("After creating a linklist")
cdll=DNode()
print(cdll)
print("After appending all the elements in a double link list")
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.append(40)
print(cdll)
print('After insert the element at the biginning ')
cdll.insert_at_biginning(5)
print(cdll)
print('After insert the element at the end ')
cdll.insert_at_end(55)
print(cdll)
print('After reverseing the linklist ')
cdll.reverse_print()
print('After insert the element before a node')
cdll.insert_before(25,30)
print(cdll)
print('After insert the element after a node')
cdll.insert_after(35,30)
print(cdll)
print('After insert the element at the posiction')
cdll.insert_at_position(28,4)
print(cdll)
print('After delete the element at the biginning ')
cdll.delete_first()
print(cdll)
print('After delete the element at the end ')
cdll.delete_end()
print(cdll)
print('After delete the element before a element')
cdll.delete_before(35)
print(cdll)
print('After delete the element after a element')
cdll.delete_after(25)
print(cdll)
print('After delete the element at the position')
cdll.delete_position(3)
print(cdll)