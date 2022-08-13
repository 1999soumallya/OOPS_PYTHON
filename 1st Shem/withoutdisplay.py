def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
class fraction:
    def __init__(self,num=0,den=1):
        com_fact=gcd(abs(num),abs(den))
        if den<0:
            self.num=int(-num/com_fact)
            self.den=int(-den/com_fact)
        else:
            self.num=int(num/com_fact)
            self.den=int(den/com_fact)
    def __str__(self):
        return (str(self.num)+"/"+str(self.den))
    def __add__(F1,F2):
        n=F1.num*F2.den+F1.den*F2.num
        d=F1.den*F2.den
        return fraction(n,d)
f1=fraction(-2,-4)
f2=fraction(4,6)
f3=fraction()

f3=f1+f2
print(f1)
print(f2)
print(f3)
