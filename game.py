# all the stuff the user if holding onto.
inventaris = {}


def beantwoordVraag(vraag, opties):
	foutantwoord = True
	while foutantwoord:
		antwoord = input(vraag + " (" + ",".join(opties) + ") ")
		foutantwoord = False; # wishful thinking....
		if antwoord.upper() in opties:
			return antwoord.upper()
		else:
			print ("hint: answer must be one of " + ",".join(opties) + ", try opnieuw.")
			foutantwoord = True; # Foiled!

def intro():
	print("This is the introduction of the game....")

def spelvoorbij():
	print("GAME OVER!")
	opnieuw = beantwoordVraag("Would you like to play again?", ["Y","N"])
	if opnieuw == "N":
		exit()
	inventaris = {}
	intro()
	kamer0()

def kamer1():
	print("This is room 1, it is north of the town square. The only option from here is south (S).");
	antwoord = beantwoordVraag("Which way do you want to go?", ("S"))
	if antwoord == "S":
		kamer0()
	else:
		print("This is not a possible answer.... how did you get here?")

def kindBiedtKipAan():
	print("There is a kid trying to give you a chicken. Do you want the chicken?");
	antwoord = beantwoordVraag("Take chicken?", ("Y","N"))
	if antwoord == "Y":
		print("You took the chicken.");
		if not "chicken" in inventaris:
			inventaris["chicken"] = 0
		inventaris["chicken"] += 1
		print ("You have " + str(inventaris["chicken"]) + " chickens.")
	else:
		print("You did not take the chicken")

def kamer2():
	print("This is room 2, it is south of the town square.")
	if not "chicken" in inventaris:
		kindBiedtKipAan()
	print("You decide to head north again...")
	kamer0()

def biedKipAan():
	antwoord = beantwoordVraag("Do you offer your chicken to the old lady?", ("Y","N"))
	if antwoord == "Y":
		print("She takes your chicken and opens the door. YOU WIN!")
		spelvoorbij()
	else:
		print("She stabs you and takes your chicken. YOU DIE.")
		spelvoorbij()

def kamer4():
	print("There is a steep cliff here. You decide to look over it. You lean right out.")
	print("You fall. You die.")
	spelvoorbij();

def kamer3():
	print("There is a golden door. An old lady stands next to it. A sign says 'entry price one chicken.'")
	if not "chicken" in inventaris:
		print("It is a pity you do not have a chicken.")
		print("You return to the west.")
		kamer0()
	else:
		biedKipAan()

def kamer0():
	print("You are standing in a town square. Pathways lead to the north (N), south (S), east (E) and west (W).")
	antwoord = beantwoordVraag("Which way do you want to go?", ("N","S","E","W"))
	if antwoord == "N":
		kamer1()
	elif antwoord == "S":
		kamer2()
	elif antwoord == "E":
		kamer3()
	elif antwoord == "W":
		kamer4()

# here is the starting point of the game...
intro()
kamer0()
