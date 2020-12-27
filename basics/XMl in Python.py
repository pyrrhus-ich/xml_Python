
https://lxml.de/tutorial.html

1. Installiere lxml
-----------------------------------------------------------------------------------

from lxml import etree

2. Wir verwneden vorerst zwei klassen:
    - Element: repräsentiert ein Element im XML Dokument. Speichert alle Informationen
                über Tag Namen, Attribute und Verweise auf untergeordnete Elemente
    - ElementTree: repräsentiert das gesamte XML Dokument. Es enthält einige allgemeine
                Informationen zum XML Dokument wie Codierung, XML Version, sowie einen 
                Verweis auf das Stammelement des Dokuments

3. Vom Text zum XML
-------------------------------------------------------------------------------------
    - Analysen von xml geht entweder von einem Dokument oder von einer Zeichenfolge

3.1 Zeichenfolge analysieren:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - mit fromstring()
        #Beispiel
        xml_string = "<a><b>hello</b></a>"
        root = etree.fromstring(xml_string)
        print(type(root)) # <class 'lxml.etree._Element'>

3.2 XML aus Datei analysieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - mit parse()
        # Beispiel
        xml_path = 'xml_file.xml'

        tree = etree.parse(xml_path)
        print(type(tree))  # <class 'lxml.etree._ElementTree'>

        root = tree.getroot()
        print(type(root))  # <class 'lxml.etree._Element'>

3.3 Drucken des XML Dokuments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - mit dump()
    - nimmt ein Element und druckt es sauber formatiert aus
        # Beispiel
        xml_string = "<a><b>hello</b></a>"
        root = etree.fromstring(xml_string)
        
        etree.dump(root)
        # <a>
        #   <b>hello</b>
        # </a>  

4. Durchlaufen des XML tree
-------------------------------------------------------------------------------------
 Die Struktur eines XML Dokumentes verhält sich wie eine Sammlung von Listen.
 Mit Ausnahme von Root, ist jede Liste mit einer anderen Liste verschachtelt.
Auf ein untergeordnetes Element kann zugegriffen werden, indem sein Index in eckigen
Klammern angegeben wird.
        # Beispieldokument
        xml_file = "xml_file.xml"
        root = etree.parse(xml_file).getroot()
        etree.dump(root)
        
        # <country>
        #   <name>United Stated of America</name>
        #   <capital>Washington</capital>
        #   <states>
        #     <state>California</state>
        #     <state>Texas</state>
        #     <state>Florida</state>
        #     <state>Hawaii</state>
        #   </states>
        # </country>
    Wenn ich jetzt auf 'capital' zugreifen möchte:
        etree.dump(root[1])  # <capital>Washington</capital>
    Das Stammelement 'country' hat drei Unterelemente ('name', 'capital', 'states')
    name hat Index 0
    capital hat index 1
    states hat Index 2
    Um jetzt alle Unterelemente von 'states' zu durchlaufen müssen wir zuerst das Element abrufen:
        states = root[2] # Hier rufen wir das Element ab
        for state in states:
            print(state.text)# text ist keyword für den Inhalt des Elementes
    # California
    # Texas
    # Florida
    # Hawaii

5. Zugriff auf Attribute:
--------------------------------------------------------------------------------------
    Da die Daten nicht unbedingt als Rohtext gespeichert werden, sondern oft nur als 
    Attribute in einem Tag.
        xml_file = "xml_file1.xml"
        root = etree.parse(xml_file).getroot()
        etree.dump(root)
        
        # <country name="United Stated of America" capital="Washington">
        #   <states>
        #     <state name="Hawaii"/>
        #     <state name="Florida"/>
        #     <state name="Texas"/>
        #     <state name="California"/>
        #   </states>
        # </country>

    Wenn wir auf Unterelement zugreifen wollen, verhält sich das xml wie eine Liste.
    Beim Zugriff auf Attribute verhält sich das xml jedoch wie ein Dictionary. Hier be-
    nötigen wir die get() Methode um auf das angegebene Attribut zuzugreifen. Wenn 
    das Attribut nicht vorhanden ist, wird 'None' zurück gegeben.
    Im Gegensatz zu Dictionary wird das Attribut hierbei nicht in eckigen Klammern angegeben.
        states = root[0]
        for state in states:
            print(state.get('name'))
            
        # Hawaii
        # Florida
        # Texas
        # California

    Mit den Methoden keys() und items() können alle Attribute eines Tags abgerufen werden
        print(root.keys())     # ['name', 'capital']
        print(root.items())    # [('name', 'United Stated of America'), ('capital', 'Washington')] 

