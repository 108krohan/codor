"""This Program converts time from 12 hour format into 24 hour format.
:::Input:::
time in the format : 12:00:00AM 01:00:33PM
:::Output:::
time in the format : 00:00:00 13:00:33
"""


time = raw_input()
newTime =''
if 'AM' in time :
    for i in time :
        if i is 'A' or i is 'a':
            break
        newTime += i
    if '12' in time[:2] :
        newTime = '00' + newTime[2:]
    print newTime
else :
    for i in time :
        if i is 'P' or i is 'p':
            break
        newTime += i
    if '12' not in newTime[:2] :
        newTime = str(int(newTime[:2]) + 12) + newTime[2:]
    #newTime[1] = str(int(newTime[1]) + 12)
    print newTime
