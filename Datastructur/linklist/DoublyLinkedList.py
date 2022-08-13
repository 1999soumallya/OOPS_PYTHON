class double:
    def __init__(self, detaval=None):
        self.data = detaval
        self.next = None
        self.prev = None

    def append(self, detaval):
        if self.data is None:
            self.data = detaval
        else:
            temp = self
            while temp.next is not None:
                temp = temp.next
            newnode = double(detaval)
            newnode.prev = temp
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
        if self.next is None:
            return 0
        else:
            temp = self
            count = 0
            while temp.next is not None:
                temp = temp.next
                count += 1
            return count

    def insert_at_beginning(self, detaval):
        if self.data is None:
            self.data = detaval
        else:
            newnode = double(detaval)
            self.data, newnode.data = newnode.data, self.data
            newnode.next = self.next
            newnode.prev = self
            self.next = newnode
            self.next.prev = newnode
        print(f'After inserting the value {detaval} at the beginning of the lined list:')

    def insert_at_end(self, detaval):
        self.append(detaval)
        print(f'After inserting the value {detaval} at the end of the lined list:')

    def insert_after(self, detaval,key):
        if self.data is None:
            self.data = detaval
        else:
            temp = self
            while temp.data != key:
                temp = temp.next
            newnode = double(detaval)
            newnode.next = temp.next
            newnode.prev = temp
            temp.next = newnode
            temp.next.prev = newnode
        print(f'Inserting the value {detaval} after a node {key}:')

    def insert_before(self, detaval, key):
        if self.data is None:
            self.data = detaval
        else:
            temp = self
            while temp.next.data != key:
                temp = temp.next
            newnode = double(detaval)
            newnode.next = temp.next
            newnode.prev = temp
            temp.next = newnode
            temp.next.prev = newnode
        print(f'Inserting the value {detaval} after a node {key}:')

    def insert_at_point(self, detaval, poc):
        if poc == 0:
            newnode = double(detaval)
            self.data, newnode.data = newnode.data, self.data
            newnode.next = self.next
            newnode.prev = self
            self.next = newnode
            self.next.prev = newnode
        elif poc > self.length():
            return
        elif poc < 1:
            return
        else:
            temp = self
            count = 0
            while count < poc-1:
                temp = temp.next
                count += 1
            newnode = double(detaval)
            newnode.next = temp.next
            newnode.prev = temp
            temp.next = newnode
            temp.next.prev = newnode

    def delete_first(self):
        if self.data is None:
            return
        elif self.next is None:
            self.data = None
        else:
            self.data = self.next.data
            self.next = self.next.next

    def delete_end(self):
        if self.data is None:
            return
        else:
            temp = self
            while temp.next is not None:
                temp = temp.next



if __name__ == '__main__':
    dll = double()
    print('After creating a double linked list => ', dll)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    dll.append(50)
    print('After appending all values the double linked list is =>', dll)
    print('The length of a double lined list is =>', dll.length())
    dll.insert_at_beginning(10)
    print(dll)
    dll.insert_at_end(60)
    print(dll)
    dll.insert_after(35, 30)
    print(dll)
    dll.insert_before(25, 30)
    print(dll)
    dll.insert_at_point(45, 6)
    print(dll)
    dll.delete_first()
    print('Delete the value from the first => ', dll)
