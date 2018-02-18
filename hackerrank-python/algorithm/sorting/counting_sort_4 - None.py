﻿"""counting sort 4 at hackerrank.com
"""

def counting_sort() :
    ##occurences of an integer
    global array, occurs 
    occurs = [0 for i in range(100)]
    for elem in array : 
        occurs[elem] += 1
##    print " ".join(str(i) for i in occurs)

def counting_sort_2() :
    ##sorted indices' list
    ##later, transformed into starting_pos vals of each elem index
    global array, occurs, starting_pos
    starting_pos = [0 for i in range(100 + 1)]
    count = 0
    for index in range(len(occurs)) : 
        starting_pos[index] = count
        while occurs[index] is not 0 : 
##            print index, 
            count += 1
            occurs[index] -= 1
    index += 1
    while index <= 100 : 
        starting_pos[index] = count
        index += 1

def counting_sort_3() :
    ##number of vals lower than the given val
    global array, occurs, starting_pos
    for elem in range(100) :
        print starting_pos[elem + 1],

def counting_sort_4() :
    ##sorts data into the required format using counnting sort.
    
    global data, size
    result = [[] for i in range(size)]
    for index in range(size/2) :
        data[index][1] = '-'
    for elem in data :
        result[int(elem[0])].append(elem[1])

    for elem in result :
        for sub_elem in elem :
            print sub_elem,
    return
    
occurs = []    
starting_pos = []
size = int(raw_input())
data = [raw_input().strip().split() for i in range(size)]
array = [int(i[0]) for i in data]
strings = ['-' for i in data[:size/2]]
strings.extend([i[1] for i in data[size/2:]])
##counting_sort()
##counting_sort_2()
##counting_sort_3()
counting_sort_4()

"""

size = int(raw_input())
data = [raw_input().strip().split() for i in range(size)]


for index in range(size/2) :
    data[index][1] = '-'
data.sort(key = lambda x : x[0])
for elem in data :
    print elem[1], 

           

"""
"""
Problem Statement

In this challenge you need to print the data that accompanies each integer in a list. In addition, if two strings have the same integers, you need to print the strings in their original order. Hence, your sorting algorithm should be stable, i.e. the original order should be maintained for equal elements.

Insertion Sort and the simple version of Quicksort were stable, but the faster in-place version of Quicksort was not (since it scrambled around elements while sorting).

In cases where you care about the original order, it is important to use a stable sorting algorithm. In this challenge, you will use counting sort to sort a list while keeping the order of the strings (with the accompanying integer) preserved.

Challenge 
In the previous challenge, you created a "helper array" that contains information about the starting position of each element in a sorted array. Can you use this array to help you create a sorted array of the original list?

Hint: You can go through the original array to access the strings. You can then use your helper array to help determine where to place those strings in the sorted array. Be careful about being one off.

Details and a Twist 
You will be given a list that contains both integers and strings. Can you print the strings in order of their accompanying integers? If the integers for two strings are equal, ensure that they are print in the order they appeared in the original list.

The Twist - Your clients just called with an update. They don't want you to print the first half of the original array. Instead, they want you to print a dash for any element from the first half. So you can modify your counting sort algorithm to sort the second half of the array only.

Input Format 
- n, the size of the list ar. 
- n lines follow, each containing an integer x and a string s.

Output Format 
Print the strings in their correct order.

Constraints 
1≤n≤1000000 
n is even 
1≤ length(s) ≤10 
0≤x<100,x∈ar 
The characters in every string in lowercase.

Sample Input

20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
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

- - - - - to be or not to be - that is the question - - - -
Explanation 
Below is the list in the correct order. The strings of each number were printed above for the second half of the array. Elements from the first half of the original array were replaced with dashes.

0 ab
0 ef
0 ab
0 ef
0 ij
0 to
1 be
1 or
2 not
2 to
3 be
4 ij
4 that
4 is
4 the
5 question
6 cd
6 gh
6 cd
6 gh
"""
