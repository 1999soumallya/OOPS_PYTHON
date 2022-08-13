class Stack:
    def __init__(self,MAXSIZE):   # O(1)
        self.Arr=[None]*MAXSIZE
        self.Top=-1
        self.size=0
        self.MSize=MAXSIZE       

    def isEmpty(self):     # O(1)
        return self.Top==-1

    def isFull(self):      # O(1)
        return self.Top == self.MSize-1
    
    def Push(self, item):  # O(1)
        if self.isFull():
            return("Stack is FULL")
        else:
            self.Top+=1
            self.Arr[self.Top]=item

    def Pop(self):         # O(1)
        if self.isEmpty():
            return("Stack is EMPTY")
        else:
            elem=self.Arr[self.Top]
            self.Top-=1
            return(elem)

    def Peek(self):        # O(1)
        if self.isEmpty():
            return("Stack is EMPTY")
        else:
            return(self.Arr[self.Top])

    def Display(self):     # O(n)
        datalist=[]
        for i in range(self.Top+1):
            datalist.append(self.Arr[i])
        print(datalist)

    def No_of_items(self): # O(1)
        return(len(self.Arr))


S=Stack(5)
print(S.Pop())
S.Push(1)
print(S.Pop())
S.Push(2)
S.Push(3)
S.Push(4)
S.Push(4)
print(S.Pop())
print(S.Pop())
S.Display()
print(S.Pop())
print(S.Pop())
S.Display()
print(S.Pop())