# -*- coding: utf-8 -*-
"""Library Fine challenge on Hackerrank.com

Problem Statement

The Head Librarian at a library wants you to make a program
that calculates the fine for returning the book after the
return date. You are given the actual and the expected return dates.
Calculate the fine as follows:

If the book is returned on or before the expected return date,
no fine will be charged.
If the book is returned in the same month as the expected return date,
Fine = 15 Hackos × Number of late days
If the book is not returned in the same month but in the same year as
the expected return date, Fine = 500 Hackos × Number of late months
If the book is not returned in the same year,
the fine is fixed at 10000 Hackos.

:::Input Format:::

You are given the actual and the expected return dates in D M Y format
respectively. There are two lines of input. The first line contains the
D M Y values for the actual return date and the next line contains the
D M Y values for the expected return date.

Constraints 
1≤D≤31 
1≤M≤12 
1≤Y≤3000

:::Output Format:::

Output a single value equal to the fine.

Sample Input

9 6 2015
6 6 2015

Sample Output

45

"""
acday,acmonth,acyear = map(int, raw_input().split())
exday,exmonth,exyear = map(int, raw_input().split())
#print acday, acmonth, acyear
#print exday, exmonth, exyear
if acyear < exyear :
    print 0
elif acyear == exyear :
    #print "here"
    if acmonth < exmonth :
        print 0
    elif acmonth is exmonth :
        if acday <= exday :
            print 0
        else :
            print 15*(acday - exday)
    else :
        print 500*(acmonth - exmonth)
else :
    print 10000
