"""poisonous plants at hackerrank.com
"""

def test(pcide) :
    global num_plants
    for index in range(1, num_plants) :
        if pcide[index] > pcide[index - 1] :
            return True, index
    return False, None


def big_case() :
    global pcide, num_plants
    stop, start_index = test(pcide)
    while stop

num_plants = int(raw_input())
pcide = [int(i) for i in raw_input().split()]
day = 0
if num_plants <= 1 :
    pass
elif num_plants >= 500 :
    losers = ()
    big_case()
else :
    stop, start_index = test(pcide)
    while stop: 
        day += 1
        new_cide = tuple(pcide[:start_index])
        old = num_plants
        num_plants = start_index
        for index in range(start_index + 1, old) :
            elem = pcide[index]
            if elem > pcide[index - 1] :
                continue
            new_cide += (elem,)
            num_plants += 1
        pcide = new_cide
        print pcide, num_plants
        stop, start_index = test(pcide)
    
print day


"""
def test(pcide) :
    global num_plants
    for index in range(1, num_plants) :
        if pcide[index] > pcide[index - 1] :
            return True, index
    return False, None


def big_case() :
    global pcide, num_plants
    stop, start_index = test(pcide)
##    while stop

num_plants = int(raw_input())
pcide = [int(i) for i in raw_input().split()]
day = 0
if num_plants <= 1 :
    pass
elif num_plants >= 500 :
    losers = ()
    big_case()
else :
    stop, start_index = test(pcide)
    while stop: 
        day += 1
        new_cide = tuple(pcide[:start_index])
        old = num_plants
        num_plants = start_index
        for index in range(start_index + 1, old) :
            elem = pcide[index]
            if elem > pcide[index - 1] :
                continue
            new_cide += (elem,)
            num_plants += 1
        pcide = new_cide
        print pcide, num_plants
        stop, start_index = test(pcide)
    
print day
"""
"""
Problem Statement

There are N plants in a garden. Each of these plants has been added with some amount of pesticide. After each day, if any plant has more pesticide than the plant at its left, being weaker than the left one, it dies. You are given the initial values of the pesticide in each plant. Print the number of days after which no plant dies, i.e. the time after which there are no plants with more pesticide content than the plant to their left.

Input Format

The input consists of an integer N. The next line consists of N integers describing the array P where P[i] denotes the amount of pesticide in plant i.

Constraints 
1≤N≤100000 
0≤P[i]≤109
Output Format

Output a single value equal to the number of days after which no plants die.

Sample Input

7
6 5 8 4 7 10 9
Sample Output

2
Explanation

Initially all plants are alive. 
Plants = {(6,1), (5,2), (8,3), (4,4), (7,5), (10,6), (9,7)} 
Plants[k] = (i,j) => jth plant has pesticide amount = i. 
After the 1st day, 4 plants remain as plants 3, 5, and 6 die. 
Plants = {(6,1), (5,2), (4,4), (9,7)} 
After the 2nd day, 3 plants survive as plant 7 dies. Plants = {(6,1), (5,2), (4,4)} 
After the 3rd day, 3 plants survive and no more plants die. 
Plants = {(6,1), (5,2), (4,4)} 
After the 2nd day the plants stop dying
"""
