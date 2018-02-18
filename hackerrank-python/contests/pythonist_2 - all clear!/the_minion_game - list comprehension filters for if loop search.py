"""the minion game at pythonist at hackerrank.com
"""

from collections import defaultdict

##def pfind(prefix, sequences):
##    collector = defaultdict(list)
##    for sequence in sequences:
##        collector[sequence[0]].append(sequence)
##    for item, matching_sequences in collector.items():
##        if len(matching_sequences) >= 2:
##            new_prefix = prefix + item
##            yield (new_prefix, len(matching_sequences))
##            for r in pfind(new_prefix, [sequence[1:] for sequence in matching_sequences]):
##                yield r
##
##def find_repeated_substrings(s):
##    s0 = s + " "
##    return pfind("", [s0[i:] for i in range(len(s))])

vowels = 'AEIOU'
string = raw_input()
p1 = 'Stuart'
p0 = 'Kevin'
lstr = len(string)
count0 = 0
count1 = 0
for index in xrange(lstr) :
    if string[index] not in vowels :  ##player 1
        count1 += lstr - index
    else :
        count0 += lstr - index
##print count0, count1
if count0 == count1 :
    print 'Draw'
elif count0 < count1 :
    print p1, count1
else :
    print p0, count0
    

"""
def p2(string) :
    ##words starting with consonants
    global lstr
    lst = []
    count = 0
    for i in xrange(lstr - 1) :
        if string[i] in vowels :
            for end_i in xrange(i + 1, lstr + 1) :
                if string[i:end_i] not in lst :
                    score = sum([1 for tem_i in xrange(lstr + end_i - i) \
                                  if string[tem_i:tem_i + (end_i - i)] == \
                                  string[i:end_i]])
##                    print string[i:end_i], score
                    count += score
                    lst.append(string[i:end_i])
                else :
                    pass
##    print count
    return count

def p1(string) :
    ##words starting with consonants
    global lstr
    count = 0
    lst = []
    for i in xrange(lstr - 1) :
        if string[i] not in vowels :
            for end_i in xrange(i + 1, lstr + 1) :
                if string[i:end_i] not in lst :
                    score = sum([1 for tem_i in xrange(lstr + end_i - i) \
                                  if string[tem_i:tem_i + (end_i - i)] == \
                                  string[i:end_i]])
##                    print string[i:end_i], score
                    count += score
                    lst.append(string[i:end_i])
                else :
                    pass
##    print count
    return count
"""
"""
for index in xrange(lstr - 1) :
    if string[index] not in vowels :  ##player 1
        for sub_index in xrange(index + 1, lstr + 1) :
##            sub_string = string[index: sub_index]
##            if sub_string not in lst1 :
##                count1 += string.count(sub_string)
####                print sub_string, count1
##                lst1 += (sub_string, )
            count1 += 1
    else :
        for sub_index in xrange(index + 1, lstr + 1) :
##            sub_string = string[index: sub_index]
##            if sub_string not in lst0 :
##                count0 += string.count(sub_string)
####                print sub_string, count0
##                lst0 += (sub_string, )
            count0 += 1

"""
