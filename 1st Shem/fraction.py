def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
class fraction:
    def __init__(self,num=0,den=1):
        com_fac=gcd(abs(num),abs(den))
        if den<0:
            self.num=int(-num/com_fac)
            self.den=int(-den/com_fac)
        else:
            self.num=num
            self.den=den
    def display(self):
        print(self.num,"/",self.den)
    def __add__(F1,F2):                 #result=(a/b)+(c/d)=((ad+bc)/bd)
        #result = fraction()             #Here Create a temporary object
        #result.num=F1.num*F2.den + F1.den*F2.num   #result=((ad+bc)/bd)
        #result.den=F1.den*F2.den
        n=F1.num*F2.den + F1.den*F2.num   #result=((ad+bc)/bd)
        d=F1.den*F2.den
        #return result
        return fraction(n,d)
f1=fraction(-2,-3)
f2=fraction(14,16)
f3=fraction()

f1.display()
f2.display()
f3=f1+f2
f3.display()
