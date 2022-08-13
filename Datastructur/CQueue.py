class Queue:
    def __init__(self, MAXSIZE):
        self.arr = [None] * MAXSIZE
        self.MSize = MAXSIZE
        self.rear = self.MSize - 1
        self.front = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.MSize

    def insert(self, elem):
        if self.isFull():
            print("Queue is FULL")
            return
        else:
            self.rear = (self.rear + 1) % self.MSize
            self.arr[self.rear] = elem
            self.size += 1

    def delete(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            elem = self.arr[self.front]
            self.front += 1
            self.size -= 1
            return elem

    def print_queue(self):
        elemlist = []
        if self.isEmpty():
            return elemlist
        else:
            i = 1
            front = self.front
            while i <= self.size:
                elemlist.append(self.arr[front])
                front = (front + 1) % self.MSize
                i += 1
            return elemlist


q = Queue(5)
print(q.print_queue())
q.insert('A')
q.insert('B')
q.insert('C')
print(q.print_queue())
print(q.delete())
print(q.print_queue())
print(q.delete())
print(q.print_queue())
print(q.delete())
print(q.print_queue())
print(q.delete())
print(q.print_queue())
