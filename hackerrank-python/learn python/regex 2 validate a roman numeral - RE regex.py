"""regex 2 validate a roman number at hackerrank.com
"""
"""
Roman numerals only exist between one and 3999"""
import re
expr = raw_input()
meta = re.compile('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
if meta.match(expr) :
    print True
else :
    print False
