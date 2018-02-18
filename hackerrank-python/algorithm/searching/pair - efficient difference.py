"""pairs at hackerrank.com
"""
def pairs(lst, k) :
    answer = 0
    global _a_size
    neg_k = -k
    lst.sort()
    print lst
    return sum([1 for i in range(_a_size - 2) if lst[i + 1] - lst[i] == k])


a = map(int, raw_input().strip().split(" "))
_a_size=a[0]
_k=a[1]
b = [int(i) for i in raw_input().split()]
print pairs(b,_k)


"""
def pairs(a,k, s):
    #a contains array of numbers and k is the value of difference
    answer = 0
    a.sort()
    for index in range(s - 1): 
        for next_index in range(index + 1, s) : 
            if a[next_index] - a[index] < k :
                pass
            elif a[next_index] - a[index] == k :
                answer += 1
            else :
                break
                
    return answer

a = map(int, raw_input().strip().split(" "))
_a_size=a[0]
_k=a[1]
b = [int(i) for i in raw_input().split()]
print pairs(b,_k, _a_size)
"""

"""
Problem Statement

Given N integers, count the number of pairs of integers whose difference is K.

Input Format

The first line contains N and K. 
The second line contains N numbers of the set. All the N numbers are unique.

Output Format

An integer that tells the number of pairs of integers whose difference is K.

Constraints: 
N≤105 
0<K<109 
Each integer will be greater than 0 and at least K smaller than 231−1.

Sample Input

5 2  
1 5 3 4 2  
Sample Output

3
Explanation

There are 3 pairs of integers in the set with a difference of 2.
"""
