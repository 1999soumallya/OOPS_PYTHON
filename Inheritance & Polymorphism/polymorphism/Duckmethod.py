'''class dog:
    def bark(self):
        print('BOW , WOW!')
class Duck:
    def talk(self):
        print('QUACK , quack!')
class Human:
    def talk(self):
        print('Hallo , Hi!')
def call_talk(obj):
    obj.talk()
x=Duck()
call_talk(x)
x=Human()
call_talk(x)
x=dog()
call_talk(x)'''

class dog:
    def bark(self):
        print('BOW , WOW!')
class Duck:
    def talk(self):
        print('QUACK , quack!')
class Human:
    def talk(self):
        print('Hallo , Hi!')
def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
    else:
        print('Wrong object passed.......')
x=Duck()
call_talk(x)
x=Human()
call_talk(x)
x=dog()
call_talk(x)
