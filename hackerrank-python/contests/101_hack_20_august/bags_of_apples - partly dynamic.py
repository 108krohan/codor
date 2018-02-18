"""bags of apples101hack28 at hackerrank.com
"""
a=input()
b=map(int,raw_input().split())
b.sort()
c=sum(b)
if c%3==0:
 print c
else:
    d=b+[sum(i) for i in [(b[x],b[y]) for x in range(len(b)) for y in range(x+1,len(b))]]
    d.sort()
    for i in d:
        if (c-i)%3==0:
                print c-i
                exit()



"""bullshit warned"""
##bags = int(raw_input())
##apples = [int(i) for i in raw_input().split()]
##apples.sort(reverse = True)
##one = [i for i in apples if i % 3 == 1]
##two = [i for i in apples if i % 3 == 2]
##zero = [i for i in apples if i % 3 == 0]
##val = sum(zero)
##one_len = len(one)
##two_len = len(two)
##if two_len % 3 == 0 :
##    val += sum(two)
####val += sum(two
####for index in range(min(one_len, two_len)) :
####    val += one[index] + two[index]
######for rest_index in range(index
####print val
##if one_len == two_len :
##    val += sum(one) + sum(two)
##elif one_len < two_len :
##    last_is_two = False
##    last_is_one = False
##    for index in range(one_len - 2) :
##
##        big_val = max(two[index] + one[index], sum(one[index:index + 3]), \
##                   sum(two[index:index + 3]))        
##
##        if index == one_len - 3 :
##
##            if sum(one[index:index + 3]) == big_val :
##                last_is_one = True
##                val += big_val
##                break
##            if sum(two[index:index + 3]) == big_val :
##                last_is_two = True
##                val += big_val
##                val += sum(two[index + 3: two_len - two_len%3])
##                break
##            else :
##                for i in range(index, one_len) :
##                    val += two[i] + one[i]
##                mod = two_len % 3
##                end = two_len - mod
##                val += sum(two[i:end])
##                break
##
##        val += big_val
##elif one_len > two_len :
##    last_is_two = False
##    last_is_one = False
##    for index in range(two_len - 2) :
##
##        big_val = max(two[index] + one[index], sum(one[index:index + 3]), \
##                   sum(two[index:index + 3]))        
##
##        if index == two_len - 3 :
##            if sum(two[index:index + 3]) == big_val :
##                last_is_two = True
##                val += big_val
##                break
##            if sum(one[index:index + 3]) == big_val :
##                last_is_one = True
##                val += big_val
##                val += sum(one[index + 3: one_len - one_len%3])
##                break
##            else :
##                for i in range(index, two_len) :
##                    val += two[i] + one[i]
##                mod = one_len % 3
##                end = one_len - mod
##                val += sum(one[i:end])
##                break
##
##        val += big_val
##       
##print val

"""
Problem Statement

Mika is very rich guy. He has n bags of apples! Each bag contains positive integer number of apples, bag with number i contains ai apples. Mika decided that the time has come to sell some of his bags. When selling some bag, Mika is automatically selling each apple inside the bag, but he can't take apple out of bag and sell it. To make this more interesting, Mika added yet another extra condition (he likes extra conditions)! He wants the total number of sold apples be divisible by 3.

So Mika is wondering, what is the maximum number of apples that can be sold? Help him calculate that number!

Input Format

The first line contains integer n (1≤n≤1000), number of Mika's bags of apples.

The second line contains n numbers a1,a2,…,an (1≤ai≤1000) where ai is the number of apples in i-th bag (1≤i≤n).

Output Format

In a single line, print the largest total number of apples which can be sold.

Sample Input 1

4
2 2 1 2
Sample Output 1

6
Sample Input 2

5
3 6 9 9 3
Sample Output 2

30
Explanation

In the first sample, the best options is to sell three bags, each containing 2 apples. In total, Mika will sell 2+2+2=6 apples.

In the second sample every bag has number of apples divisible by 3. So, total sum of apples is divisible by 3 and Mika can sell all his bags.
"""
##total number of sold apples be divisible by 3
##apples.sort()
##largest_num = 0
##found = False
##val = sum(apples)
##if val % 3 == 0 :
##    print val
##    found = True
##else :
##    
##    for index in range(bags) :
##        bag = apples[index]
##        val -= bag
##        if val % 3 == 0 :
##            print val
##            found = True
##            break
##        val += 3
##
##if not found :
####    for index in range(bags) :
####        
