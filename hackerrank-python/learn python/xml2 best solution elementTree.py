# Enter your code here. Read input from STDIN. Print output to STDOUT
import xml.etree.ElementTree as etree;
def maxdepth(node):
    ans=0;
    if(len(node)==0): return ans;
    for child in node:
        ans=max(ans,maxdepth(child));
    return ans+1;

xml="";
for i in range(input()):
    xml=xml+raw_input();

tree = etree.ElementTree(etree.fromstring(xml));
print maxdepth(tree.getroot());
