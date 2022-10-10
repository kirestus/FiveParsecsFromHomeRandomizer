import xml.etree.ElementTree as ET
from xml.dom import minidom
dat = minidom.parse('background.xml')

racename = dat.getElementsByTagName('raceName')
roll = dat.getElementsByTagName('roll')
reactions = dat.getElementsByTagName('reactions')
descriptions = dat.getElementsByTagName('description')

for x in racename:
    print (x.firstChild.data)

for x in reactions:
    print (x.firstChild.data)

for x in descriptions:
    print (x.firstChild.data)