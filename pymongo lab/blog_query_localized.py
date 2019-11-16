from pymongo import MongoClient
import re
mongo_client = MongoClient("localhost", 27017)

db = mongo_client.lab4
coll = db.blogs
lang = "e"

while True:
	if lang is "e":
		print("Please select an option")
		print("1. Search by title")
		print("2. Search by content")
		print("3. Search by tags")
		print("4. Language settings")
		print("5. Exit")
	elif lang is "l":
		print("Elige optionem")
		print("1. Quaere per titulum")
		print("2. Quaere per contentum")
		print("3. Quaere per notam")
		print("4. Optiones linguae")
		print("5. Exit")
	selection = raw_input("")
	if selection is "5":
		if lang is "e":
			print("Bye")
		elif lang is "l":
			print("Vale")
		break
	elif selection is "1":
		search_field = "Title"
	elif selection is "2":
		search_field = "Content"
	elif selection is "3":
		search_field = "Tags"
	elif selection is "4":
		if lang is "e":
			print("Choose a language")
			print("1. English")
			print("2. Latin")
		if lang is "l":
			print("Elige linguam")
			print("1. Anglica")
			print("2. Latine")
		lang_select = raw_input("")
		if lang_select is "1":
			lang = "e"
		elif lang_select is "2":
			lang = "l"
		continue
	else:
		if lang is "e":
			print("Invalid selection")
		elif lang is "l":
			print("Selectio invalidus")
		continue
	if lang is "e":
		display = "Please enter a search term: "
	elif lang is "l":
		display = "Inserta sermo pro investigatium: "
	search_term = raw_input(display)	
	regx = re.compile(search_term)	
	result = coll.find({search_field: regx})
	i = 0
	print("")
	for p in result:
		i += 1
		print(p["Title"])
	if i == 0:
		if lang is "e":
			print("No entries found")
		elif lang is "l":
			print("Exitum nullum")
	print("")