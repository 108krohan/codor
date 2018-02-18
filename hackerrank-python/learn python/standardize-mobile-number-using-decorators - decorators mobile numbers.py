"""standardize mobile number using decorators at hackerrank.com
"""
"""
Problem Statement

Lets dive into decorators! You are given N mobile numbers.
Sort them in ascending order after which print them in standard format.


+91 xxxxx xxxxx

The given mobile numbers may have +91 or 91 or 0 written
before the actual 10 digit number. Alternatively, there maynot
be any prefix at all. 

Input Format

An integer N followed by N mobile numbers.

Output Format

N mobile numbers printed in different lines in the required format.

Sample Input

3
07895462130
919875641230
9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230

"""
def standardize(strNum) :
    lstNum = list(strNum)
    lstNum = lstNum[-10:]
##    strNum = str(lstNum)
##    print strNum
    result = '+91 '
    for digit in lstNum :
        if len(result) == 9 :
            result += ' '
        result += digit
    return result

numCases = int(raw_input())
record = []
for _ in range(numCases) :
    record.append(standardize((raw_input())))
record.sort()
for i in record :
    print i

"""
def standardize(record) :
    for oneRecord in record :
        result = '+91 '
        for elem in str(oneRecord)[:] :
            if len(result) == 9 :
                result += ' '
            result += elem
        print result

numCases = int(raw_input())
record = []
for _ in range(numCases) :
    record.append(int(raw_input()[-10:]))

record.sort()
standardize(record)
"""
