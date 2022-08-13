class DoubleNode:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None
        self.prev = None

    def append(self, dataval):
        if self.data == None:
            self.data = dataval
        else:
            temp = self
            while temp.next != None:
                temp = temp.next
            newnode = DoubleNode(dataval)
            newnode.next = temp.next
            temp.next = newnode
            newnode.prev = temp

    def __str__(self) -> str:
        datalist = []
        if self.data == None:
            return str(datalist)
        else:
            temp = self
            datalist.append(temp.data)
            while temp.next != None:
                temp = temp.next
                datalist.append(temp.data)
            return str(datalist)

    def insert_at_end(self, dataval):
        self.append(dataval)

    def insert_after(self, dataval, key):
        if self.data == None:
            return
        temp = self
        while temp.data != key:
            if temp.next == None:
                self.insert_at_end()
            else:
                temp = temp.next
        newnode = DoubleNode(dataval)
        nxt = temp.next
        temp.next = newnode
        newnode.next = nxt
        newnode.prev = temp
        print(f'After insert the element after {key} node and value is {dataval}')

    def delete_position(self, pos):
        if self.data == None:
            return
        elif pos == 0:
            self.data, self.next.data = self.next.data, self.data
            self.next = self.next.next
            self.next.next.prev = self
        else:
            temp = self
            count = 0
            while count != pos - 1:
                temp = temp.next
                count += 1
        temp.next.next.prev = temp
        temp.next = temp.next.next
        print(f'After delete the element at {pos}th position')

print("After creating a linkedlist")
cdll = DoubleNode()
print(cdll)
print("After appending all the elements in a double linked list")
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.append(40)
cdll.append(50)
print(cdll)
cdll.insert_after(35, 30)
print(cdll)
cdll.delete_position(3)
print(cdll)
