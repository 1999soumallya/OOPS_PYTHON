class Stack:
    Max_Size = int(input('Enter the size =>'))

    def __init__(self):  # O(1)
        self.Arr = []

    def isEmpty(self):  # O(1)
        return self.Arr == []

    def isFull(self):  # O(1)
        return len(self.Arr) == Stack.Max_Size

    def Push(self, item):  # O(2) =>  O(1)
        if self.isFull():
            return "Stack is FULL"
        else:
            self.Arr.append(item)

    def Pop(self):  # O(1)
        if self.isEmpty():
            return "Stack is EMPTY"
        else:
            return self.Arr.pop()

    def Peek(self):  # O(1)
        if self.isEmpty():
            return "Stack is EMPTY"
        else:
            return self.Arr[-1]

    def Display(self):  # O(1)
        print(self.Arr)

    def No_of_items(self):  # O(1)
        return len(self.Arr)


S = Stack()
print(S.Pop())
S.Push('A')
S.Push('B')
S.Push('C')
S.Push('D')
S.Display()
print("Item Popped out", S.Pop())
S.Display()
print("The Peeked Item is", S.Peek())
S.Display()
print("The Size of the Stack is", S.No_of_items())
