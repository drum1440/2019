import xml.etree.cElementTree as ET

context = ET.iterparse('/Users/myalias/Documents/myxml2.xml', events=("start", "end"))

context = iter(context)
tag1b_tag = False
for event, elem in context:
    tag = elem.tag
    value = elem.text
    if value :
        value = value.encode('utf-8').strip()

    if event == 'start' :
        if tag == "tag1":
            print ("tag1 %s" % value)
        if tag == "tag2":
            print ("tag2 %s" % value)
        if tag == "tag1b" :
            tag1b_tag = True

        elif tag == 'tag3' :
            if tag1b_tag :
                print ("tag3 follows tag1b %s" % value)
            else :
                print ("tag3 does not follow tag1b %s " % value)

        elif tag == 'tag1' :
            if tag1b_tag :
                print ("tag1 follows tag1b %s" % value)
            else :
                print ("tag1 does not follow tag1b %s " % value)

    if event == 'end' and tag =='tag1b' :
        tag1b_tag = False
    elem.clear()

#<root>
# <tag1> id="mytag1id"
#  <tag1b> id="tag1b my id"
#   <tag2>
#    <tag3>tag3wow</tag3>
#   </tag2>
#  </tag1b>
# </tag1>
# <tag1> id="mytag1id2"
#  <tag1b> id="tag1b my id2"
#   <tag2>
#    <tag3>tag3wow2</tag3>
#   </tag2>
#  </tag1b>
# </tag1>
#</root>
