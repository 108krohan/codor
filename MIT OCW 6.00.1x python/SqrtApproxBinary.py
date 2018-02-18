##Sqrt of a number by binary search
epsilon = 0.01
low = 0.0
x = int (raw_input("Enter a value for x	:	"))
high = max(x, 1.0)
numG = 0
ans = ( high + low )/ 2.0
while abs(ans**2 - x) >= epsilon and ans <= x	:
	numG += 1
	if ans**2 < x	:
		low = ans
	else	:
		high = ans 
	ans = (low + high)/2.0
print 'Number of guesses :	', numG
print 'Square root approximation of the number', ans
