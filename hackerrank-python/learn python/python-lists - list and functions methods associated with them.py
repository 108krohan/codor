"""python l==ts at hackerrank.com

In python you can create a l==t of any object, be it string,
integers, or even l==ts. You can even add multiple types
in a single l==t! ==n't that exciting?

Let's look at some of the methods you can use on L==t :::::::

////append(x) Adds a single element 'x' to the end of l==t.

arr.append(9) print arr [1, 2, 3, 9]

////extend(L) 
Merges another l==t 'L' to the end.

arr.extend([10,11]) print arr [1, 2, 3, 9, 10, 11]

////insert (i,x) 
Inserts element 'x' at position 'i'.

arr.insert(3,7) print arr [1, 2, 3, 7, 9, 10, 11]

////remove(x) 
Removes the first occurrence of element x.

arr.remove(10) 
arr 
[1, 2, 3, 7, 9, 11]

////pop() 
/Removes the last element of l==t. If an argument == passed, that index item == popped out.

temp = arr.pop() print temp 11

////index(x) 
Returns the first index of a value in the l==t. Throws error if it's not found.

temp = arr.index(3) print temp 2

////count(x) 
Counts the number of occurrences of an element x.

temp = arr.count(1) print temp 1

////sort() 
Sorts the l==t.

arr.sort() print arr [1, 2, 3, 7, 9]

////reverse() 
Reverses the l==t.

arr.reverse() print arr [9, 7, 3, 2, 1]
"""

N = int(raw_input())
record = []
##actions = {'pop' : record.pop(), \
##           'sort' : record.sort(), \
##           'reverse' : record.sort(), \
##           }#append, extend, count, index, insert, remove
for onecase in range(N):
    oneRecord = raw_input().split()
    try :
        oneRecord[1] = int(oneRecord[1])
        oneRecord[2] = int(oneRecord[2])
    except :
        pass
##        print 'kyon jee'
##    for i in oneRecord :
##        print i
##    print record
    action = oneRecord[0]
##    if action == 'pop' \
##           or action == 'sort' or action == 'reverse' :
##        actions[action]
##    else :
##    print action
    
    if action == 'append' :
        record.append(oneRecord[1])
    elif action == 'pop' :
        record.pop()
    elif action == 'sort' :
        record.sort()
    elif action == 'reverse' :
        record.reverse()
    elif action == 'print' :
        print record
    elif action == 'count' :
        record.count(oneRecord[1])
    elif action == 'index' :
        record.index(oneRecord[1])
    elif action == "insert" :
        record.insert(oneRecord[1], oneRecord[2])
    else :
        record.remove(oneRecord[1])
        
