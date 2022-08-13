class Node:
    def __init__(self, detaval=None):
        self.data = detaval
        self.next = None

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
        detalist = []
        if self.data is None:
            return str(detalist)
        else:
            temp = self
            detalist.append(temp.data)
            while temp.next is not None:
                temp = temp.next
                detalist.append(temp.data)
            return str(detalist)

    def length(self):
        if self.data is None:
            return 0
        else:
            temp = self
            count = 0
            while temp.next is not None:
                temp = temp.next
                count += 1
            return count

    def insert_at_first(self, dataval):
        if self.data is None:
            self.data = dataval
        else:
            newnode = Node(dataval)
            self.data, newnode.data = newnode.data, self.data
            newnode.next = self.next
            self.next = newnode
        print(f'After competing the insertion at first and the value is {dataval} ')

    def insert_at_end(self, dataval):
        if self.data is None:
            self.data = dataval
        else:
            temp = self
            while temp.next is not None:
                temp = temp.next
            newnode = Node(dataval)
            temp.next = newnode
        print(f'After competing the insertion at end and the value is {dataval} ')

    def insert_at_point(self, dataval, poc):
        if poc == 0:
            newnode = Node(dataval)
            self.data, newnode.data = newnode.data, self.data
            newnode.next = self.next
            self.next = newnode
        elif poc < 1:
            return
        elif poc > self.length():
            return
        else:
            temp = self
            count = 0
            while count < poc - 1:
                temp = temp.next
                count += 1
            newnode = Node(dataval)
            newnode.next = temp.next
            temp.next = newnode
        print(f'After inserting the value at position {poc} and the value is {dataval}')

    def insert_before(self, dataval, key):
        if self.data is None:
            return
        else:
            temp = self
            while temp.next.data != key:
                temp = temp.next
            newnode = Node(dataval)
            newnode.next = temp.next
            temp.next = newnode
        print(f'After inserting the value before {key} and the value is {dataval}')

    def insert_after(self, dataval, key):
        if self.data is None:
            return
        else:
            temp = self
            while temp.data != key:
                temp = temp.next
            newnode = Node(dataval)
            newnode.next = temp.next
            temp.next = newnode
        print(f'After inserting the value at after {key} and the value is {dataval}')

    def delete_at_first(self):
        if self.data is None:
            return
        elif self.next is None:
            self.data = None
        else:
            self.data = self.next.data
            self.next = self.next.next

    def delete_at_end(self):
        if self.data is None:
            return
        elif self.next is None:
            self.data = None
        else:
            temp = self
            while temp.next.next is not None:
                temp = temp.next
            lastnode = temp.next
            temp.next = None
            lastnode = None

    def delete_at_point(self, poc):
        if poc == 0:
            self.data = self.next.data
            self.next = self.next.next
        elif poc < 1:
            return
        else:
            temp = self
            count = 0
            while count < poc - 1:
                temp = temp.next
                count += 1
            temp.next = temp.next.next
        print(f'After deleting the value at position {poc}')

    def delete_before(self, key):
        if self.data is None:
            return
        elif self.next.data is key:
            self.delete_at_first()
        else:
            temp = self
            while temp.next.next.data != key:
                temp = temp.next
            temp.next = temp.next.next
        print(f'After deleting a node before {key}')

    def delete_after(self, key):
        if self.data is None:
            return
        elif self.data is key:
            self.delete_at_end()
        else:
            temp = self
            while temp.data is not key:
                temp = temp.next
            temp.next = temp.next.next
        print(f'After deleting a node before {key}')


if __name__ == '__main__':
    sll = Node()
    print('After creating a list => ', sll)
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.append(40)
    print('After appending all element the final linked list is => ', sll)
    print(f'Total length of a linked list is =>  {sll.length()}')
    sll.insert_at_first(5)
    print(sll)
    sll.insert_at_end(50)
    print(sll)
    sll.insert_at_point(45, 5)
    print(sll)
    sll.insert_before(15, 20)
    print(sll)
    sll.insert_after(25, 20)
    print(sll)
    sll.delete_at_first()
    print('After competing the deletion at first => ', sll)
    sll.delete_at_end()
    print('After competing the deletion at first => ', sll)
    sll.delete_at_point(2)
    print(sll)
    sll.delete_before(30)
    print(sll)
    sll.delete_after(30)
    print(sll)
