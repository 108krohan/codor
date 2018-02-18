# -*- coding: utf-8 -*-
"""Largest Permutation at hackerrank.com
"""
"""
Problem Statement

You are given an array of N integers which is a permuation of
the first N natural numbers. You can swap any two elements of the
array. You can make at most K swaps. What is the largest permutation,
in numerical order, you can make?

Input Format 
The first line of the input contains two integers, N and K, the
size of the input array and the maximum swaps you can make,
respectively. The second line of the input contains a permutation
of the first N natural numbers.

Output Format 
Print the lexicographically largest permutation you can make
with at most K swaps.

Constraints 
1≤N≤105 
1≤K≤109

Sample Input#00

5 1
4 2 3 5 1

Sample Output#00

5 2 3 4 1

Explanation#00 
You can swap any two numbers in [4,2,3,5,1] and see the
largest permutation is [5,2,3,4,1]

Sample Input#01

3 1
2 1 3

Sample Output#01

3 1 2

Explanation#01 
With 1 swap we can get [1,2,3], [3,1,2] and [2,3,1] out
of these [3,1,2] is the largest permutation.

Sample Input#02

2 1
2 1

Sample Output#02

2 1

Explanation#02 

We can see that [2,1] is already the largest permutation. So we
don't need any swaps.
"""
import sys
sys.setrecursionlimit(10000)

def swap(nums, swaps, index = 0) :

    if swaps == 0 or nums == [] :
        return nums[:]

    if nums[0] == max(nums) :
        try :
            return [nums[0]] + swap(nums[index+1:], swaps)
        except :
            return [nums[0]] + swap([], swaps)
    i = nums.index(max(nums))
    nums[index], nums[i] = \
                 nums[i] , nums[index]
    return [nums[index]] + swap(nums[index+1:], swaps - 1)
     

size, swaps = [int(x) for x in raw_input().split()]
numbers = [int(x) for x in raw_input().split()]

result = swap(numbers, swaps)

for elem in result :
    print elem,

"""
###a failed attempt that had me fucked. 

size, swaps = [int(x) for x in raw_input().split()]
oneSwap = 1
index = 0
numbers = [int(x) for x in raw_input().split()]
orderedNums = list(enumerate(numbers[:]))
orderedNums.sort(key = lambda x : x[1], reverse = True)
##print orderedNums

repeats = 0
donebar = [x[1] for x in orderedNums[:swaps]]
##print donebar

while oneSwap <= swaps and index < size:

    if numbers[orderedNums[index][0]] == index :
##       oneSwap -= 1
        donebar.insert(swaps, orderedNums[swaps + repeats][1])
        repeats += 1
        index += 1
        continue
    numbers[orderedNums[index][0]] = numbers[index]
    index += 1
    oneSwap += 1

##print oneSwap
donebar.extend(numbers[swaps+repeats:])
for elem in donebar :
    print elem,
"""
