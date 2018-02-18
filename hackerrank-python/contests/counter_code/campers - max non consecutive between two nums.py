"""campers at hackerrank.com
"""

##def max_in_range(start, stop) :
##    new_start = start + 2
##    new_stop = stop - 2
####    print 'new_start', new_start
####    print 'new_stop', new_stop
##    global players
##    if new_stop - new_start <= 2 : 
####        if start == stop :
####            return 1
##        if new_stop - new_start < 0 :
##            return 0
##        if new_start == new_stop :
##            return 1
##        if new_start in (1, players, players - 1) :
##            return 1
##        if new_stop in (1, players, players - 1) :
##            return 1
##        if new_stop - new_start == 1 :
##            return 0
####        if new_stop - new_start == 3 :
####            return 2
##        if new_stop - new_start  == 2 :
##            return 2            
##    else :
##        return 2 + max_in_range(new_start, new_stop)
##

def max_in_range(start, stop) :
##    global players
    count = 0
    new_start = start + 2
    while stop - new_start > 1 :
        count += 1
        new_start += 2
    return count
players, num_members = map(int, raw_input().split())
members = [ int(i) for i in raw_input().split() ]
members.sort()
max_players = num_members
start = -1
for one_member in members : 
    max_players += max_in_range(start, one_member)
    start = one_member
max_players += max_in_range(members[-1], players + 2)
print max_players



"""
Problem Statement

Time is running out. You have a final match to play as a counter terrorist. You have N players each having a distinct ID from 1 to N. You have to choose some players on your team from these N players such that no two chosen players have consecutive numbers (as they tend to kill each other). Also you definitely have to choose some K players whose numbers are given. They are the snipers. Find the maximum number of players that you can choose.

Input Format

The first line contains 2 space-separated integers, N and K, where N is the total number of players and K is the number of players that have to be definitely in the team (the snipers). 
The second line contains K space-separated integers that are the IDs of the snipers.

NOTE: There are no two snipers with consecutive numbers.

Constraints 
2≤N≤2×106 
1≤K≤N/2 
1≤ ID of each sniper ≤N
Output Format

You need to print the maximum number of players that you can have in your team.

Sample Input

8 2
6 2
Sample Output

4
Explanation

There are 8 players in total, among which you have to definitely choose players with ID 2 and 6. 
To maximize the number of players in the team, you will choose the players with IDs 4 and 8, so that you will have a total of 4 players.
"""
