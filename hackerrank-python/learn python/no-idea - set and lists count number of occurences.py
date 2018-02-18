# -*- coding: utf-8 -*-
"""

Problem Statement

There is an array of n integers, and 2 disjoint sets of m integers each A and B. You like all integers in A and dislike all integers in B. Your initial happiness is 0 and for each integer in the array, i, if i∈A, you add 1 to your happiness, if i∈B, you add −1 to your happiness, else your happiness does not change. Output your final happiness at the end.

Note that since A and B are sets, they have no repeated elements. But, the array might contain duplicate elements.

Constraints 
1≤n≤105 
1≤m≤105 
1≤Any integer in the input≤109

Input Format

First line contains n and m. 
Second line contains n integers, the array. 
Third and fourth lines contain m integers, A and B respectively.

Output Format

Output a single integer, the answer.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain 1 unit of happiness for each 3 and 1 and loose 1 unit for 5 and 7 hence total happiness is 2−1=1.
"""

arraylen, checkerlen = map(int, raw_input().split())
array = map(int, raw_input().split())
happy = map(int, raw_input().split())
sad = map(int, raw_input().split())
happy, sad = set(happy), set(sad)
happiness = 0 
####print happy
####print sad
####type(sad)
##happiness = 0
####for i in range(arraylen) :
####    for check in range(checkerlen) :
####for i in range(arraylen) :
####    for check in range(checkerlen) :
##for j in happy :
##    happiness += array.count(j)
##for j in sad :
##    happiness -= array.count(j)
##print happiness
"""the above code timeout almost everything!
So be careful when using functions!
"""
"""the below code :
Test Case #0:   0s
Test Case #1:   0s
Test Case #2:   0.01s
Test Case #3:   0.09s
Test Case #4:   0.15s
Test Case #5:   0.1s
Test Case #6:   0.12s
Test Case #7:   0.01s
"""
for i in range(arraylen) :
    if array[i] in happy :
        happiness += 1
    elif array[i] in sad :
        happiness -= 1
    else :
        continue
print happiness
