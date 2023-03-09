import xml.sax

class Listener(xml.sax.ContentHandler):


  def __init__(self):
    self.currentData = ""
    self.tag = ""
    self.type = ""
    self.name = ""
    self.lat = ""
    self.lon = ""
    self.hasAmenity = False
    self.hasToPrint = False

  

  def startElement(self, tag, attributes):    
    self.currentData = ""
    if tag == 'node':
        self.lat = attributes.get('lat')
        self.lon = attributes.get('lon')
    if tag =="tag":  
      if attributes.get("k") == "amenity":
        self.hasAmenity = True
        self.type = attributes.get('v')
        self.hasToPrint = True
      if attributes.get("k") == "name" and self.hasAmenity:
        self.hasAmenity = False
        self.name = attributes.get('v')
        
    

  def endElement(self, tag):    
    if tag =="node" and self.hasToPrint:	
      print("Nome:", self.name) 
      print("Tipo:", self.type) 
      print("lat:", self.lat) 
      print("lon:", self.lon) 
      self.hasToPrint = False

  def characters(self, content):	
    self.currentData += content

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("muritiba.osm")