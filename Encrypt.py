# Define functions, imports and lists
import random

# List with all letters for alfabet
alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Function for saving words
def saveOutput(originalString, toAdd, endString):
	in_file = open("output.txt", "a")
	text = in_file.write(originalString + "    " + str(toAdd) + "    " + endString + '\n')

# Function for encryption
def encrypt(originalString):
	toAdd = random.randint(1, 20)
	endString = ""
	for c in originalString:
	
		if c == " ":
			endString += ":"
		else:
			# Finds indexnumber and encrypts it
			indexNum = alfabet.index(c)
			encNum = indexNum + toAdd
		
			if encNum > 25:
				encNum = encNum - 26
			
			endString += alfabet[encNum]
	
	# Saves and prints word	
	print "Your encrypted word is: " + endString
	saveOutput(originalString, toAdd, endString)
	

# Asks for input
userString = raw_input("String to encrypt: ")
userString = userString.lower()

# Calls encrypt function
encrypt(userString)