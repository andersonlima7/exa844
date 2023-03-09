from xml.dom.minidom import parse

BancoDocument = parse('muritiba.osm')

print("Starting DOM Parser...")
for c in BancoDocument.getElementsByTagName("node"):
	if(c.getElementsByTagName("tag").length > 0):
		if(c.getElementsByTagName("tag").item(0).getAttribute("k") != 'amenity'): continue
	else: continue
	for el in c.getElementsByTagName("tag"):
		if(el.getAttribute("k") == 'name'): 
			print("Nome:", el.getAttribute("v"));	
		elif (el.getAttribute("k") == 'amenity') :
			print("Tipo:", el.getAttribute("v"));
			print("Lat:", c.getAttribute("lat"))
			print("Long:", c.getAttribute("lon"))
        


