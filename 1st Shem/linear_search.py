def linear_search(ll,key):
    for i in range(len(ll)):      # n
        if ll[i]==key:            # 1
            return True           # 1
    return False                  # 1

ll=[22,33,44,55,66,77,11,88]
key=int(input("Enter the element to be searched:"))
print("The location of",key,"is",linear_search(ll,key))

# T(n)=2*n+1=O(n)

# case(Best): T(n)=2*1+1=3 O(1)
#             T(n)=
# case(wast): T(n)=2*8+1=17 O(8)