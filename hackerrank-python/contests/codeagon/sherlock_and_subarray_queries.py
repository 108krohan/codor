"""sherlock and subarray queries at codeagon at hackerrank.com
"""
##i could have used dictionaries!!! then via try and catch block we could have easily done the problem.......
size, queries = map(int, raw_input().strip().split())
array = [int(i) for i in raw_input().strip().split()]
table = [[0 for i in xrange(size - j)] for j in xrange(size)]
for _ in xrange(queries) :
    start, stop = map(int, raw_input().split())
    start, stop = start - 1, stop - 1
##    data = [0 for i in range(start, stop + 1)]
##    data_index = 0
    try :
        large = array[start]
        table[start][0] = 1
        occurs = 1
        if table[start][stop - start] != 0 :
    ##        print 'from the mothertable'
            print table[start][stop - start]
            continue
        for index in xrange(start + 1, stop + 1) :
            
            if array[index] > large :
                large = array[index]
                occurs = 1
            elif array[index] == large :
                occurs += 1
            else :
                pass
            table[start][index - start] = occurs
        print occurs
    except :
        continue
##for elem in table :
##    print '\t'.join([str(i) for i in elem])

"""
Problem Statement


Watson gives to Sherlock an array A1,A2,…,AN of integers. He also gives him M queries of the form Li,Ri. For each query, Sherlock has to find how many times the largest element of the subarray A[Li,Ri] occurs in A[Li,Ri]. 
A[i,j] denotes the subarray Ai,Ai+1...Aj.

Input Format 
 First line contains N and M. Next line contains N integers denoting the array A. Each of the next M lines contain two space separated integers denoting Li and Ri. 

Output Format 
 For each query print the required answer in one line. 

Constraints 
1≤N,M≤105 
1≤Li≤Ri≤N 
1≤Ai≤105 

Sample Input 
5 3
3 1 3 2 1
1 3
2 5
1 5


Sample Output 
2
1
2


Explanation 
 In subarray S[1,3], the largest element is 3 which occurs 2 times. 
 In subarray S[2,5], the largest element is 3 which occurs 1 times. 
 In subarray S[1,5], the largest element is 3 which occurs 2 times. 

"""
