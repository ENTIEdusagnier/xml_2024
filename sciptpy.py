#!/usr/bin/python3

from xml.dom import minidom

facx = minidom.parse('characters.facx')

characters = facx.getElementsByTagName('character')

for character in characters:
		
	name = character.getElementsByTagName('name')
	print(name[0].firstChild.nodeValue)
	
	age = character.getElementsByTagName('age')
	print(age[0].firstChild.nodeValue)
	
	gender = character.getElementsByTagName('gender')
	print(gender[0].getAttribute('value'))

	level = character.getElementsByTagName('level')
	print(level[0].getAttribute('value'))

	print("\n")
