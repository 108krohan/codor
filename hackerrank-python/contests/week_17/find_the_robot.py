"""find the robot at hackerrank.com"""

def action(one_turn) :
    global x, y
    goes_in = one_turn % 4
    if goes_in == 0 : ##going to the down
        y -= one_turn
    elif goes_in == 1 : ##going to the right
        x += one_turn
    elif goes_in == 2 : ##going to the up
        y += one_turn
    elif goes_in == 3 : ##going to the left
        x -= one_turn
    return x, y
x, y = 0, 0
testcases = int(raw_input())
data = [(0, 0)]
##print data
curr_max = 0
for _ in range(testcases) :
    turn = int(raw_input())
    try :
        print ' '.join([str(i) for i in data[turn]])
    except :
        for one_turn in range(curr_max + 1, turn + 1) :
            data.append(action(one_turn))
        curr_max = turn
        print ' '.join([str(i) for i in data[turn]])
