alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	
def encrypt(originalString):
	toAdd = 1
	endString = ""
	for c in originalString:
		indexNum = alfabet.index(c)
		encNum = indexNum + toAdd
		
		if encNum > 25:
			encNum = encNum - 26
			
		endString += alfabet[encNum]
		
	print "Your encrypted word is: " + endString
			

userString = raw_input("String to encrypt ")
userString = userString.lower()

encrypt(userString)