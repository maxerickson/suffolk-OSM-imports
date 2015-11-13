#! python3

import argparse
from xml.etree import ElementTree

if "__main__"==__name__:
	parser = argparse.ArgumentParser()
	parser.add_argument('infile')
	parser.add_argument('outfile')
	args = parser.parse_args()
	intree=ElementTree.parse(args.infile)
	with open(args.outfile, 'w') as outfile:
		outfile.write("<?xml version='1.0' encoding='UTF-8'?>\n")
		outfile.write("<osm version='0.6' upload='true' generator='names.py'>\n")
		for event, elem in ElementTree.iterparse(args.infile):
			if event=='end':
				if elem.tag=='tag':
					if elem.get('k')=='name':
						old=elem.get('v')
						new=old.title()
						elem.attrib['v']=new
						print(old, '--', new)
			if elem.tag in ['node','way','relation']:
				outfile.write(ElementTree.tostring(elem, encoding='unicode'))
				elem.clear()
		outfile.write("</osm>\n")