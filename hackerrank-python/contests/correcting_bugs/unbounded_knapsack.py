# -*- coding: utf-8 -*-
"""unbounded knapsack at hackerrank.com
"""

# Knapsack problem
import sys

sys.setrecursionlimit(10000)
##file_name = sys.argv[1]

items = []
##print 'Reading input...'
##with open(file_name, 'r') as reader:
##  first_line = True
##  for line in reader:
##    if first_line:
##      first_line = False
##      knapsack_size, num_of_items = [int(x) for x in line.strip().split()]
##      continue
##    value, weight = [int(x) for x in line.strip().split()]
##    items.append((value, weight))

##assert num_of_items == len(items)
##print 'Read %d items.' % len(items)

optimals = [{} for x in range(num_of_items)]  # [right_most_item][weight_limit] = optimal_value

def get_optimal_value(right_most_item, weight_limit):
  global optimals
  for elem in optimals :
      print elem

  # edge case 1
  if right_most_item < 0:
      return 0

  # edge case 2
  val, weight = items[right_most_item]
  if weight > weight_limit:
      return get_optimal_value(right_most_item - 1, weight_limit)

  # check cached case
  if weight_limit in optimals[right_most_item]:
      return optimals[right_most_item][weight_limit]

  # regular case
  val_with_this = get_optimal_value(right_most_item - 1, weight_limit)
  val_without_this = get_optimal_value(right_most_item - 1, weight_limit - weight) + val
  optimal_val =  max(val_with_this, val_without_this)
  optimals[right_most_item][weight_limit] = optimal_val
  return optimal_val

##print 'Calculating optimal value...'
optimal_val = get_optimal_value(num_of_items - 1, knapsack_size)
##print 'Optimal value:', optimal_val

"""


Problem Statement

Given a list of n integers, A={a1,a2,…,an}, and another integer, k representing the expected sum. Select zero or more numbers from A such that the sum of these numbers is as near as possible, but not exceeding, to the expected sum (k).

Note

    Each element of A can be selected multiple times.
    If no element is selected then the sum is 0.

Input Format

The first line contains T the number of test cases.
Each test case comprises of two lines. First line contains two integers, n k, representing the length of list A and expected sum, respectively. Second line consists of n space separated integers, a1,a2,…,an, representing the elements of list A.

Constraints
1≤T≤10
1≤n≤2000
1≤k≤2000
1≤ai≤2000,where i∈[1,n]

Output Format

Output T lines, the maximum sum for each test case which is as near as possible, but not exceeding, to the expected sum (k).

Sample Input

2
3 12
1 6 9
5 9
3 4 4 4 8

Sample Output

12
9

Explanation

In the first test case, one can pick {6, 6}. In the second, we can pick {3,3,3}.

"""
