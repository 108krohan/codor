"""most common at pythonist 2 at hackerrank.com
"""

string = raw_input()
lst = [[index] for index in range(26)]
for i in range(26) :
    count = 0
    for char in string :
        if char == chr(i + 97) :
            count += 1
    lst[i].append(count)

lst.sort(key = lambda x : x[1], reverse = True)
for elem in lst[:3] :
    print chr(elem[0] + 97), elem[1]


##def change(new_r) :
##    if new_r[0][0] == new_r[1][0] :
##        if new_r[0][0] == new_r[1][0] :
##            ##all equal vals
####            print 'coming here'
##            new_r.sort()
##        else :
##            new_r[0], new_r[1] = new_r[1], new_r[0]
##    else :
##        if new_r[1][0] == new_r[2][0] :
##            new_r[1], new_r[2] = new_r[2], new_r[1]
##    
##    
##
##def mod(threes) :
##    result = []
##    for elem in threes :
####        print elem, threes[elem]
##        result.append(str(threes[elem]) + str(elem))
##    result.sort(reverse = True)
##    new_r = [[elem[0], elem[1]] for elem in result]
##    print new_r
##    change(new_r)
##    return new_r
##string = raw_input()
##freq = {}
##for key in string :
##    if key in freq :
##        freq[key] += 1
##    else :
##        freq[key] = 1
##threes = {}
##for key, value in sorted(freq.iteritems(), key = lambda (k, v) : (v, k), reverse = True)[:3] :
##    threes[key] = value
##    
##lst = mod(threes)
##
##for elem in lst :
##    print elem[1] + ' ' + elem[0]



