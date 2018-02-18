"""maximize it at pythonist 2 at hackerrank.com
"""

def framer(lst, i = 0, so_far = ()) :
    global modnum, big, N
##    print i, so_far, big
    if i == N - 1:
        for elem in lst[N - 1] :
##            print 'sum so_far', sum(so_far + (elem,))% modnum
            big = max(big, sum(so_far + (elem, )) % modnum)
    else :         
        for elem in lst[i] :
            framer(lst, i + 1, so_far + (elem, ))
        

N, modnum = map(int, raw_input().split())
lst = [map(lambda x: int(x) ** 2, raw_input().split())[1:] for i in range(N)]
big = 0
##for elem in lst :
##    print ' '.join([str(i) for i in elem])
if N == 1 :
    stubig = 0
    for elem in lst[0] :
        stubig = max(stubig, elem % modnum)
    print stubig
else : 
    framer(lst)
    print big
