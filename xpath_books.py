from lxml import etree as et 


xml_path = "./src/books.xml"
tree = et.parse(xml_path)
"""
for title in tree.xpath("/bookstore/book/title"):
    #print(title.text)

# Die beiden folgenden Schleifen machen das selbe nur mit anderer Syntax
len = 0
for author in tree.xpath("/bookstore/book/author"):
    len += 1
    #print("Nr {} ist {}".format(len, author.text))

len = 0
for author in tree.xpath("//author"):
    len += 1
    #print("Nr {} ist {}".format(len, author.text))
"""
book = tree.xpath("//book[@category='web']")

