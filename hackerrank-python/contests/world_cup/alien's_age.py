def getkind(srow, scol) :
    global grid, row, col
    if srow < row - 1 and scol < col - 1 :
        if grid[srow + 1][scol] == '#' :
            if grid[srow][scol + 1] == '#' : 
                return 2
            elif grid[srow+1][scol+1] == '#' :
                return 1
        elif grid[srow + 1][scol + 1] == '#' :
            if grid[srow][scol + 1] == '#' :
                return 3
    else : 
        return 4
    return 4
		
def getage(srow, scol) : 
    global grid, row, col
    age = 1
    ##find type 
    ##execute va type
    ##three types
    kind = getkind(srow, scol) 
    if kind == 4 : 
        return 0
    if kind == 1 : 
        ##|\
        ##| \
        count = 1
        while count + scol <= col and grid[srow][scol:scol + count] == '#'*count :
            srow += 1
            count += 1
        age = count - 1
    elif kind == 2 : 
        ##|---
        ##| /
        count = 0
        srow += 1
        while count + scol < col and grid[srow][scol + count] == '#' : 
            count += 1
        extr = count
        while srow < row and count > 0 and grid[srow][scol:scol + count] == '#'*count :
            srow += 1
            count -= 1
        if count != 0 : 
            return 1
        age = extr - 1
    elif kind == 3 : 
        ##\-|
        ## \|
        count = 1
        extr = 1
        while extr + scol <= col - 1 and grid[srow][scol + extr] == '#' : 	
            extr += 1
        while srow < row and count >= 1 and grid[srow][scol + count:scol + extr] == '#'*count :
            srow += 1
            count += 1
        if count != 0 : 
            return 1
        age = extr - 1
    return age
	
def action() : 
	global grid, row, col
	age = 0
	for onerow in xrange(row) :
		for onecol in xrange(col) :
			if grid[onerow][onecol] == '#' : 
				age = max(age, getage(onerow, onecol))
                
	return age
row, col = map(int, raw_input().split())
grid = [raw_input() for _ in xrange(row)]
result = action()
print result
