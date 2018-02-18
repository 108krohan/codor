x = 26
epsilon = 0.01
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x :
	ans += 0.00001
	numGuesses += 1
print 'numGuesses = ', numGuesses
if abs(ans**2 - x) >= epsilon	:
	print 'Failed on sqroot of ', x
else	:
	print ans, 'is close to sqroot of', x
	
"""
x = 25

variable up up up
"""
