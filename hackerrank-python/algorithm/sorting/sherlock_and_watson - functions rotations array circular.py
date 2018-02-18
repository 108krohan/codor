"""sherlock and watson at hackerrank.com
"""
def new(index) :
    global size_arr, num_rotns
    new_index = index + num_rotns
    if new_index < size_arr :
        return new_index 
    else :
        return new(index - size_arr)

def rotations(rotns) :
    global array, size_arr
    rotns = 0
    new_arr = [0 for i in range(size_arr)]
##    for elem in range(rotns) :
    for index in range(size_arr) :
        new_arr[new(index)] = array[index]
    return new_arr

def print_queries() :
    global queries, array
    for index in queries :
        print array[index]

size_arr, num_rotns, size_queries = map(int, raw_input().strip().split())
array = [int(i) for i in raw_input().strip().split()]
queries = [int(raw_input()) for i in xrange(size_queries)]
array = rotations(num_rotns)
##print array
print_queries()


"""
Problem Statement

John Watson performs an operation called Right Circular Rotation
on an integer array [a0,a1,...an−1]. Right Circular Rotation transforms
the array from [a0,a1,...an−1] to [aN−1,a0,...,aN−2].

He performs the operation K times and tests Sherlock's
ability to identify the element at a particular position
in the array. He asks Q queries. Each query consists of one
integer, idx, for which you have to print the element at
index idx in the rotated array, i.e. aidx.

Input Format 
The first line consists of three integers, N, K, and Q,,
separated by a single space. 
The next line contains N space-separated integers which
indicate the elements of the array A. 
Each of the next Q lines contains one integer
per line denoting idx.

Output Format

For each query, print the value at index idx in the updated array
separated by newline.

Constraints

1≤N≤105
1≤ai ≤105
1≤K≤105
1≤Q≤500
0≤idx≤N−1

Sample input

3 2 3
1 2 3
0
1
2

Sample output

2
3
1

Explanation 

After one rotation array becomes, [3, 1, 2]. 
After another rotation array becomes [2, 3, 1]. 
Final array now is [2, 3, 1]. 
0th element of array is 2. 
1st element of array is 3. 
2nd element of array is 1.
"""
