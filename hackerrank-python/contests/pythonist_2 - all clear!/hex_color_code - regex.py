"""hex color code at pythonist 2 at hackerrank.com
"""

"""
Problem Statement


CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code
 ■ It must start with a '#' symbol.
 ■ It can have 3 or 6 digits.
 ■ Each digit is in the range of 0 to F. (i.e. 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E and F).
 ■ A-F letters can be in lower case too. (i.e. a, b, c, d, e and f are also valid digits).
"""
import re
string = ''
lines = int(raw_input())
lst = []
for i in range(lines) :
    lst.append(raw_input())
paren_o, paren_c = 0, 0
"""
x = [m.group() for m in re.finditer('test', 'test test test test')]
print x
"""
pattern = re.compile(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}(?![0-9a-fA-F])')
result = []
for i in range(lines) :
    if '{' in lst[i] :
        paren_o += 1
    if '}' in lst[i] :
        paren_c += 1
    if paren_o != paren_c :
        x = [m.group() for m in re.finditer(pattern, lst[i])]
        result.extend(x)
    elif i == lines - 1 :
        x = [m.group() for m in re.finditer(pattern, lst[i])]
        result.extend(x)
for elem in result :
    print elem
####better code below!!!
"""
import re
string = ''
lines = int(raw_input())
lst = []
for i in range(lines) :
    lst.append(raw_input())
paren_o, paren_c = 0, 0
"""
##x = [m.group() for m in re.finditer('test', 'test test test test')]
##print x
"""
pattern = re.compile(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}(?![0-9a-fA-F])')
result = []
for i in range(lines) :
    try :
        if lst[i][0] != '#' :     
            x = [m.group() for m in re.finditer(pattern, lst[i])]
            result.extend(x) 
    except : 
        continue
for elem in result :
    print elem
"""
