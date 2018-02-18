##This program gets the sum of big numbers 32 bit type


N = int(raw_input())
x = raw_input().split()
a = ()
sum = 0
for i in range (0,N) :
    sum += int(x[i])
print sum
