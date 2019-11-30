# all the stuff the user if holding onto.
inventory = {}


def answerQuestion(question, options):
	wronganswer = True
	while wronganswer:
		answer = input(question + " (" + ",".join(options) + ") ")
		wronganswer = False; # wishful thinking....
		if answer.upper() in options:
			return answer.upper()
		else:
			print ("hint: answer must be one of " + ",".join(options) + ", try again.")
			wronganswer = True; # Foiled!

def intro():
	print("This is the introduction of the game....")

def gameover():
	global inventory
	print("GAME OVER!")
	again = answerQuestion("Would you like to play again?", ["Y","N"])
	if again == "N":
		exit()
	inventory = {}
	intro()
	room0()

def room1():
	print("This is room 1, it is north of the town square. The only option from here is south (S).");
	ans = answerQuestion("Which way do you want to go?", ("S"))
	if ans == "S":
		room0()
	else:
		print("This is not a possible answer.... how did you get here?")

def kidOffersChicken():
	print("There is a kid trying to give you a chicken. Do you want the chicken?");
	ans = answerQuestion("Take chicken?", ("Y","N"))
	if ans == "Y":
		print("You took the chicken.");
		if not "chicken" in inventory:
			inventory["chicken"] = 0
		inventory["chicken"] += 1
		print ("You have " + str(inventory["chicken"]) + " chickens.")
	else:
		print("You did not take the chicken")

def room2():
	print("This is room 2, it is south of the town square.")
	if not "chicken" in inventory:
		kidOffersChicken()
	print("You decide to head north again...")
	room0()

def offerChicken():
	ans = answerQuestion("Do you offer your chicken to the old lady?", ("Y","N"))
	if ans == "Y":
		print("She takes your chicken and opens the door. YOU WIN!")
		gameover()
	else:
		print("She stabs you and takes your chicken. YOU DIE.")
		gameover()

def room4():
	print("There is a steep cliff here. You decide to look over it. You lean right out.")
	print("You fall. You die.")
	gameover();

def room3():
	print("There is a golden door. An old lady stands next to it. A sign says 'entry price one chicken.'")
	if not "chicken" in inventory:
		print("It is a pity you do not have a chicken.")
		print("You return to the west.")
		room0()
	else:
		offerChicken()

def room0():
	print("You are standing in a town square. Pathways lead to the north (N), south (S), east (E) and west (W).")
	ans = answerQuestion("Which way do you want to go?", ("N","S","E","W"))
	if ans == "N":
		room1()
	elif ans == "S":
		room2()
	elif ans == "E":
		room3()
	elif ans == "W":
		room4()

# here is the starting point of the game...
intro()
room0()
