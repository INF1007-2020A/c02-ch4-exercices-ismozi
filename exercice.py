#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	
	

	return len(string)%2 == 0


def get_num_char(string, char):
	compteurChar=0
	for chars in string:
		if char==chars:
			compteurChar+=1

	return compteurChar


def get_first_part_of_name(name):
	premierNom=''
	
	for char in name:
		if char != '-':
			premierNom+=char
		else:
			break
	
	capitalized = 'Bonjour, '+premierNom.capitalize()

	return capitalized


def get_random_sentence(animals, adjectives, fruits):


	words = []

	for word_set in (animals, adjectives, fruits):
		words += [word_set[random.randrange(len(word_set))]]

	phrase = 'Aujourd’hui, j’ai vu un '+ words[0]+' s’emparer d’un panier '+ words[1] +' plein de '+words[2]+'.'


	return phrase


if __name__ == "__main__":
	spam = "Bonjour"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
