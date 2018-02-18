# -*- coding: utf-8 -*-
"""Encryption at hackerrank.com

List Manipulation, Exception Handling, math functions, etc.

Problem Statement

An English text needs to be encrypted using the following encryption scheme. 
First, the spaces are removed from the text. Let L be the length of this text. 
Then, characters are written into a grid, whose rows and columns have the
following constraints:

⌊L−−√⌋≤rows≤column≤⌈L−−√⌉, where ⌊x⌋ is floor function and ⌈x⌉ is ceil function
For example, the sentence if man was meant to stay on the ground god would have
given us roots after removing spaces is 54 characters long,
so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots

Ensure that rows×columns≥L

If multiple grids satisfy the above conditions,
choose the one with the minimum area, i.e. rows×columns.
The encoded message is obtained by displaying the characters in a column,
inserting a space, and then displaying the next column and
inserting a space,
and so on. For example, the encoded message for the above rectangle is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message in English with no spaces between the words.
The maximum message length can be 81 characters. Print the encoded message.
"""
import math
string = raw_input()
L = len(string)
floorL = int(math.floor(L**.5))
ceilL = int(math.ceil(L**.5))
#print floorL, ceilL, L
rows = 0
columns = 0
area = 999999999
for row in range(floorL, ceilL+1) :
    for column in range (row, ceilL+1) :
        if row * column < area and row * column >= L:
            area = row * column
            rows, columns = row, column
#print rows, columns
matrix = []
for i in range(rows) :
    #tempstr = ''
    #for j in range(column) :
    tempstr = string[columns*i:columns*(i+1)]
    #print tempstr
    matrix.append(tempstr)
#print matrix
#for row in range(len(matrix)) :
for col in range(columns):
    tempstr = ''
    row = 0
    chr = matrix[row][col] 
    while chr is not '' or chr is not ' ' and row < len(matrix):
        tempstr += chr
        row += 1
        try :
            chr = matrix[row][col]
        except IndexError :
            break
    print tempstr,
