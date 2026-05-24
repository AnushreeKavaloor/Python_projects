print("–––MENU–––")
print("1.Add new note\n2.View all saved notes\n3.Erase content in file and create fresh\n4.Exit")

while True:
	try:
		choice = int(input("Enter your choice: "))
		if choice==1:
			with open("my_note.txt", "a") as file:
				note = input("Type your note:\n")
				file.write(f"{note}\n")
		elif choice==2:
			with open("my_note.txt","r") as file:
				content =file.read()
				if content:
					print(content)
				else:
					print("No notes found. Add one first")
		elif choice==3:
			with open("my_note.txt", "w") as file:
				print("Erased the old content!")
		elif choice==4:
			break
		else:
			print("You must chose 1-4")
	except ValueError:
		print("You must choose only number from 1 to 4")
	except FileNotFoundError:
		print("File not created yet. You first create the file by choosing 1 to add note")
	finally:
		print("–––––")
