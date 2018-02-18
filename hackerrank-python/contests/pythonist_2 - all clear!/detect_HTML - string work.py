"""detect HTML tags at pythonist 2 at hackerrank.com
"""

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for attr in attrs:
            print '-> ' + attr[0] + ' > ' + attr[1]
num_lines = int(raw_input())
parser = MyHTMLParser()
string = ''
for i in xrange(num_lines) :
    string += raw_input()
parser.feed(string)

####the most below is a parser function from html parser. A more complete
####version of the same.

##
##string = ''
##num_lines = int(raw_input())
##for i in xrange(num_lines) :
##    string += raw_input()
##lstr = len(string)
##tag = 0
##at = 0
##lst = []
##attribute = {}
##index = 0
##try : 
##    while index < lstr :
##        while string[index] == ' ' :
##            index += 1
##        if string[index] == '<' :
##            if string[index + 1] == '/' :
##                index += 1
##                while string[index] != '<' :
##                    index += 1
##            elif string[index + 1] == '!' : ##getting over comments
##                index += 1
##                arr_o = 1
##                arr_c = 0
##                while arr_o != arr_c :
##                    index += 1
##                    if string[index] == '<' :
##                        arr_o += 1
##                    if string[index] == '>' :
##                        arr_c += 1
##                index += 1                
##            else :
##                name = ''
##                index += 1
##                while string[index] not in ('>', ' ') : ##name
##                    name += string[index]
##                    index += 1
##                lst.append(name)
##                tag += 1
##                if string[index] == '>' : ##check if ended
##                    index += 1
##                    continue
##                else :
##                    attribute[tag] = []
##                    while string[index] != '>' :
##                        attr = ''
##                        attr_val = ''
##                        index += 1
##                        if string[index] in ('/', '>') :
##                            index += 1
##                            break
##                        while string[index] == ' ' :
##                            index += 1
##                        while string[index] not in ('=',' ') : 
##                            attr += string[index]
##                            index += 1
##                        while string[index] != '"' :
##                            index += 1
##                        index += 1
##                        while string[index] != '"' :
##                            attr_val += string[index]
##                            index += 1
##                        index += 1
##                        
####                        print attr, attr_val
##                        attribute[tag].append((attr, attr_val))
##        else :
##            index += 1
##            continue
##except Exception, e:
##    pass
##print lst
##for one_tag in range(tag) :
##    print lst[one_tag]
##    try :
##        attr_lst = attribute[one_tag + 1] 
##        for elem in attr_lst :
##            print '-> ' + elem[0] + ' > ' + elem[1]
##    except :
##        continue
"""
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr
    def handle_endtag(self, tag):
        print "End tag  :", tag
    def handle_data(self, data):
        print "Data     :", data
    def handle_comment(self, data):
        print "Comment  :", data
        pass ##added
    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c
    def handle_decl(self, data):
        print "Decl     :", data
"""
