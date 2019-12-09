# alle spullen die de speler bij zich heeft
inventaris = {}


def beantwoordVraag(vraag, opties):
	foutantwoord = True
	while foutantwoord:
		antwoord = input("> " + vraag + " (" + ",".join(opties) + ") ")
		foutantwoord = False; # hopelijk gaat het goed....
		if antwoord.upper() in opties:
			return antwoord.upper()
		else:
			print ("hint: het antwoord moet één van " + ",".join(opties) + " zijn, probeer opnieuw.")
			foutantwoord = True; # toch niet!

def intro():
	print("Dit is de introductie van het spel....")

def spelvoorbij():
	global inventaris
	print("SPEL VOORBIJ!")
	opnieuw = beantwoordVraag("Zou je opnieuw willen spelen?", ["J","N"])
	if opnieuw == "N":
		exit()
	inventaris = {}
	intro()
	kamer0()

def kamer1():
	print("Dit is kamer 1, het is ten noorden van het stadsplein. Je kunt hier alleen naar het zuiden (Z)).");
	antwoord = beantwoordVraag("Welke kant wil je op?", ("Z"))
	if antwoord == "Z":
		kamer0()
	else:
		print("Dit antwoord is niet mogelijk.... hoe ben je hier überhaupt gekomen?")

def kindBiedtKipAan():
	print("Er is een kind dat je een kip aanbiedt. Wil je de kip hebben?");
	antwoord = beantwoordVraag("Neem de kip?", ("J","N"))
	if antwoord == "J":
		print("Je hebt de kip aangenomen.");
		if not "kippen" in inventaris:
			inventaris["kippen"] = 0
		inventaris["kippen"] += 1
		print ("Je hebt " + str(inventaris["kippen"]) + " kippen.")
	else:
		print("Je hebt de kip niet genomen")

def kamer2():
	print("Dit is kamer 2, het is ten zuiden van het stadsplein.")
	if not "kippen" in inventaris:
		kindBiedtKipAan()
	print("Je besluit naar het noorden te gaan...")
	kamer0()

def biedKipAan():
	antwoord = beantwoordVraag("Bied je je kip aan de oude dame aan??", ("J","N"))
	if antwoord == "J":
		print("Ze neemt je kip en opent de deur. JE WINT!")
		spelvoorbij()
	else:
		print("Ze steekt je en neemt je kip. JE STERFT.")
		spelvoorbij()

def kamer4():
	print("Er is hier een steil klif. Je besluit over de rand te kijken. Je leunt er een beetje over.")
	print("Je valt. Je sterft.")
	spelvoorbij();

def kamer3():
	print("Er is een gouden deur. Een oude dame staat ernaast. Op een bord staat 'entree één kip'.")
	if not "kippen" in inventaris:
		print("Het is jammer dat je geen kip hebt.")
		print("Je keert terug naar het westen.")
		kamer0()
	else:
		biedKipAan()

def kamer0():
	print("Je staat op een dorpsplein. Paden leiden naar het noorden (N), zuiden (Z), oost (O) en west (W).")
	antwoord = beantwoordVraag("Welke kant wil je op?", ("N","Z","O","W"))
	if antwoord == "N":
		kamer1()
	elif antwoord == "Z":
		kamer2()
	elif antwoord == "O":
		kamer3()
	elif antwoord == "W":
		kamer4()

# dit is het startpunt van het spel...
intro()
kamer0()
