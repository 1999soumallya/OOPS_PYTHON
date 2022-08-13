print('MULTIPLE INHERITANCE USING DERACTORY')
class Father:
    hight=6.0
    @classmethod #Decorator
    def display_hight(cls):
        print("The Height is",cls.hight,"foot")
class Mother:
    colour="Brown"
    @classmethod
    def display_colour(cls):
        print("Color is",cls.colour)
class son(Father,Mother):
    pass
c=son()
print('Child\'s inherited qualities')
c.display_hight()
c.display_colour()

print('NORMAL MULTIPLE INHERITANCE')
class father:
    def height(self):
        print('The Height is 6.0 foot')
class mother:
    def colour(self):
        print('Colour is brown')
class son(father,mother):
    pass
s=son()
s.height()
s.colour()

print('MULTIPLE INHERITANCE USING CONSTRUCTOR')
class A:
    def __init__(self) -> None:
        self.a='a'
        print(self.a)
class B:
    def __init__(self) -> None:
        self.b='b'
        print(self.b)
class C(A,B):
    def __init__(self) -> None:
        super().__init__()
        self.c='c'
        print(self.c)

c=C()

print('MULTIPLE INHERITANCE USING CONSTRUCTOR AND WHEN WE ARE PRINT ALL THE ELEMENT/S')
class A:
    def __init__(self) -> None:
        self.a='a'
        print(self.a)
        super().__init__()
class B:
    def __init__(self) -> None:
        super().__init__()
        self.b='b'
        print(self.b)
class C(A,B):
    def __init__(self) -> None:
        super().__init__()
        self.c='c'
        print(self.c)

c=C()