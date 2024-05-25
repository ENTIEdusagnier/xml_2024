#!/usr/bin/python3

from bs4 import BeautifulSoup


archivo = open('characters.facx', 'r')

soup = BeautifulSoup(archivo, 'xml')

characters = soup.find_all("character")

num_characters = len(characters)

opcion_entrar = int(input("Que quieres hacer:\n 1. Selecionar un informacion de un personaje \n 2. Matar a un personaje \n"))


for character in characters:
	print(f"{character['id']} \t {character.find('name').text}")


personaje = int(input("Que personaje quieres NUM: "))

if personaje > num_characters:
	print ("Numero insertado es mayor de los characters que hay")
	exit(1)


if opcion_entrar == 1:
	
	for character in characters:
		
		id_personaje = int(f"{character['id']}")

		if id_personaje == personaje:
			print(f"ID: {character['id']}")
			print(f"Nombre: {character.find('name').text}")
			print(f"Edad: {character.find('age').text}")
			print(f"Género: {character.find('gender')['value']}")
			print(f"Nivel: {character.find('level')['value']}")
	
	file = open('characters_weapons.facwx', 'r')
	soup_weapons = BeautifulSoup(file, 'xml')
	file.close()

	characters_weapons = soup_weapons.find_all('character_weapon')
	
	weapons_ids = []

	for character_weapon in characters_weapons:

		id_character = character_weapon.find("character")["id"]
		if int(id_character) == personaje:
			
			id_weapon = character_weapon.find("weapon")["id"]

			weapons_ids.append(id_weapon)

	
	if len(weapons_ids) == 0:
		print("El personaje no tiene armas")
		exit()

	file = open('weapons.fawx','r')
	soup = BeautifulSoup(file, 'xml')

	file.close()
	
	weapons = soup.find_all('weapon', {'id':True})
	
	daño = 0

	for weapon in weapons:
		if weapon['id'] in weapons_ids:
			daño += int(weapon.find('damage')['value'])
	
	print(f"Daño: {daño}")


elif opcion_entrar == 2:
	
	for character in characters:
		id_personaje_matar = int(f"{character['id']}")	
		
		if id_personaje_matar == personaje:
			character.decompose()

	
	archivo.close()

	archivo = open('characters.facx', 'w')
	archivo.write(str(soup))
	archivo.close

else:
	print("No hay esa opcion 1 o 2")
	exit(2)


