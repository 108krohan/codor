"""divisors of a number"""
x = int(raw_input("Enter a number to get it's divisors\t:\t"))
divisors = ()
for i in range(1 , x+1) :
    if x % i == 0 :
        divisors = divisors + (i,)
print divisors
