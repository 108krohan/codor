"""Solve me second on hackerrank.com

This program takes input on the same line"""
##
##def solveMeSecond(a,b):
##   return a+b
##n = int(raw_input())    #faster than n = input() , since input()
##                        #executes the line as python command
##for i in range(0,n):
##    a, b = raw_input().split()
##    a,b = int(a),int(b)
##    res = solveMeSecond(a,b)
##    print res
##
##"""Alternate method to do the same"""
##"""
##n = int(raw_input()) 
##for _ in range(n):
##    a,b = map(int,raw_input().split())
##    res = solveMeSecond(a,b)
##    print res
##"""

class solveMeSecond(object) :
   #solveMeSecond is a set of variable that are to be computed

   def __init__(self) :
      self.a,self.b = map(int, raw_input().split())
      
   def __add__(self) :
      print 'chud gayi'
      return self.a + self.b

def fn(numCases = int(raw_input())) :
   record = []
   for i in range(numCases) :
      print record
      ele = solveMeSecond()
      record.append(ele)
   ##for i in range(numCases) :
   ##   print 
   for ele in record :
      print ele
    
fn()
