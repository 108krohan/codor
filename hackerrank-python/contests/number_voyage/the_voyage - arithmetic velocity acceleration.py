"""the voyage at number voyage at hackerrank.com
"""
#wrong answer

distance = 10**20
##print distance
##subs = distance/3 +.33
ldist = distance - (distance)*1/3.0
subs = ldist/2
print ldist
print 'subs =', subs
accln = 150
v1_3 = (2*accln*subs)**.5
print v1_3,
##v2_3 = v1_3
##print v2_3,
v3_3 = (2*(-accln)*subs + v1_3**2)**.5
print v3_3
t1_3 = v1_3/accln
print t1_3,
##t1_3 = (2*subs/accln)**0.5
##print t1_3,
##t2_3 = distance/v2_3
##print t2_3,
t2_3 = 1000000000.0
t3_3 = (v1_3 - v3_3)/accln
print t3_3
print 't3_3 == t1_3 ?', t3_3 == t1_3
time = t1_3 + t2_3 + t3_3
print 'time taken =',time
av_velo = distance/time
print av_velo
##print av_velo*av_velo
try_velo = v1_3*2/3 
"""
Problem Statement


Professor Math decided to go for a long distance. He will be
driving 1020 Kms. For the first one-third distance he distances
with acceleration of 150 Km/Hr2. For the next one-third
distance he distances with constant velocity. For the rest of
the journey he distances with deceleration of 150 Km/Hr2.
Find the average velocity of professor's long distance. Print the
integer value only (no unit).
"""
