# -*- coding: utf-8 -*-

"""
Problem Statement

You're given an array containing integer values.
You need to print the fraction of count of positive numbers,
negative numbers and zeroes to the total numbers.
Print the value of the fractions correct to 3 decimal places.

:::Input Format:::

First line contains N, which is the size of the array. 
Next line contains N integers A1,A2,A3,⋯,An, separated by space.

Constraints 
1≤N≤100 
−100≤Ai≤100

:::Output Format:::

Output three values on different lines equal to the fraction of
count of positive numbers, negative numbers and zeroes to the
total numbers respectively correct to 3 decimal places.
"""
positive = negative = zero = 0
N = int(raw_input())
x = raw_input().split()
for i in range(N) :
   if int(x[i]) is 0 :
       zero += 1
   elif int(x[i]) > 0 :
       positive += 1
   else :
       negative += 1
print "{:.3f}".format(float(positive)/float(N))
print "{:.3f}".format(float(negative)/float(N))
print "{:.3f}".format(float(zero)/float(N))
