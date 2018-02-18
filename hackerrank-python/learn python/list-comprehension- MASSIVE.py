"""list comprehensions at hackerrank.com

Sample Input

1
1
1
2
Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
Concept

You already have used list in some of the previous hacks.
List comprehensions are an elegant way in which list
can be built without having to use different for loops
to append values one by one.
These examples might help.

The simplest form of a list comprehension is : 

[ expression-involving-loop-variable for loop-variable in sequence ] 

This will step over every element of sequence,
successively setting loop-variable equal
to every element one at a time, and will then build up a list
by evaluating expression-involving-loop-variable for each one.
This eliminates the need to use lambda forms,
and thus generally produces
a much more readable code than using map()
and a more compact code than using a for-loop. 


lis = [ x for x in range(10) ] # List of integers from 0 to 9
lis
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 


List comprehensions can be nested,
in which case they take on the following form: 

[ expression-involving-loop-variables for outer-loop-variable
in outer-sequence for inner-loop-variable in inner-sequence ] 
This is equivalent to writing 

results = []
for outer_loop_variable in outer_sequence:
    for inner_loop_variable in inner_sequence:
        results.append( expression_involving_loop_variables )

The final form of list comprehension involves creating a list and
filtering it similarly to
using filter(). The filtering form of list comprehension takes
the following form: 
[ expression-involving-loop-variable for loop-variable
in sequence if boolean-expression-involving-loop-variable ] 

This form is similar to the simple form of list comprehension,
but it evaluates boolean-expression-involving-loop-variable
for every item and keeps only those members for
which the boolean expression is True. 


lis = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
lis
[0, 3, 6, 9]
"""
##X, Y, Z, N = (int(raw_input()) for x in range(4))
####print X
####print Y
####print Z
##lis = [ [x,y,z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) \
##        if x + y + z is not N ]
##print lis
##

##N = int(raw_input())
##rec = set(map(int, raw_input().split()))
##
##rec = list(rec)
##rec.sort()
##print rec[-2]

N = int(raw_input())
record = []
for i in range(N):
    oneRecord = []
    oneRecord.append(raw_input())
    oneRecord.append(float(raw_input()))
    record.append(oneRecord)

