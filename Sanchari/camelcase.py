def camelcase(s):
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            print(' ', end='')
            print(s[i].lower(), end="")
        else:
            print(s[i], end="")


s = input('Enter the string: ')
camelcase(s)
