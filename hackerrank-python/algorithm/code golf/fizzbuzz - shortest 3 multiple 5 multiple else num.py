"""fizzbuzz at hackerrank.com
"""

for i in range(1,101):
    if i%15==0:
        print 'FizzBuzz'
    elif i%3==0:
        print 'Fizz'
    elif i%5==0:
        print 'Buzz'
    else:
        print i

#i=1;exec"print'FizzBuzz'[i%-3&4:12&8-i%5]or i;i+=1;"*100

"""
Problem Statement

Write a short program that prints (to STDOUT) the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

The goal is to write the shortest code possible.

Scoring: Your score is (200 - number of characters in your source code)/10

Expected output:

1 
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
............and so on
"""
