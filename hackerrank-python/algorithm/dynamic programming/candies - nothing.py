"""candies at hackerrank.com
"""

##the one with the higher rating must get more candies

num_children = int(raw_input())
rating = [int(raw_input()) for i in range(num_children)]
candy_level = 1
table = [0 for i in range(num_children)]
table[0] = 1
for index in range(1, num_children) :
    if rating[index] == rating[index - 1] :
        candy_level = 1
        table[index] = candy_level
    if rating[index] > rating[index - 1] :
        candy_level += 1
        table[index] = candy_level
##        print 'in if table =', table
    else :
        candy_level = 1
        table[index] = 1
##        print 'in else table =', table
candy_level = 1
print rating
print table

for index in range(num_children - 1, 0, -1) :
    if table[index] == 1 :
##        print 'table index is 1 at index :', index
        while index > 0 and table[index - 1] == 1 :
            table[index - 1] += candy_level
            candy_level += 1
            index -= 1
##        print 'table[index] >= table[index - 1]', table[index], table[index - 1]
##        print table
    if table[index] >= table[index - 1] and rating[index] < rating[index - 1] :
        difference = table[index] - table[index - 1] + (table[index] - table[index - 1])%2
##            print difference 
##            while index > 0 and table[index - 1] != 1 :
        table[index - 1] += difference
##                    index -= 1
##            print 'in while table =', table
        candy_level = 1
print rating
print table
print sum(table)


                        








##for index in range(0, num_children) : 
####    child = rating[index]
##    try :
##        if rating[index] > rating[index - 1] :
##            candy_level += 1
##            candies += candy_level
##            print candy_level,
####            print candy_level,
##    except :
##        pass
##    else :
##        pivot = index + 1
##        curr_level = candy_level
##        candy_level = 0
##        while index + 1 < num_children and rating[index] > rating[index + 1] :
##            candy_level += 1
##            print candy_level,
##            index += 1
##        if candy_level > curr_level :
##            candies += pivot
####            print 'candy_level > curr_level'
##        candies += candy_level
##        print candy_level,
##        candy_level = 1
####        print candy_level
####        print candies
##        
####    prev_child = child
####    print candy_level,
##print candies
"""

Problem Statement


Alice is a kindergarden teacher. She wants to give some candies to the children in her class.  All the children sit in a line, and each  of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to save money, so she needs to minimize the total number of candies.


Input Format


The first line of the input is an integer N, the number of children in Alice's class. Each of the following N lines contains an integer that indicates the rating of each child.

1 <= N <= 105 
 1 <= ratingi <= 105 


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


Here 1, 2, 2 is the rating. Note that when two children have equal
rating, they are allowed to have different number of candies. Hence
optimal distribution will be 1, 2, 1.

"""
