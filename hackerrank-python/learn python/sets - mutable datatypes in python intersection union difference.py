"""sets in python at hackerrank.com

Concept

If the inputs are given in one line separated by a space character, use split() to get the splitted values in form of a list. EG:

a = raw_input()
5 4 3 2
lis = a.split()
print (lis)
['5', '4', '3', '2'] 


If the values in a list are all of integer type, use the map() to convert all the strings to integers. 


newlis = list(map(int, lis))
print (newlis)
[5, 4, 3, 2] 


Sets are unordered bag of unique values. A single set contains values of any immutable data type. 

CREATING SET 


set = {1, 2} # Directly assigning values to a set
set = set() # Initializing a set
set = set(['a', 'b']) # Creating a set from a list
set
{'a', 'b'}



MODIFYING SET - add() and update() 


set.add('c')
set
{'a', 'c', 'b'}
set.add('a') # As 'a' already exists in the set, nothing happens
set.add((5, 4))
set
{'a', 'c', 'b', (5, 4)} 


set.update([1, 2, 3, 4]) # update() only works for iterable objects
set
{'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
set.update({1, 7, 8})
set
{'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
set.update({1, 6}, [5, 13])
set
{'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3} 


REMOVING ITEMS - discard() and remove() 

Both discard() and remove() take a single value as an argument and removes that value from the set. If that value is not present in the set, discard() does nothing but remove() raises a KeyError exception 


set.discard(10)
set
{'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
set.remove(13)
set
{'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3} 


COMMON SET OPERATIONS - union(), intersection() and difference() 


a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
a.union(b) # Values which exist in a or b
{2, 4, 5, 9, 11, 12}
a.intersection(b) # Values which exist in a and b
{2, 4}
a.difference(b) # Values which exist in a but not in b
{9, 5} 


union() and intersection() are symmetric methods i.e. to say, 


a.union(b) == b.union(a)
True
a.intersection(b) == b.intersection(a)
True
a.difference(b) == b.difference(a)
False

These other built-in data structures in Python are also useful.

http://www.thelearningpoint.net/computer-science/lea
rning-python-programming-and-data-structures/lea
rning-python-programming-and-data-structures--tutoria
l-4--built-in-data-structures-strings-lists-tuples-di
ctionaries-mutability
"""
numCase1 = int(raw_input())
case1 = map(int, raw_input().split())
case1.sort()
##print case1
numCase2 = int(raw_input())
case2 = map(int, raw_input().split())
case2.sort()
##print case2
result = []
set1 = set(case1)
print set1
set2 = set(case2)
print set2
##resultSet = (set1.union(set2)).difference(set1.intersection(set2))
resultSet = set1.difference(set2)
resultSet.update(set2.difference(set1))
result = list(resultSet)
result.sort()
for i in result :
    print i 

##set1 = set(case1)
##set2 = set(case2)
##print set1
##print set2
##print 'differs a - b', set1.difference(set2)
