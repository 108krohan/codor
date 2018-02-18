"""the time in words at hackerrank.com
"""
"""
"""

def num2word(number) :

    data_conv = ['','one', 'two', 'three', 'four', 'five', 'six', \
                 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', \
                 'thirteen', 'fourteen', 'fifteen', 'sixteen', \
                 'seventeen', 'eighteen', 'nineteen', 'twenty', \
                 'twenty-one', 'twenty-two', 'twenty-three', \
                 'twenty-four', 'twenty-five', 'twenty-six', \
                 'twenty-seven', 'twenty-eight', 'twenty-nine', ]
    return data_conv[number]

hours = int(raw_input())
minutes = int(raw_input())

##print  hours
##print minutes
##import num2word

if minutes == 0 :
    print num2word(hours) + " o' clock"
if minutes == 15 :
    print "quarter past " + num2word(hours)
elif minutes == 30 :
    print "half past " + num2word(hours)
elif minutes == 45 :
    print "quarter to " + num2word(hours + 1)
elif minutes > 30 :
    if minutes == 59 :
        print num2word(60 - minutes).replace('-',' ') + \
          " minute to " + num2word(hours + 1)
    else :
        print num2word(60 - minutes).replace('-',' ') + \
          " minutes to " + num2word(hours + 1)
elif minutes == 1 :
    print num2word(minutes).replace('-',' ') + \
      " minute past " + num2word(hours)
else :
    print num2word(minutes).replace('-',' ') + \
      " minutes past " + num2word(hours)

"""
def number(Number):
    if 1 <= Number < 19:
        return num2words1[Number]
    elif 20 <= Number <= 99:
        tens, below_ten = divmod(Number, 10)
        return num2words2[tens - 2] + '-' + num2words1[below_ten]
    else:
        print("Number out of range")
"""