6. XML zu Text
-------------------------------------------------------------------------------------------------------
    tostring() nimmt ein Element und gibt ein Byte Objekt zurück, das später in einer Datei 
    gespeichert werden kann
        xml_string = "<a><b>hello</b></a>"
        root = etree.fromstring(xml_string)
        
        print(etree.tostring(root))  # b'<a><b>hello</b></a>'

7. Speichern mit write()
----------------------------------------------------------------------------------------
    Die Methode write() speichert eine Instanz ElementTree direkt in einer Datei
    Wenn wir mit einem lxml Element gearbeitet haben, sollten wir es zuerst konvertieren
    zu ElementTree.

        xml_string = "<a><b>hello</b></a>"
        root = etree.fromstring(xml_string)
        
        tree = etree.ElementTree(root)  # create an instance of ElementTree in order to save it
        tree.write("xml_file.xml")

Zusammenfassung
---------------------------------------------------------------------------------------
- ein element eines xml dokumentes im xml.etree modul wird repräsentiert als eine 
    Instanz der Element klasse 
- Arbeite mit Elements als eine Liste, wenn Du auf die Subelemente zugreifen willst.
- Zugriff auf die Attribute wie in einem Dictionary
- fromstring() und parse() werden benutzt um xml Objekte aus einem String oder einem 
    File zu importieren
- tostring() und write() erlauben es XML Objekte zurückzuspeichern in Dateien.

# Beispiel 1 'How much information'
'''Schreiben Sie ein Programm, das eine Zeichenfolge, die ein XML-Dokument darstellt, 
aus der Eingabe liest und zwei Zahlen ausgibt: die Anzahl der untergeordneten Elemente 
des Wurzelelements und die Anzahl der Attribute, die das Wurzelelement hat. Diese Zahlen 
sollten in einer Zeile gedruckt und durch ein Leerzeichen getrennt werden.'''
from lxml import etree

xml_string = '<a attr="123"><b>hello</b><c/></a>'

root = etree.fromstring(xml_string)
x = len(root)
y = len(root.keys())
print(x,y)
#oder:
doc = etree.fromstring(input())
print(len(doc.getchildren()), len(doc.keys()))

#Beispiel2: 'Print all text'
'''Sie erhalten ein XML-Dokument, das aus einem Wurzelelement und seinen mehreren 
untergeordneten Elementen besteht. Jedes dieser untergeordneten Elemente speichert 
etwas Text darin. Schreiben Sie ein Programm, das über die untergeordneten Elemente 
iteriert und den darin enthaltenen Text ausgibt.'''

    from lxml import etree

    xml_string = '<root><elem1>I am elem1</elem1><elem2>I am elem2</elem2><elem3>I am elem3</elem3></root>'
    root = etree.fromstring(xml_string)
    #root = etree.fromstring(input())
    for el in root:
        print(el.text)

#Beispiel 3: 'Find attribute'
'''Sie erhalten ein XML-Dokument. Ihr Programm sollte einen String, der dieses Dokument repräsentiert, 
aus der Eingabe lesen. Die zweite Zeile der Eingabe enthält einen Attributnamen, den Sie im Wurzelelement 
finden sollten. Wenn die Wurzel dieses Attribut enthält, geben Sie seinen Wert aus. Andernfalls geben Sie 
None aus.'''

    from lxml import etree

    # xml_string = '<root a1="aba" a2="caba"/>'
    # atr_name = 'a1'
    xml_string = input()
    attr = input()
    root = etree.fromstring(xml_string)
    print(root.get(attr))