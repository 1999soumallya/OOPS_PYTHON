'''class father:
    def __init__(self,property=0) -> None:
        self.property=property
    def display_property(self):
        print('Father\s property=',self.property)
class son(father):
    def __init__(self, property1=0,property=0) -> None:
        super().__init__(property)
        self.property1=property1
    def display_property(self):
        print('Total property of child',self.property1+self.property)

s=son(2000000.00,8000000.00)
s.display_property()'''

#another program 
class square:
    def __init__(self,x) -> None:
        self.x=x
    def area(self):
        print('Area of square=',self.x*self.x)
class rechtangle(square):
    def __init__(self,x,y) -> None:
        super().__init__(x)
        self.y=y
    def area(self):
        super().area()
        print('Area of rechtangle=',self.x*self.y)
a,b=[float(x) for x in input('Enter two measurments:').split()]
r=rechtangle(a,b)
r.area()