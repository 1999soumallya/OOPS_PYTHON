class Stack:
    Max_Size = int(input('Enter the size =>'))

    def __init__(self):
        self.Arr = []

    def isEmpty(self):
        return self.Arr == []

    def isFull(self):
        return len(self.Arr) == Stack.Max_Size

    def Push(self, item):
        if self.isFull():
            return "Stack is FULL"
        else:
            self.Arr.append(item)

    def Pop(self):
        if self.isEmpty():
            return "Stack is EMPTY"
        else:
            return self.Arr.pop()

    def Peek(self):
        if self.isEmpty():
            return "Stack is EMPTY"
        else:
            return self.Arr[-1]

    def Display(self):
        print(self.Arr)

    def No_of_items(self):
        return len(self.Arr)


S = Stack()
print(S.Pop())
for i in range(S.Max_Size):
    n = input('Enter the elements do you want to push into the stack: ')
    S.Push(n)
S.Display()
print("Item Popped out", S.Pop())
S.Display()
print("The Peeked Item is", S.Peek())
S.Display()
print("The Size of the Stack is", S.No_of_items())

'''Discussion of this program is => At we are define the maximum size of an array and then create a constructor of 
Stack class and inside the constructor are creating a default array which is access in whole program then create a 
function 'isEmpty' in this function we are checking stack array content any elements are available or not and 
creating and function for checking the array is full or not for this checking we use a method which is 'if total length 
of an is equal with max size then it returns is full' 

Now come to the main operation of stack first one is 'push' in operation at first we are checking the stack is full 
or not if stack is full then it returns "Stack is full" Other wise it appending all the elements in the stack

second one is 'pop' in operation at first we are checking the stack is empty or not if stack is empty then it returns 
"Stack is empty" Other wise it removing the last elements in top of the stack

and another one is 'peek' in this operation returns the element at the top of the Stack at first we are checking the 
stack is empty or not if stack is empty then it returns "Stack is empty" Other wise it returns the last elements in 
top of the stack 

We are creating a function 'display', Using display method we are displaying the array after completing each Iteration

Then we want to know the final size of the stack i.e. we are creating 'No_of_items' function, In this function we are 
printing the final array size using length function '''
