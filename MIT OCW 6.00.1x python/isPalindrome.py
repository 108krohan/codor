"""checks if a string is palindromic"""
def toChars(s):
    import string
    s = string.lower(s)
    ##print s
    ##print string.lowercase
    ans = ''
    for c in s :
        if c is not ' ' :
            ans = ans + c
    return ans

def isPal(s):
    if len(s) <= 1 :
        return True
    else :
        return s[0] == s[-1] and isPal(s[1:-1])

def isPalindrome(s):
    return isPal(toChars(s))

x=raw_input("Enter the string so I can tell you if it's Palindromic\t: ")
print x, " is palindromic or not? ->", isPalindrome(x)
print "Rohan Kumar is palindromic or not? ->", isPalindrome("Rohan Kumar")
print "M A D A M  is palindromic or not? ->", isPalindrome("M A D A M ")


