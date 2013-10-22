alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(userString):
	string = ""
	toAdd = 2
	for c in userString:
	
		indexNumber = alfabet.index(c)
		if c == " ":
			string = string + ":"
		elif indexNumber >= 25 :
			
			print indexNumber
			# Encrypt
			newNumber = indexNumber - 25

			# Output
			c = alfabet[newNumber]
			string = string + c
		else:
			# Encrypt
			newNumber = indexNumber + toAdd

			# Output
			c = alfabet[newNumber]
			string = string + c
	print string
			

userString = raw_input("String to encrypt ")
userString = userString.lower()

encrypt(userString)