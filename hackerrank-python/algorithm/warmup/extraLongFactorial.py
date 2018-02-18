# -*- coding: utf-8 -*-
"""extra long factorials at Hackerrank.com

Problem Statement

You are given an integer N. Print the factorial of this number.

N!=N×N−1×N−2×⋯×3×2×1

Note: Factorials of N>20 can't be stored even in a 64−bit long long variable.
Big integers must be used for such calculations.
Languages like Java, Python, Ruby etc. can handle big integers but
we need to write additional code in C/C++ to handle such large values.

We recommend solving this challenge using BigIntegers.

:::Input Format:::

Input consists of a single integer N.

Constraints 
1≤N≤100

:::Output Format:::

Output the factorial of N."""

number = int(raw_input())
for i in range (1, number):
    number *= i
print number
