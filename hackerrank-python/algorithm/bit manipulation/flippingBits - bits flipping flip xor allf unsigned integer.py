# -*- coding: utf-8 -*-
"""Flipping bits at hackerrank.com
"""
"""
Problem Statement

You will be given a list of 32 bits unsigned integers. You are
required to output the list of the unsigned integers you get
by flipping bits in its binary representation (i.e. unset
bits must be set, and set bits must be unset).

Input Format

The first line of the input contains the list size T,
which is followed by T lines, each line having an integer from the
list.

Constraints

1≤T≤100 
0≤integer<232

Output Format

Output one line per element from the list with the requested result.
"""

m = 0xFFFFFF00
allf = 0xFFFFFFFF
##m ^ allf does XOR, so it all is like unsignedd

testcases = int(raw_input())
record = []
for _ in range(testcases) :
    record.append(int(raw_input()))
record = map(lambda x : x ^ allf, record)
for elem in record :
    print elem
             
