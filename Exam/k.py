class DNode:
    def __init__(self, dataval=None):
        self.prev = None
        self.data = dataval
        self.next = None

    def append(self, dataval):
        if self.data == None:  # means DLL is empty        1
            self.data = dataval  # becomes a Singleton DLL
        else:
            temp = self
            while temp.next != None:
                temp = temp.next
            newnode = DNode(dataval)
            temp.next = newnode
            newnode.prev = temp

    def __str__(self):
        datalist = []
        if self.data == None:
            return (str(datalist))
        else:
            temp = self
            datalist.append(temp.data)
            while temp.next != None:
                temp = temp.next
                datalist.append(temp.data)
            return (str(datalist))

    def insert_at_beginning(self, dataval):
        if self.data == None:
            self.data = dataval
        else:
            newnode = DNode(dataval)
            self.data, newnode.data = newnode.data, self.data
            newnode.next = self.next
            self.next = newnode
            newnode.prev = self
            newnode.next.prev = newnode

    def delete_after(self, key):
        if self.data == None:
            return
        else:
            temp = self
            while temp.data != key:
                temp = temp.next
        temp.next.next.prev = temp
        temp.next = temp.next.next

dll=DNode()
print(dll)

dll.append(10)
dll.append(20)
dll.append(30)
print(dll)

dll.insert_at_beginning(5)
print(dll)

dll.delete_after(10)
print(dll)
