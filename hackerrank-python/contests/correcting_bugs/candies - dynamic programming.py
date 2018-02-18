"""candies at hackerrank.com
"""
one_index = 0
def dp_candies(studs) :

    global r, c, size, one_index
    
    ##edges
    if studs < 1 :
        c[studs] = 1
        return 1
    if studs > size - 1 :
        print 'wrong input'
        return None

    ##check from sols
    try :
        return c[studs]
    except :
        dp_candies(studs - 1)
        for elem in c :
            print c[elem],
        print ''
        i = studs
        if r[i-1] > r[i] : 
            try :
                c[i]=c[i-1]+1
            except :
                print 'excepts'
                dp_candies(i - 1)
                c[i] = c[i - 1] + 1
        if r[i+1] < r[i] : 
            try : 
                c[i]=max(c[i+1]+1, c[i])
            except :
                print'excepts'
                dp_candies(i + 1)
                c[i]=max(c[i+1]+1, c[i])
        return c[i]
        
size = int(raw_input())
r = [int(raw_input()) for i in xrange(size)]
##c = [{} for i in xrange(size)]
c = {}
dp_candies(size - 1)
min_candies = 0
for elem in c :
    min_candies += c[elem]
for elem in r :
    print elem,
print ''
print min_candies


##        if studs == size :
##            return
##        elif r[studs] == r[studs - 1] :
##            c[studs] = 1
##            one_index = studs
##        elif r[studs] > r[studs - 1] :
##            ##current elem is more than prev elem
##            c[studs] = c[studs - 1] + 1
##            curr_min = c[studs - 1] + 1
##        else :
##            ##current elem is more than prev
##            if c[studs - 1] == 1 :
##                for index in xrange(one_index, studs) :
##                    c[index] += 1
##                opitmals[studs] = 1
##            else :
##                c[studs] = c[studs - 1] - 1
##        return c[studs]

"""


Problem Statement

Alice is a kindergarden teacher. She wants to give some candies to the children in her class.  All the children sit in a line, and each  of them has a r score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher r must get more candies. Alice wants to save money, so she needs to minimize the total number of candies.

Input Format

The first line of the input is an integer N, the number of children in Alice's class. Each of the following N lines contains an integer that indicates the r of each child.

1 <= N <= 105
1 <= ri <= 105

Output Format

Output a single line containing the minimum number of candies Alice must buy.

Sample Input

3  
1  
2  
2

Sample Output

4

Explanation

Here 1, 2, 2 is the r. Note that when two children have equal r, they are allowed to have different number of candies. Hence optimal distribution will be 1, 2, 1.

"""
