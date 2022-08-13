class mainstack:
    def __init__(self):
        self.item = []
        self.size = int(input('Enter the size of the stack => '))

    def isEmpty(self):
        return self.item == []

    def isFull(self):
        return len(self.item) == self.size

    def push(self, data):
        if self.isFull():
            return 'Stack is Full'
        else:
            return self.item.append(data)

    def pop(self):
        if self.isEmpty():
            return 'Stack is Empty'
        else:
            return self.item.pop()

    def peek(self):
        if self.isEmpty():
            return 'Stack is Empty'
        else:
            return self.item[-1]

    def Display(self):
        print(self.item)

    def No_item(self):
        return len(self.item)


S = mainstack()
print('The item is pushed up: ')
S.push('A')
S.push('B')
S.push('C')
S.push('D')
S.Display()
print('The item is popped up: ', S.pop())
S.Display()
print('The item is peeked up: ', S.peek())
S.Display()
print('The Size of the Stack is => ', S.No_item())
