"""fraction equality at number voyage at hackerrank.com
"""

p = 10010101
q = 11111117
add = p + q
print add
result = 0
for a in range(1, add) :
    b = a - add
    if b != 0 :

        result = result + a + b
print result

#answer = 0
"""
Professor Math has a fraction PQ, where P and Q are prime numbers. For two integers A and B, 0<A<(P+Q),B≠0, he observes that the fractions P−AQ+B and P+BQ−A are equal, when written in reduced form.

For P = 10010101 and Q = 11111117, professor Math finds all the distinct pairs (A, B) that satisfy the observation. Find the value of ∑for all pairs(Ai+Bi), here Ai is the value of A in the ith pair and Bi is the value of B in the ith pair. 

Note that:
•Fraction PQ is said to be in reduced form, if gcd(|P|, |Q|) = 1
•Pairs (A1,B1) and (A2,B2) are considered to be equal, iff A1=A2 and B1=B2

"""
