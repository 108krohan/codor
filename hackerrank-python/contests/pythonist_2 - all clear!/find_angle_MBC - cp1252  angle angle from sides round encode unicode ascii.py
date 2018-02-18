"""find angle MBC at pythonist at hackerrank.com
"""


from __future__ import division
##print 2/4
import math
ab = int(raw_input())
bc = int(raw_input())
mc = (ab**2 + bc**2)**.5 / 2
semi_perimeter = (ab + bc + mc*2) / 2
m_x = bc/2
m_y = ab/2
##math.degrees(math.acos(nume/denom))
mb = (m_x**2 + m_y**2)**.5
cos_val = (mb**2 + bc**2 - mc**2) / (2 * mb * bc)
val = str(int(round(math.degrees(math.acos(cos_val)))))
print val + u'°'.encode('cp1252', 'ignore')

##this also works
##print str(int(round(math.degrees(math.asin(per/hypo))))) + u'°'
##val = unicode(val).encode('ascii', 'ignore') + '°'.encode('ascii', 'ignore')

