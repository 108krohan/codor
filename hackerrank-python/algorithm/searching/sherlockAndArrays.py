# -*- coding: utf-8 -*-
"""sherlock and array at hackerrank.com
"""
"""
Problem Statement
Watson gives Sherlock an array A of length N.
Then he asks him to determine if there exists an
element in the array such that the sum of the elements
on its left is equal to the sum of the elements on its right. If
there are no elements to the left/right, then the
sum is considered to be zero. 
Formally, find an i, such that, A1+A2...Ai-1 =Ai+1+Ai+2...AN.

Input Format 
The first line contains T, the number of test cases. For each
test case, the first line contains N, the number of elements
in the array A. The second line for each
test case contains N space-separated integers, denoting the array A.

Output Format 
For each test case print YES if there exists an element in
the array, such that the sum of the elements
on its left is equal to the sum of the elements
on its right; otherwise print NO.

Constraints 

1≤T≤10 
1≤N≤105 
1≤Ai ≤2×104 
1≤i≤N

Sample Input

2
3
1 2 3
4
1 2 3 3

Sample Output

NO
YES

Explanation 
For the first test case, no such index exists. 
For the second test case, A[1]+A[2]=A[4], therefore index 3
satisfies the given conditions.
"""

testcases = int(raw_input())

for case in range(testcases) :
    num = int(raw_input())
    array = map(int, raw_input().split())
    flag = 1
    left = [0]
    right = [0]
        
    for index in range(1, num - 1) :
##        left = sum(elem for elem in array[:i])
##        right = sum(elem for elem in array[i+1:])
        left.append(left[-1] + array[index-1])
        right.append(right[-1] + array[-index])
    print left
    print right
    if num == 1 :
        print 'YES'
    elif num == 2 :
        print 'NO'
    else :            
        for index in range(1, num - 1) :
            if left[index] == right[num - 1 - index] :
                print 'YES'
                flag = 0
                break
        if flag is not 0 :
            print 'NO'
                
