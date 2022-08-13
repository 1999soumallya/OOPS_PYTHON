def reverse_string(str):
    str1=" "
    for i in str:
        str1=i+str1
    return str1
str=input("Pleace enter the sring which is wanted to reverse: ")
print("The reverse string is : ",reverse_string(str))