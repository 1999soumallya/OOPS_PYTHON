import string
import random
import pyautogui

if __name__=="__main__":
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation

    chars=[]
    chars.extend(s1)
    chars.extend(s2)
    chars.extend(s3)
    chars.extend(s4)

    password=input("Enter the password: ")
    guess_password=" "

    while guess_password!=password:
        guess_password=random.choices(chars,k=len(password))
        print("<======="+str(guess_password)+"======>")
        if(guess_password==list(password)):
            print("your password is: "+" ".join(guess_password))
            break

'''password=pyautogui.password("Enter the password: ")

guess_password= ""

while(guess_password !=password):
    guess_password=random.choices(chars,k=len(password))

    print("<======="+str(guess_password)+"======>")
    if(guess_password == list(password)):
        print("Your password is : "+ "".join(guess_password))
        break
'''