from lxml import etree as et 


#tree = et.parse(xml_path)


class Beispielklasse:
    def __init__(self):
        print("Hier spricht der Konstruktor")

class PaRes:
    def __init__(self, XmlSource, root):
        self.srcPfad = "./src/" + XmlSource
        self.root = root
        #print("Source Pfad ist {}".format(self.srcPfad))
    def pfad(self, query):
        self.query = query
        tree = et.parse(self.srcPfad)
        res = tree.xpath(self.root + self.query)
        print(res)
        print(self.root + self.query)
    def text(self, query):
        self.query = query
        tree = et.parse(self.srcPfad)
        res = tree.xpath(self.root + self.query + "/text()")
        print("\n {}/text()".format(self.root + self.query))
        print("\n {}\n".format(res))


Beispielklasse()

#ExtItem->card->group->characteristic [code=1100001279] ->value->desc

#src = PaRes("product-input-xml-2.xml", "/ExtItem/")
#src.pfad("card/group/characteristic[code=1100001279]/value/desc/text()")
src = PaRes("product-input-xml-2.xml", "/ExtItem/header")
#src.pfad("/description/text()")
#src.text("/EAN/EANCode")
#src.text("/itemSupplierCode")
#src.text("/signLabelDescription")
#src.text("/EAN/supplierCode")
#src.text("/createDate")
#src.text("/itemSupplierCode")
src.text("/productHierarchy/productGroup/mainProductGroup/department/domain/desc")



