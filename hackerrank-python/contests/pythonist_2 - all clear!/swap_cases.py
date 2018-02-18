"""swap cases at pythonist 2 at hackerrank.com
"""

def swap_case(string) : 
    ss = ''
    for i in string :
        if 65 <= ord(i) <= 90 :
            ss += chr(ord(i) + 32)
        elif 97 <= ord(i) <= 122 :
            ss += chr(ord(i) - 32)
        else :
            ss += i
    return ss


string = raw_input()
print swap_case(string)
