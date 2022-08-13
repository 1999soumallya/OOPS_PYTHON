class Node:
    def __init__(self, dataval=None):
        self.data=dataval
        self.next=None

    def append(self, dataval):
        if self.data==None:
            self.data=dataval
            self.next=self
        else:
            temp=self
            while temp.next!=self:
                temp=temp.next
            newnode=Node(dataval)
            temp.next=newnode
            newnode.next=self

    def __str__(self):
        datalist=[]
        if self.data==None:
            return(str(datalist))
        else:
            temp=self
            datalist.append(temp.data)
            while temp.next!=self:
                temp=temp.next
                datalist.append(temp.data)
            return(str(datalist))
    
    def insertion_at_beginning(self,dataval):
        if self.data==None:
            self.data=dataval
            self.next=self
        else:
            newnode=Node(dataval)
            self.data, newnode.data=newnode.data, self.data
            newnode.next=self.next
            self.next=newnode

    def insertion_at_end(self,dataval):
        self.append(dataval)

    def insertion_before_node(self,dataval,key):
        if self.data==key:
            self.insertion_at_beginning(dataval)
        elif self.data==None:
            return
        else:
            temp=self
            while temp.next.data!=key: 
                temp=temp.next
            newnode=Node(dataval)
            newnode.next=temp.next
            temp.next=newnode

    def insertion_after_node(self,dataval,key):
        if self.data==key:
            self.insertion_at_end(dataval)
        else:
            temp=self
            while temp.data!=key:
                temp=temp.next
            newnode=Node(dataval)
            newnode.next=temp.next
            temp.next=newnode

    def length(self):
        if self.data==None:
            return 0
        else:
            count=0
            temp=self
            while temp.next!=self:
                count+=1
                temp=temp.next
            return count

    def insertion_at_any_position(self,dataval,pos):
        if pos<1:
            return
        elif pos==0:
            self.insertion_at_beginning(dataval)
        else:
            count=0
            temp=self
            while count!=pos-1:
                temp=temp.next
                count+=1
            newnode=Node(dataval)
            newnode.next=temp.next
            temp.next=newnode

    def deleteion_at_beginning(self):
        if self.data==None:
            return
        else:  # Bypassing
            self.data=self.next.data
            self.next=self.next.next

    def delete_at_end(self):
        if self.data==None:
            return
        else:
            temp=self
            while temp.next.next!=self:
                temp=temp.next
            temp.next=self  

    def deletion_after_node(self,key):
        if self.data==key:
            self.deleteion_at_beginning()
        elif self.next.data==key:
            self.delete_at_end()
        else:
            temp=self
            while temp.next.data!=key:
                temp=temp.next
        temp.next=temp.next.next

    def deletion_before_node(self,key):
        if self.data==key:
            self.deleteion_at_beginning()
        else:
            temp=self
            while temp.next.next.data!=key:
                temp=temp.next
        temp.next=temp.next.next
    
    def deletion_at_any_position(self,pos):
        if pos==0:
            self.deleteion_at_beginning()
        elif self.next==self.length():
            self.delete_at_end()
        else:
            temp=self
            count=0
            while count!=pos:
                temp=temp.next
                count+=1
        temp.next=temp.next.next
    
    def deletion_a_node_by_value(self,dataval):
        if self.data==dataval:
            self.deleteion_at_beginning()
            return
        else:
            temp=self
            while temp.next.data!=dataval:
                temp=temp.next
        temp.next=temp.next.next
print("After createing an linklist: ")
cll=Node()
print(cll)
print("After appending all the elements: ")
cll.append(11)
cll.append(22)
cll.append(33)
cll.append(55)
print(cll)
print("After instertion at the beginning: ")
cll.insertion_at_beginning(9)
print(cll)
print("After instertion at the ending: ")
cll.insertion_at_end(66)
print(cll)
print("After instertion before a node: ")
cll.insertion_before_node(44,55)
print(cll)
print('After insert a node after a node: ')
cll.insertion_after_node(57,55)
print(cll)
print('After insert node at a position: ')
cll.insertion_at_any_position(34,3)
print(cll)
print("After deleteion at the beginning: ")
cll.deleteion_at_beginning()
print(cll)
print("After deleteion at the ending: ")
cll.delete_at_end()
print(cll)
print('After delete a node after a node: ')
cll.deletion_after_node(34)
print(cll)
print('After delete a node before a node: ')
cll.deletion_before_node(57)
print(cll)
print('After delete a node at a position: ')
cll.deletion_at_any_position(3)
print(cll)
print('After delete a node using value: ')
cll.deletion_a_node_by_value(33)
print(cll)