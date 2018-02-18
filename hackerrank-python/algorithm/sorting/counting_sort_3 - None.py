"""counting sort 3 at hackerrank.com
"""
"""
Problem Statement

In the previous challenge, it was easy to print all the integers in order, since you did not have to access the original list. Once you had obtained the frequencies of all the integers, you could simply print each integer in order the correct number of times. However, if there is other data associated with an element, you will have to access the original element itself.

In the final counting sort challenge, you are required to print the data associated with each integer. This means, you will go through the original array to get the data, and then use some "helper arrays" to determine where to place everything in a sorted array.

If you know the frequencies of each element, you know how many times to place it, but which index will you start placing it from? It will be helpful to create a helper array for the "starting values" of each element.

Challenge 
You will be given a list that contains both integers and strings. In this challenge you just care about the integers. For every value i from 0to99, can you output L, the number of elements that are less than or equal to i?

Input Format 
- n, the size of the list ar. 
- n lines follow, each containing an integer x and a string s.

Output Format 
Output L for all numbers from 0 to 99 (inclusive).

Constraints 
1≤n≤1000000 
0≤x<100,x∈ar 
length of string ≤10
Sample Input

10
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the
Sample Output

1 3 5 6 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 
Explanation 
0 appears 1 time, so the 0th number is 1. 
0 and 1 combined appear 3 times, so the next number is 3. 
This continues for the rest of the list, until no more new numbers appear.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def counting_sort() : 
    global array, result 
    result = [0 for i in range(100)]
    for elem in array : 
        result[elem] += 1
##    print " ".join(str(i) for i in result)

def counting_sort_2() :
    global array, result, starting_pos
    starting_pos = [0 for i in range(100 + 1)]
    count = 0
    for index in range(len(result)) : 
        starting_pos[index] = count
        while result[index] is not 0 : 
##            print index, 
            count += 1
            result[index] -= 1
    index += 1
    while index <= 100 : 
        starting_pos[index] = count
        index += 1
def counting_sort_3() :
    global array, result, starting_pos
    for elem in range(100) :
        print starting_pos[elem + 1],
result = []    
starting_pos = []
size = int(raw_input())
array = [int(raw_input().strip().split()[0]) for i in range(size)]
counting_sort()
counting_sort_2()
counting_sort_3()

