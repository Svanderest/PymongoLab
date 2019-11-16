from pymongo import MongoClient
import re
import os
mongo_client = MongoClient("localhost", 27017)


db = mongo_client.lab4
coll = db.blogs

while True:
	print("Please select an option")
	print("1. Search by title")
	print("2. Search by content")
	print("3. Search by tags")
	print("4. Exit")
	selection = raw_input("")
	if selection is "4":
		print("Bye")
		break
	elif selection is "1":
		search_field = "Title"
	elif selection is "2":
		search_field = "Content"
	elif selection is "3":
		search_field = "Tags"
	else:
		print("Invalid selection\a")
		continue
	search_term = raw_input("Please enter a search term: ")	
	regx = re.compile(search_term)	
	while True:
		result = coll.find({search_field:regx})
		display_title = False
		display_content = False
		while True:
			print("Please select an option")
			print("1. Display title")
			print("2. Display content")
			print("3. Display all")
			selection = raw_input("")
			if selection is "1":
				display_title = True
				break
			elif selection is "2":
				display_content = True
				break
			elif selection is "3":
				display_title = True
				display_content = True
				break
			else:
				print("Invalid selection\a")
		i = 0
		print("")
		for p in result:
			i += 1
			if display_title:
				print(p["Title"])
			if display_content:
				print(p["Content"])
			print("")
		if i == 0:
			print("No entries found")
		selection = raw_input("Return to main menu? (y/n)")
		if selection is "y":
			os.system("cls")
			break