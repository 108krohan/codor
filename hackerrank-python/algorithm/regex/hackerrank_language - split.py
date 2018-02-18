"""hackerrank language by hackerrank.com
"""
import re
testcases = int(raw_input())
string = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:"+\
         "SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:"+\
         "PASCAL:SBCL:DART:GROOVY:OBJECTIVEC"
langs = string.split(":")
for _ in range(testcases) :
    string = raw_input().split()[1]
    if string in langs :
        print 'VALID'
    else :
        print 'INVALID'

##import re
##n = int(raw_input())
##
##pattern = r'\b(CPP|C|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)\b'
##reg = re.compile(pattern)
##while n:
##    x,word = raw_input().split()
##    result = reg.findall(word)
##  
##    if result:
##        print 'VALID'
##    else:
##        print 'INVALID'
##    n = n - 1

"""
Problem Statement

Every submission at HackerRank has a field called language which
indicates the programming language which a hacker used to code his solution.

C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:
ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:
GROOVY:OBJECTIVEC

Sometimes, error-prone API requests can have an invalid language
field. Could you find out if a given submission has a valid language
field or not?

Input Format

First line contains N. N API requests follow, each in
a newline. Each request has an integer api_id and a string language
which are the request parameters placed by the an API request.

Constraints

1 <= N <= 100  
10^4 <= api_id < 10^5  
a valid language is any of the languages listed above (case sensitive):

Output Format

For every api request given in input, print "VALID" if it has
a valid language string in it or print "INVALID" otherwise.

Sample Input

3
11011 LUA
11022 BRAINFUCK
11044 X

Sample Output

VALID
VALID
INVALID

Explanation

LUA and BRAINFUCK are valid languages as listed above. As
X is doesn't appear in the list, it is an invalid request.
"""
