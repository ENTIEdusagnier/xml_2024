#!/usr/bin/python3

from bs4 import BeautifulSoup


archivo = open('characters.facx', 'r')

soup = BeautifulSoup(archivo, 'xml')

characters = soup.find_all("character")

num_characters = len(characters)

personaje = int(input("Que personaje quieres NUM: "))

if personaje > num_characters:
	print ("Numero insertado es mayor de los characters que hay")
	exit(1)


iteraciones = 1

for character in characters:
	
	if iteraciones == personaje:
		print(f"{character['id']} \t {character.find('name').text} \t {character.find('age').text} \t {character.find('gender')['value']} \t {character.find('level')['value']}")
	
	iteraciones +=1

