# overload + operator
class BookX:
    def __init__(self,pages) -> None:
        self.pages=pages
    def __add__(self,others):
        return self.pages+others.pages
class BookY:
    def __init__(self,pages) -> None:
        self.pages=pages

b1=BookX(100)
b2=BookY(150)
print('Total pages =',b1+b2)

# overload > operator
class Ramayan:
    def __init__(self,pages) -> None:
        self.pages=pages
    def __gt__(self,others):
        return self.pages>others.pages
class Mahabharat:
    def __init__(self,pages) -> None:
        self.pages=pages
b1=Ramayan(1000)
b2=Mahabharat(1500)
if b1>b2:
    print('Ramayan has more pages')
else:
    print('Mahabharat has more pages')

# overload < operator
class IVY:
    def __init__(self,age) -> None:
        self.age=age
    def __lt__(self,others):
        return self.age<others.age
class SOUMALLYA:
    def __init__(self,age) -> None:
        self.age=age
m1=SOUMALLYA(21)
f1=IVY(20)
if f1<m1:
    print('She is Younger than Me')
else:
    print('He is Younger than She')