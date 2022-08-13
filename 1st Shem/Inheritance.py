# Single Inheritance
'''class A:
    def feature1(self):
        print("The feature 1 is working")
    def feature2(self):
        print("The feature 2 is working")
class B(A):
    def feature3(self):
        print("The feature 3 is working")
a1=A()
a1.feature1()
a1.feature2()


b1=B()
b1.feature1()
b1.feature2()
b1.feature3()'''
# Multipal Inheritance
class A:
    def feature1(self):
        print("The feature 1 is working")
    def feature2(self):
        print("The feature 2 is working")
class B:
    def feature3(self):
        print("The feature 3 is working")
    def feature4(self):
        print("The feature 4 is working")
    def feature5(self):
        print("The feature 5 is working")
class C(A,B):
    def feature6(self):
        print("The feature 6 is working")
    def feature7(self):
        print("The feature 7 is working")
a1=A()
a1.feature1()
a1.feature2()


b1=B()
b1.feature3()
b1.feature4()
b1.feature5()

c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()
c1.feature7()