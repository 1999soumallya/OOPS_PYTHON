def sumofsquare(n) :
    i = 1 
    while (i * i <= n):
        j = 1
        while(j * j <= n) :
            if (i * i + j * j == n) :
                print(i, "^2 + ", j , "^2" )
                return True
            j = j + 1
        i = i + 1
    return False
   

n = int(input("Enter the number : "))
if (sumofsquare(n)) :
    print("Yes")
else :
    print( "No")
    
def sumofsquare(n):
    for i in range(n//2):
        for j in range(n//2) :
            if n==i * i + j * j:
                print(i,"^2","+",j,"^2")
                return True
    return False
   
n = int(input("Enter the number : "))
print(sumofsquare(n))
