##Implementing functions to check if two numbers are within
##A specified difference range
def fn(x,y,epsilon)	:
	return abs(x-y) < epsilon
x = float (raw_input("Enter x : "))
y = float (raw_input("Enter y : "))
epsilon = float (raw_input("Enter the epsilon value : "))
if fn(x,y,epsilon)	:
	print "Yes! The input data is lying within epsilon"
else	:
	print "Goddamn it. No luck. It flew out of the epsilon."
