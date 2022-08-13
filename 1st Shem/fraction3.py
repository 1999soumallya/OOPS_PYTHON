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
            self.num=int(num/com_fac)
            self.den=int(den/com_fac)
    def __str__(self):
        return(str(self.num)+"/"+str(self.den))
