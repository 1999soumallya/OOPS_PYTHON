import string
import random

if __name__=="__main__":
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation
    plan=int(input("Enter the size of your password: "))
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    print(" ".join(s[0:plan]))
    password=input("Enter your password: ")
    input_password=" "
    while input_password!=password:
        input_password=random.choices(s,k=len(password))
        print(input_password)
        if(input_password == list(password)):
            print(" ".join(password))
            break