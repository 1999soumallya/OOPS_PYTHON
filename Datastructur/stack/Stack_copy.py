class Stack:
    def __init__(self, Maxsize):
        self.arr = [None] * Maxsize
        self.top = -1
        self.Maxsize = Maxsize

    def isempty(self):
        return self.top == -1

    def isfull(self):
        return self.top == self.Maxsize - 1

    def push(self, elem):
        if self.isfull():
            print("Stack is FULL")
            return
        else:
            self.top += 1
            self.arr[self.top] = elem

    def pop(self):
        if self.isempty():
            return ("Stack is Empty")
        else:
            self.top -= 1
            return (self.arr[self.top + 1])

    def peek(self):
        return (self.arr[self.top])

    def display(self):
        dataelem = []
        if self.isempty():
            print(dataelem)
        else:
            for i in range(self.top + 1):
                dataelem.append(self.arr[i])
            print(dataelem)
