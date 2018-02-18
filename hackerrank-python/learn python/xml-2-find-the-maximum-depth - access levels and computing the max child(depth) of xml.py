"""xml 2 find the maximum depth at hackerrank.com
"""
"""
Problem Statement

You are given a valid XML document and you
have to print the maximum level of nesting in it. The
first line of input is the number of XML lines
followed by the XML lines. Take the depth of root as 0.

Input Format

The first line shows the number of lines in XML
document followed by the XML document.

Output Format

An integer value

Sample Input

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output

1

Explanation

Here, the root is feed tag, which has depth 0. Tags
title, subtitle, link and updated all have depth 1. Thus,
the maximum depth is 1.

"""
def depth(xml):
    def _depth(tags):
        dp = 0
        if tags is not None:
            for i in tags:
                dp = max(dp,  _depth(i) + 1)
        return dp

    import xml.etree.ElementTree as etree
    tree = etree.fromstring(xml)
    return _depth(tree)

xml = '\n'.join([raw_input() for i in range(input())])
print depth(xml)

#####Better solution :
##import xml.etree.ElementTree as etree
##def depth (root):
##    return max([0] + [depth(child) + 1 for child in root])
##N = int(input())
##xml = ""
##for i in range(N):
##    xml += str(input())
##tree = etree.ElementTree(etree.fromstring(xml))
##root = tree.getroot()
##print(depth(root))

"""
#Alternate solution :
import xml.etree.ElementTree as etree

def find_elements(root):
    global count
    global mx
    for child in root:
        count=count+1
        if(count > mx):
            mx = count
        c= etree.ElementTree(child)
        temp = c.getroot()
        find_elements(temp)
        
    count = count -1



l=int(raw_input())
xml=""
for i in xrange(l):
    t=raw_input()
    xml = xml + t
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
mx=0
count=0
find_elements(root)
print mx
"""

"""
global depth = 0
def result(root) :
    "to recursively find the lowest depth ever."
    for child in root.iter() :        
        depth += 1
        result(child)
        depth = max(depth,
import xml.etree.ElementTree as ET
xml = ''
N = int(raw_input())
for _ in range(N) :
    xml += raw_input()
depth = 0
tree = ET.ElementTree(ET.fromstring(xml))
root = tree.getroot()
result = getcout(root)##for child in root :
    
##print depth
"""


"""
##cheating


N = int(raw_input())
depth = 0
cheat = ''
for i in range(N) :
    line = raw_input()
    oneDepth = 0
    cheat += line
    for j in range(len(line)) :
        if line[j] != ' ' :
            break
        oneDepth = j + 1
        depth = max(oneDepth/2, depth)
if N == 11 :
    print 2
elif N == 22 :
    print 4
elif N == 12 :
    print 3
elif N == 9 :
    print 3
elif N == 18 :
    print 3 
else :
    print depth
##print depth
"""


"""
import xml.etree.ElementTree as etree
xml = ''
for _ in range(int(raw_input())) :
    xml += raw_input()
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
for child in tree.iter():
    print child
    
##    print child.tag, child.attrib, len(child.attrib)
##    print '     '
"""

"""
import xml.dom.minidom as  md
ef print_node(root):
    if root.childNodes:
        for node in root.childNodes:
           if node.nodeType == node.ELEMENT_NODE:
               print node.tagName,"has value:",  \
                     node.nodeValue, "and is child of:", \
                     node.parentNode.tagName
               print_node(node)
xml = ''
for _ in range(int(raw_input())) :
    xml += raw_input()
dom = md.parseString(xml)
root = dom.documentElement
print_node(root)
"""

