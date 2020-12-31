from lxml import etree as et

# nur zum testen ob settings funktioniert
#print(wdir)

xml_path = "./src/books.xml"
tree = et.parse(xml_path)
root = tree.getroot()


#print(root)
#print(root[0])
#print(root[0][0])

""" for el in root:
    print(el.tag +' '+ el.text)
    for i in el:
        print(i.tag + ' ' + i.text)

# Zugriff auf Attribute die bekannt sind
for el in root:
    print(el.get('category'))
    if el.get('cover') is not None:
        print(el.get('cover')) """

""" # druckt die Attribute für den ersten Knoten
for el in root:
    di = el
    key = di.keys()
    val = di.values()
    item = di.items()
    print("Der Key ist {} und der value ist {}".format(key,val))
    print(item)
     """
# Diese Funktion liest für alle Attribute die Keys aus ud speichert diese als List
def readAttributesFromNodes(rootNode):   
    bookAttr = [] #definiert die Liste von Attributen
    nodes = []
    for firstNode in rootNode: # erster Knoten <book>
        fn = firstNode
        if fn.tag not in nodes: nodes.append(fn.tag)
        key = fn.keys() # hier werden alle keys der Attribute abgelegt | Jedes Attribute ist ein Dict {key: value}
        for keys in key: # Jetzt wird über die keys iteriert | weil man ja nicht weiss wieviele es im Node gibt
            if keys not in bookAttr: # hiermit wird sicher gestellt das in der Liste bookAttr keine Duplikate vorhanden sind
                bookAttr.append(keys)
            for secondNode in firstNode:
                sn = secondNode
                key = sn.keys()
                for keys in key:
                    if keys not in bookAttr:
                        bookAttr.append(keys)
    print(bookAttr)

readAttributesFromNodes(root)
