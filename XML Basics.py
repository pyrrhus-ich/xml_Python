
# 1. Zeile nennt man 'Prolog'
<?xml version="1.0" encoding="UTF-8"?>
# Tag 'book'
<book>
  # Tag 'title'
  <title>The Three-Body Problem</title>
  <author>Liu Cixin</author>
</book>

Element:
    ist die Kombination aus Start und Endtag
    gemeinsam mit dem Inhalt
        # Element 'title'
        <title>The Three-Body Problem</title>

Prolog:
    # 1. Zeile nennt man 'Prolog'
    <?xml version="1.0" encoding="UTF-8"?>
    Der Prolog ist optional aber wenn vorhanden, muss er an erster Stelle stehen
    Beachte: Der Prolog hat kein schließendes Tag

Root:    
    Jedes XML Dokument hat ein 'root' Element

    <?xml version="1.0" encoding="UTF-8"?>
    # Root Element 'library'
    <library>
    # untergeordnetes Element von library
    <book>
        # untergeordnete Elemente von 'book'
        <title>The Three-Body Problem</title>
        <author>Liu Cixin</author>
    </book>
    <book>
        <title>Modern Operating Systems</title>
        <author>Andrew S. Tanenbaum</author>
    </book>
    </library>

Attribute:
    XML Elemente können Attribute besitzen. Hier hat das Element 'picture' das 
    Attribute 'name'
    <picture name="The Black Square"/>
    Ein Element kann mehrere Attribute enthalten:
    <picture name='Sunset at Sea' author='Ivan Aivazovsky'/>

Ersetzen von untergeordneten Elementen durch Attribute
    <?xml version="1.0" encoding="UTF-8"?>
    <gallery>
        <picture name='Sunset at Sea' author='Ivan Aivazovsky'/>
        <picture name='The Black Square' author='Kazimir Malevich'/>
        <picture name='Sunflowers' author='Vincent van Gogh'/>
    </gallery>