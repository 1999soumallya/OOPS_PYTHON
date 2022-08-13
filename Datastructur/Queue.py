class Queue:
    def __init__(self, Maxsize):
        self.arr = [None]*Maxsize
        self.front = 0
        self.size = 0
        self.MSize = Maxsize
        self.rear = Maxsize - 1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.MSize

    def insert(self, Value):
        if self.isFull():
            print('This queue is full')
            return
        else:
            self.rear = (self.rear + 1) % self.MSize
            self.arr[self.rear] = Value
            self.size += 1

    def delete(self):
        if self.isEmpty():
            print('This queue is empty')
            return
        else:
            value = self.arr[self.front]
            self.front += 1
            self.size -= 1
            return value

    def print(self):
        element = []
        if self.isEmpty():
            return element
        else:
            count = 1
            front = self.front
            while count <= self.size:
                element.append(self.arr[front])
                front = (front + 1) % self.MSize
                count += 1
            return element


Q = Queue(5)
Q.insert('A')
Q.insert('B')
Q.insert('C')
print(Q.print())
