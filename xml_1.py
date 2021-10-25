import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    total = 0
    
    if root.attrib:
        total += 1
    
    for child in node:
        total += len(child.attrib)
        for c in child:
            total += len(c.attrib)
    
    return total

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
