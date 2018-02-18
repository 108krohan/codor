"""ice cream parlor at hackerrank.com
"""
"""
Sample Input

2
4
5
1 4 5 3 2
4
4
2 2 4 3

Sample Output

1 4
1 2

Explanation

The sample input has two test cases. 
For the 1st, the amount M = 4 and there are 5 flavors
at the store. The flavors indexed at 1 and 4 sum up to 4. 
For the 2nd test case, the amount M = 4 and the flavors
indexed at 1 and 2 sum up to 4.

"""
cases = int(raw_input())

for _ in range(cases) :
    dollars = int(raw_input())
    size = int(raw_input())
    flavors = map(int, raw_input().split())
    for index in range(len(flavors)) :
        complete = 0 
        for subindex in range(index + 1, len(flavors)) :
            if flavors[index] + flavors[subindex] == dollars :
                print index + 1, subindex + 1
                complete = 1
                break
        if complete == 1 :
            break
