"""make it anagram at hackerrank.com"""

w1=raw_input()
w2=raw_input()

total=0
conv = {True : 0, False : 1}
for letter in "abcdefghijklmnopqrstuvwxyz":
    total+= abs(w1.count(letter) - w2.count(letter))
print total

"""
https://www.hackerrank.com/contests/magic-lines-september-2015/challenges/make-it-anagram-mglines
"""
