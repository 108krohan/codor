N = int(raw_input())
for i in range(N+1) :
    for j in range(N-i) :
        print " ",
    for j in range(i) :
        print "#",
    print ""
###Only possible on python 3.4 sofar from my research!
###The major flaw in it, is an extra space after every keyout.
