from lxml import etree as et 


xml_path = "./src/product-input-xml-2.xml"
tree = et.parse(xml_path)

#header
def pfad(tagName):
    head = "/ExtItem/header/" + tagName + "/text()"
    print(head)
    res = tree.xpath(head)
    print(res)


pfad("workflowStatus/id")

#ExtItem->card->group->characteristic [code=1100001279] ->value->desc

def card(tagName):
    head = "/ExtItem/card/" + tagName + "/text()"
    print(head)
    res = tree.xpath(head)
    print(res)

card("group/characteristic[code='1100001279']/value/desc")


