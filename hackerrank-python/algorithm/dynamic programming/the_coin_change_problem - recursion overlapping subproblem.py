"""the coin change problem at hackerrank.com
"""

def dyna_coin(c) :
    print 'd ' + adam
    index = 0
    for elem in c :
        print str(coins[index]) + ' ' + ' '.join([str(i) for i in elem])
        index += 1
    print ''

cash, num_coins  = map(int, raw_input().split())
coins = [int(i) for i in raw_input().split()]
coins.sort()
#to get the number of ways of getting a sum of n
c = [[0 for i in range(cash)] for j in range(num_coins)] #getting the first row mapped

for index in range(1, cash + 1) :
    if index % coins[0] == 0 :
        c[0][index - 1] = (1)
    else :
        c[0][index - 1] = (0)
adam = ' '.join([str(i) for i in range(1, cash + 1)])
print adam
print ' '.join([str(i) for i in c[0]])
print ''

for coin_index in range(1, num_coins) :
    for index in range(min(coins[coin_index], cash)) :
        c[coin_index][index] = (c[coin_index - 1][index])
    try :
        c[coin_index][coins[coin_index] - 1] += 1
    except :
        pass
    dyna_coin(c)

    for index in range(coins[coin_index], cash) : 
        val = c[coin_index - 1][index] + \
              c[coin_index][index - coins[coin_index]]
        c[coin_index][index] += (val)
        dyna_coin(c)

print c[num_coins - 1][cash - 1]







##This is utterly bullshit, below code

##global one_soln
##one_soln = 0
##
##def coin_change(final, size, array) :
##    global one_soln
##    if final < array[-1] :
##        return
##    for index in range(size) :
##        print array[index]
##        if final < array[index] :
##            continue
##        if final % array[index] == 0  :
##            one_soln += 1
##        coin_change(final % array[index], size - index - 1, \
##                        array[index + 1:])
####        print '\t'
##    return one_soln
##
##final, size = [int(i) for i in raw_input().split()]
##array = [int(i) for i in raw_input().split()]
##array.sort(reverse = True)
##soln = coin_change(final, size, array)
##print soln

"""
Problem Statement

How many different ways can you make change for an amount, given a list of coins? In this problem, your code will need to efficiently compute the answer.

Task

Write a program that, given

An amount N and types of infinite available coins M
A list of M coins - C={C1,C2,C3,..,CM}
Prints out how many different ways you can make change from the coins to STDOUT.

The problem can be formally stated:

Given a value N, if we want to make change for N cents, and we have infinite supply of each of C={C1,C2,…,CM} valued coins, how many ways can we make the change? The order of coins doesn’t matter.

Constraints

1≤Ci≤50
1≤N≤250
1≤M≤50
The list of coins will contain distinct integers.
Solving the overlapping subproblems using dynamic programming

You can solve this problem recursively, but not all the tests will passs unless you optimise your solution to eliminate the overlapping subproblems using a dynamic programming solution

Or more specifically;

If you can think of a way to store the checked solutions, then this store can be used to avoid checking the same solution again and again.
Input Format

First line will contain 2 integer N and M respectively. 
Second line contain M integer that represent list of distinct coins that are available in infinite amount.

Output Format

One integer which is the number of ways in which we can get a sum of N from the given infinite supply of M types of coins.

Sample Input

4 3
1 2 3 
Sample Output

4
Sample Input #02

10 4
2 5 3 6
Sample Output #02

5
Explanation

Example 1: For N=4 and C={1,2,3} there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}

Example 2: For N=10 and C={2,5,3,6} there are five solutions: {2,2,2,2,2},{2,2,3,3},{2,2,6},{2,3,5},{5,5}.

Hints

Think about the degenerate cases:

How many ways can you give change for 0 cents?
How many ways can you give change for >0 cents, if you have no coins?
If you are having trouble defining your solutions store, then think about it in terms of the base case (n=0)
For help on reading from STDIN, see the HackerRank environment help page under the "Sample Problem Statement" section.
"""
"""
More outputs :
2 27
44 5 9 39 6 25 3 28 16 19 4 49 40 22 2 12 45 33 23 42 34 15 46 26 13 31 8 

1
"""
