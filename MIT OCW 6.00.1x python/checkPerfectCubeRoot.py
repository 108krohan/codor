##cube root of a number via brute force
##exhaustive enumeration check if a number is a perfect cube
x = int ( raw_input ('Enter a number \t'))
ans = 0
while ans*ans*ans < abs(x)	:
	ans = ans + 1
if ans * ans * ans != abs(x)	:
	print x, 'is not a perfect cube'
else 	:
	if x < 0	:
		ans = -ans
	print 'Cube root of ' + str(x) + 'is' + str(ans)


"""
ans = 0

number = -27

+ catenation
if x == 0 :

"""
