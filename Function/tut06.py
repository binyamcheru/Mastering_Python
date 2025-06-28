# check if a word is palindrome
def is_palindrome(str):
    str = str.lower().replace(" ","")
    return str==str[::-1]

print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))

# calculate factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))