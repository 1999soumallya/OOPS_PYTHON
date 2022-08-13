class Node:
    def __init__(self, dataval=None):
        self.root = None
        self.next = None
        self.leftnode = None
        self.rightnode = None
        self.data = dataval

    def append(self, dataval):
        if self.data is None:
            self.data = dataval
        else:
            temp = self
            while temp.next is not None:
                temp = temp.next

            newnode = Node(dataval)
            temp.next = newnode

    def __str__(self):
        datalist = []  # List
        if self.data is None:
            return str(datalist)
        else:
            temp = self
            datalist.append(temp.data)
            while temp.next is not None:
                temp = temp.next
                datalist.append(temp.data)
            return str(datalist)


bt = Node()

bt.append(10)

print(bt)
