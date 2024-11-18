'''
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum()  

This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

print('ab123'.isalnum())
#prints True
print('ab123#'.isalnum())
#prints False
str.isalpha()  

This method checks if all the characters of a string are alphabetical (a-z and A-Z).

print('abcD'.isalpha())
#prints True
print('abcd1'.isalpha())
#prints False
str.isdigit()  

This method checks if all the characters of a string are digits (0-9).

print('1234'.isdigit())
#prints True
print('123edsd'.isdigit())
#prints False
str.islower()  

This method checks if all the characters of a string are lowercase characters (a-z).

print('abcd123#'.islower())
#prints True
print('Abcd123#'.islower())
#prints False
str.isupper()  

This method checks if all the characters of a string are uppercase characters (A-Z).

print('ABCD123#'.isupper())
#prints True
print('Abcd123#'.isupper())
#prints False  
Try the following example in the editor below.

You are given a string S. Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Output Format

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.

In the second line, print True if S has any alphabetical characters. Otherwise, print False.

In the third line, print True if S has any digits. Otherwise, print False.

In the fourth line, print True if S has any lowercase characters. Otherwise, print False.

In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
'''

def main():
    S = input()
    #Your code goes here
    alphanumeric = False
    alphabatic = False
    digit = False
    lowercase = False
    uppercase = False
   
    for c in S:
        if c.isalnum() and not alphanumeric:
            alphanumeric = True
        if c.isalpha() and not alphabatic:
            alphabatic = True
        if c.isdigit() and not digit:
            digit = True
        if c.islower() and not lowercase:
            lowercase = True
        if c.isupper() and not uppercase:
            uppercase = True

    print(alphanumeric)
    print(alphabatic)
    print(digit)
    print(lowercase)
    print(uppercase)

    return 0

if __name__ == '__main__':
    main()
