def countOccurrences(str, word):
    a = str.split(" ")
    count = 0
    for i in range(0, len(a)):
        if word == a[i]:
            count = count + 1
    return count


str = input("Enter your full Sentence: ")
word = input('Enter your Searching word')
print(countOccurrences(str, word))