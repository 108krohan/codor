"""another knapsack at codeagon at hackerrank.com
"""
#one coin of each denomination

coin, hackos = map(int, raw_input().split())
##coins = [0 for i in range(N)]
##table = [[] for i in range(N)]
count = 0
impossible = 0
while True :
    if hackos != 0 and coin == 0 :
        impossible = 1
        break
    hackos -= coin
    count += 1
    if hackos >= coin :
        coin -= 1
    else :
        count += 1
        break

if impossible == 1 :
    print -1
else :
    print count


"""

Problem Statement


You are given N coins with values from 1 to N. You have exactly one coin of each denomination. You need to pay M hackos to the shopkeeper. Find the minimum number of coins using which you can pay the shopkeeper.


Input Format


Input consists of 2 space seperated integers N (the number of coins) and M (the hackos that you need to pay to the shopkeeper).

Constraints 

1≤N,M≤10000


Output Format


Output a single value equal to the minimum number of coins required to pay the entire hackos to the shopkeeper.
 If it is impossible to pay the shopkeeper with the hackos you have,then print -1.


Sample Input

2 3



Sample Output

2



Explanation


You can pay the shopkeeper using coins with values 1 and 2 .

"""
