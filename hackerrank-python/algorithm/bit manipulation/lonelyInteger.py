# -*- coding: utf-8 -*-
"""lonely integere at hackerrank.com
"""
"""
Problem Statement

There are N integers in an array A. All but one integer occur in pairs. Your task is to find the number that occurs only once.

Input Format

The first line of the input contains an integer N, indicating the number of integers. The next line contains N space-separated integers that form the array A.

Constraints

1≤N<100 
N % 2=1 (N is an odd number) 
0≤A[i]≤100,∀i∈[1,N]
Output Format

Output S, the number that occurs only once.

Sample Input:1

1
1
Sample Output:1

1
"""


def lonelyinteger(a):
    answer = 0
    for elem in a[:] :
        count = a.count(elem)
        if count == 1 :
            answer = elem
            break
    return answer

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
