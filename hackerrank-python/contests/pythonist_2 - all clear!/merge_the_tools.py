"""merge the tools! at pythonist 2 at hackerrank.com
"""

def mod(elem) :
    update = ''
    s_update = ''
    for i in elem :
        if i in update or i in s_update:
            pass
        else :
            update += i
            s_update += i.lower()

##    print update
##    print s_update
    return update

string = raw_input()
num = int(raw_input())

len_s = len(string)
lst = []
div = len_s / num
##print div 
for index in range(0, len_s, num) : 
    lst.append(string[index:index + num])
##print lst
result = []
for elem in lst :
    result.append(mod(elem))
for elem in result :
    print elem
