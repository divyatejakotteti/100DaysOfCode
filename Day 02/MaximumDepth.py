import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if len(elem)>0:
        maxdepth+=1
        level+=1
    for child in elem:
        depth(child,level)
