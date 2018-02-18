"""

Task 

Read two integers from STDIN and print three lines where: 
(1) the first line contains the sum of the two numbers, 
(2) the second line contains the difference of the two numbers
(first - second), 
(3) the third line contains the product of the two numbers.

Input Format 

The first line contains the first integer, a, and the
second line contains the second integer, b.

Constraints 

1≤a≤1010 
1≤b≤1010

Output Format 

Print three lines as explained above.

Sample Input

3
2
Sample Output

5
1
6

"""
m1 = int(raw_input())
m2 = int(raw_input())
print m1 + m2
print m1 - m2
print m1*m2
