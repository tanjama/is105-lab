# -*- coding: latin-1 -*-
"""Romertall til Titall"""

print 'Begynn med Bokstav med Høyest verdi til venstre så nest høyest til høyre for den også videre'
print 'hver bokstav kan ha et negativt tall på venstre side'
print 'eks: 4 = IV, 3 = VIII, 9 = IX, 45 = VL'
roman_number = raw_input("skriv inn rommertall med bokstaver mellom I og M: ")
print roman_number.upper()


def roman_to_int(romIn):
	runBool = False #runBool blir satt til True hvis input verdien er gyldig
	romIn = romIn.upper() #sett alle bokstavenen til uppercase
	value_list = [] #list til bokstavenes tall verdi
	sum = 0
	for char in romIn: #check om input verdi er gyldig
		if char == 'I'or char == 'V' or char == 'X' or char == 'L' or char == 'C' or char == 'D' or char == 'M':
			runBool = True
	for char in romIn: #legger bokstavenes tall verdi i value_list
		if char == 'M':
			value_list.append(1000)
		elif char == 'D':
			value_list.append(500)
		elif char == 'C':
			value_list.append(100)
		elif char == 'L':
			value_list.append(50)
		elif char == 'X':
			value_list.append(10)
		elif char == 'V':
			value_list.append(5)
		elif char == 'I':
			value_list.append(1)
	print value_list
	
	for i, item in enumerate(value_list):
		print "index: %s, item: %s" %(i, item)
		if item < value_list[i+1]:
			sum -= item
		else:
			sum += item
		
	print sum
	print runBool

roman_to_int(roman_number)


"""Titall til Romertall"""