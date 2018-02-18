"""count_fridays_the_13th at hackerrank.com"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import date, timedelta
import time
monthdays = { 1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, \
               8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
testcases = int(raw_input())
for _ in range(testcases) : 
    do, mo, yo, dt, mt, yt = map(int, raw_input().split())
    numfr = 0
    date1 = date(yo, mo, do)

    while date1.day != 13 :
        date1 += timedelta(days = 1)
    
    date2 = date(yt, mt, dt) + timedelta(days = 1)
    month = date1.month
    
    while date1 < date2 :
        if date1.weekday() == 4 :
            numfr += 1
##            print date1, date1.weekday()
        if month == 13 :
            month = 1
        if date1.year % 4 == 0 and month == 2 :
            date1 += timedelta(1)
        date1 += timedelta(days = monthdays[month])    
        month += 1
    print numfr

###correct code below, with a lot of junk comments, informative comments
"""
from datetime import date, timedelta
import time

##from datetime import timedelta, date

monthdays = { 1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, \
               8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

##def daterange(start_date, end_date):
##    for n in range(0, int ((end_date - start_date).days)):
##        yield start_date + timedelta(n)

testcases = int(raw_input())
for _ in range(testcases) : 
    do, mo, yo, dt, mt, yt = map(int, raw_input().split())

##    days = days_between(do, mo, yo, dt, mt, yt)
    numfr = 0
    date1 = date(yo, mo, do)

    while date1.day != 13 :
        date1 += timedelta(days = 1)

    date2 = date(yt, mt, dt) + timedelta(days = 1)

##    for single_date in daterange(date1, date2):
##        print single_date.strftime("%Y-%m-%d")
##        numfr += 1
    month = date1.month
    while date1 < date2 :
##        print date1.weekday()        
        if date1.weekday() == 4 :
            numfr += 1
##            print date1, date1.weekday()

        if month == 13 :
            month = 1
        if date1.year % 4 == 0 and month == 2 :
            date1 += timedelta(1)
        date1 += timedelta(days = monthdays[month])    
        month += 1

    print numfr
"""


##    while (date1.day != 13) :
##        date1.day += 1
##    while (date1 < date2) :
##        if date1.weekday() == 5 :
##            numfr += 1
##        date1.month += 1
##    print numfr
##monthdates = { 1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, \
##               8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
##def conv(mt, mo) :
##    global monthdates
##    curr_m = mo
##    days = 0
##    while curr_m != mt :
##        if curr_m > 12 :
##            cur_m = 1
##        days += monthdates[curr_m]
##    return days
##
##def days_between(do, mo, yo, dt, mt, yt) :
##    in_days = (yt - yo)*365 + dt - do
##    for year in range(yo, yt + 1) :
##        if year % 4 == 0 :
##            in_days += 1
####    mt -= 1
####    if mt > mo :
####        in_days += conv(mt, mo)
####    elif mt == mo - 1 :
####        in_days += 
##    in_days += conv(mt, mo)
##    print in_days
##    return in_days
##
