"""validate list of email addresses with filter at hackerrank.com
"""
"""
"""
#import string
def conditions (oneRecord) :
##    lst = list(oneRecord)
##    #print lst
##    atRate = lst.index('@')
##    dot = lst.index('.')
    atRate = oneRecord.find('@')
    dot = oneRecord.find('.')
##    print dot
    if dot == -1 or atRate == -1 :
        return False
    username = oneRecord[:atRate]
    websitename = oneRecord[atRate+1:dot]
    extension = oneRecord[dot+1:]
##    print username, websitename,extension
    
    if not websitename.isalnum() or len(extension)>3 :
##        print oneRecord, 'False by first if'
        return False
    username = username.translate(None, '-._')
    if not username.isalnum() :
##        print username, 'False by second if'
        return False
    return True

numCases = int(raw_input())
result = []
for _ in range(numCases) :
    oneRecord = raw_input()
    if conditions(oneRecord) :
        result.append(oneRecord)
##    result.append(oneRecord)
result.sort()
print result    
