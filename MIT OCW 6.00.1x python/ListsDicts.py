"""Testing lists as mutable objects
Also testing dicts and their behaviour"""
Techs = ['MIT','CalTech']
Ivys = ['Harvard', 'Yellow', 'Brown']
Univs = []
Univs.append(Techs)
print 'Univs = ', Univs

Univs.append(Ivys)
flat = Ivys + Techs
print 'flat = ', flat
for e in Univs :
    print 'e = ', e

artSchools = [ 'RISD', 'Harvard' ]
for u2 in artSchools :
    if u2 in flat :
        flat.remove(u2)
print 'flat = ', flat


flat.sort()
print "flat = ", flat

flat[1] = 'Umass'
print 'flat = ', flat



##L1 = [2]
##L2 = [ L1, L1 ]
##print 'L2 = ', L2
##L1[0] = 3
##print 'L2 = ', L2
##L2[0] = 'a'
##print 'L2 =', L2
##
##L1 = [2]
##print 'L2 = ', L2
##L2 = L1
##L2[0] = 'a'
##print 'L1 = ', L1
##print 'L2 = ', L2
##
##L1 = [2]
##L2 = L1[:]
##L2[0] = 'a'
##print 'L1 = ', L1

##EtoF = { 'uno' : 'dupion', 'wine' : 'duven' \
##         , 'eats' : 'magic' }
##print EtoF
##print EtoF.keys()
##print EtoF.keys
##print EtoF['uno']
##


##D = { 1 : 'one', 'deux' : 'two', 'pi' : 3.14159 }
##D1 = D
##print D1
##D[1] = 'uno'
##print D1
##for k in D1.keys() :
##    print k, ' = ', D1[k]
##

