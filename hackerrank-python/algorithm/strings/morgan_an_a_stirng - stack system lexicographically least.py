"""Morgan and a string at hackerrank.com
"""

##def get_new_index(s, c) :
##    global stanley, cubric
##    global len_s, len_c
##    times = 1
##    global result
##    org_s, org_c = s, c
##    s += 1
##    c += 1
##    while s < len_s and c < len_c and stanley[s] == cubric[c] :
##        times += 1
##        s += 1
##        c += 1
##    if s == len_s or c == len_c :
####        print 'kaam under'
##        result += stanley[org_s + 1: s - 1]
##        print result,
##        print '\\ s and len_s', s, len_s,
##        print '\\ c and len_c', c, len_c
##        return s, org_c
##    if stanley[s] < cubric[c] :
##        result += stanley[org_s + 1:s + 1]
##        return s, org_c
##    else :
##        result += cubric[org_c + 1: c + 1]
##        return org_s, c

def t2(s, c) :
    global stanley, cubric
    global len_s, len_c
    global result
    char = stanley[s]
    times_s, times_c = 1, 1
    val_s, val_c = s, c
    s += 1
    c += 1
    reps = 1
    while stanley[s] == char and cubric[c] == char and \
          s < len_s and c < len_c :
        reps += 1
        s += 1
        c += 1
    if s == len_s and c == len_c :
        result += stanley[val_s + 1: s] + cubric[val_c + 1: c]
        return s, c
    elif s == len_s : # only stanley is dead
        if cubric[c] >= char : #cubric next char is greater than common char
            result += stanley[val_s + 1: s] + cubric[val_c + 1: c + 1]
            return s, c + 1 #stanley[remaining] + cubric[upto] char      
        else :  #cubric next char is less than common char
            result += cubric[val_c + 1: c + 1]
            return val_s, c + 1
    elif c == len_c : #only cubric is dead
        if stanley[s] >= char : #stanley next char is greater than common char
            result += cubric[val_c + 1: c] + stanley[val_s + 1: s + 1]
            return s + 1, c
        else :
            result += stanley[val_s + 1: s + 1]
            return s + 1: val_c
        
    if stanley[s] != char :

        if stanley[s] > char :
                
        else :
            
    else :
        if cubric[c] > char :
        else :
    return

cases = int(raw_input())
for _ in range(cases) :
    stanley, cubric = raw_input(), raw_input()
    index_s, index_c = 0, 0
    len_s, len_c = len(stanley), len(cubric)
    result = ''
    while index_s < len_s and index_c < len_c :
        if stanley[index_s] == cubric[index_c] :
##            result += stanley[index_s]
##            index_s, index_c = get_new_index(index_s, index_c)                    
         index_s, index_c = t2(index_s, index_c)
        elif stanley[index_s] < cubric[index_c] :
            result += stanley[index_s]
            index_s += 1
        else :
            result += cubric[index_c]
            index_c += 1
    while index_c < len_c :
        result += cubric[index_c]
        index_c += 1        
    while index_s < len_s :
        result += stanley[index_s]
        index_s += 1
    print result


"""

Problem Statement


Russian | Chinese 

Jack and Daniel are friends. Both of them like letters, especially upper-
case ones. 
 They are cutting upper-case letters from newspapers, and each one
 of them has their collection of letters stored in separate stacks. 
 One beautiful day, Morgan visited Jack and Daniel.
 He saw their collections. Morgan wondered what is the lexicographically
 minimal string, made of that two collections. He can
 take a letter from a collection when it is on the top of the stack. 
 Also, Morgan wants to use all the letters in the boys'
 collections.


Input Format


The first line contains the number of test cases, T. 
 Every next two lines have such format: the first line
 contains string A, and the second line contains string B.

Constraints 
1≤T≤5 
1≤|A|≤105 
1≤|B|≤105 
A and B contain upper-case letters only.


Output Format


Output the lexicographically minimal string S for each test case in new line.


Sample Input

2
JACK
DANIEL
ABACABA
ABACABA



Sample Output

DAJACKNIEL
AABABACABACABA



Explanation


(work in progress)

"""
