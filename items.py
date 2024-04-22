#!/usr/bin/python3

from xml.dom import minidom

faix = minidom.parse('items.faix')

items = faix.getElementsByTagName('item')

for item in items:
		
	name = item.getElementsByTagName('name')
	print(name[0].firstChild.nodeValue)
	
	type_value = item.getElementsByTagName('type')
	print(type_value[0].getAttribute('value'))

	rareness = item.getElementsByTagName('rareness')
	print(rareness[0].getAttribute('value'))

	print("\n")
