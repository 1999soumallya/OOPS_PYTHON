def bubble_Sort(ll):
    n=len(ll)
    for i in range(n-1):
        count=0
        for j in range(n-i-1):
            if ll[j]>ll[j+1]:
                ll[j],ll[j+1]=ll[j+1],ll[j]
                count+=1
        print("Shorted array",i+1,ll,count)
ll=[66,55,22,11,44,33]
bubble_Sort(ll)

# Create an empty array to sort integers
x= []
# Store element into the array x
print("Enter how many element do you want: ",end=" ")
n=int(input()) # Accept input into n
for i in range(n): # Repeat into n times
    print("Enter the element:",end=" ")
    x.append(int(input())) # Add the element to the array x
print("original array: ",x)
#Bubble sort
flag=False # When swipping is done, flag becomes true
for i in range(n-1): # i is from 0 to n-1
    for j in range(n-1-i): # j is from 0 to one element lesser than i
        if x[j]>x[j+1]: # If 1st element is bigger than 2nd element 
            t=x[j] # Swap j and j+1 elements
            x[j]=x[j+1]
            x[j+1]=t
            flag= True # Swapping done,hence flag is true
    if flag==False:
        break # Come out of inner for loop
    else:
        flag=False # Assign initial value to flag
print("Sorted array= ",x)