class DNode:
    def __init__(self,dataval=None):
        self.prev=None
        self.data=dataval
        self.next=None

    def append(self,dataval):  
        if self.data==None:    # means DLL is empty        1  
            self.data=dataval  # becomes a Singleton DLL       
        else:
            temp=self                                                         
            while temp.next!=None:                  
                temp=temp.next
            newnode=DNode(dataval)   
            temp.next=newnode         
            newnode.prev=temp         

    def __str__(self):
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
            
    def insert_at_beginning(self, dataval):
        if self.data==None:
            self.data=dataval
        else:
            newnode=DNode(dataval)
            self.data, newnode.data = newnode.data, self.data
            newnode.next=self.next
            self.next=newnode
            newnode.prev=self
            newnode.next.prev=newnode

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

    def insert_before(self, dataval,key):
        if self.data==None:
            return
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
    def insert_at_position(self, dataval, pos):
        if pos==1:
            self.insert_at_begin(dataval)
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
    def insert_after(self, dataval, key):
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
    def delete_first(self):
        if self.data==None:
            return
        elif self.next==None:
            self.data=None
        else:
            self.data, self.next.data = self.next.data, self.data
            self.next=self.next.next
            self.next.next.prev=self
    def delete_last(self):
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
    def delete_at_position(self, pos):
        if self.data==None:
            return
        elif self.next==pos:
            self.data=self.next.data
            self.next=self.next.next
        else:
            count=1
            temp=self
            while count<pos:
                temp=temp.next
                count+=1
        temp.next.prev=None
        temp.next=temp.next.next
    def delete_after(self, key):
        if self.data==None:
            return
        else:
            temp=self
            while temp.data!=key:
                temp=temp.next
        temp.next.next.prev=temp
        temp.next=temp.next.next
    def delete_before(self, key):
        if self.data==None:
            return
        elif self.next==key:
            self.delete_first()
        else:
            temp=self
            while temp.next.next.data!=key:
                temp=temp.next
        temp.next.next.prev=temp
        temp.next=temp.next.next
dll=DNode()
print(dll)

dll.append(10)
dll.append(20)
dll.append(30)
print(dll)

dll.insert_at_beginning(5)
print(dll)
dll.reverse_print()

dll.insert_before(8,10)
print(dll)

dll.insert_at_position(15,3)
print(dll)

dll.insert_after(12,20)
print(dll)

dll.delete_first()
print(dll)

dll.delete_last()
print(dll)

dll.delete_at_position(2)
print(dll)

dll.delete_after(10)
print(dll)

dll.delete_before(12)
print(dll)