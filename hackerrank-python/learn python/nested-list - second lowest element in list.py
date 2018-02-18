"""nesting and sorting lists at hackerrank.com

sorting lists based on a particular sub index in a nested list!
"""

second = []
record = []
numCases = int(raw_input())
for i in range(numCases) :
    oneRecord = []
    oneRecord.append(raw_input())
    oneRecord.append(float(raw_input()))
    record.append(oneRecord)

record.sort(key = lambda pair : pair[1])

lowest = record[0][1]
print lowest
print record
for elem in record :
    if elem[1] != lowest :
        secondLow = elem[1]
        for ele in record[:] :
            if ele[1] == secondLow :
                second.append(ele)
                record.remove(ele)
                print 'second', second
                print 'record', record
        break
second.sort(key = lambda pair : pair[0])
print '\n'.join(x[0] for x in second)
