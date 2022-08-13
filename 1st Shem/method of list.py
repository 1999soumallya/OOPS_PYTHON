list=[10,20,30,40,50,60,70,80,90]
n=len(list) # Return the leanth of a exicting list
print(n)
m=sum(list) # Return the sum of a exicting list
print(m)
print(list.index(30)) # Return the first occurrence of X in the list
list.append(100) # Add the value of X in the last posiction of a exicting list
print(list)
list.insert(10,110) # Insert the value of X in the specified posiction of I
print(list)
list1=list.copy() # Copy the exicting list into a new list which name is list1
print(list1)
list.extend(list1) # Insert all value from list1 to list 
print(list)
print(list1.count(110)) #Count all 110 in the exicting list name is list1
list1.remove(110) # Remove 110 from list1
print(list1)
print(list1.pop()) # Remove the end element from list1
print(list1) # Print the pop list
list3=[90,10,80,20,70,30,60,40,50]
list3.sort() # Sort all elements in the list3 as accending order
list3.reverse() # Print list3 in reverse order
print(list3)
list3.clear() # Remove all element form list3
print(list3)