def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


numbers = int(input("Enter how many numbers you want to add"))
A = []
for i in range(numbers):
    N = int(input('Enter the values: '))
    A.append(N)

print(A)
reverseList(A, 0, numbers - 1)
print("Reversed array is: ")
print(A)
print(len(A))
