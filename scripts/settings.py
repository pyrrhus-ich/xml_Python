import os

# holt den Pfad des Oberverzeichnisses
wdir = os.path.abspath("./.") #/home/ich/Dokumente/xml_Python

def dir(ext):
    dir = wdir + ext
    return dir

srcDir = dir("/src/")
dstDir = dir("/dst/")
logDir = dir("/log/")






