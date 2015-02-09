# -*- coding: latin-1 -*-
"""Romertall til Titall
Funksjonen tar inn et romertall mellom I og M og gir ut et tall i titallssystemet(desimalltall)"""

#Kode-blokk til Demo i console
print 'Bokstav med høyest verdi settes til venstre. Deretter settes tall etter høyest verdi mot høyre.'
print 'I stedet for desimal rangering (1,2,3,4,5 osv) brukes romersk gradering (1000, 500, 100, 50, 10 osv).'
print 'Hver bokstav kan ha et negativt tall på venstre side. Dvs at det negative tallet trekkes fra det postive tallet som er stilt til høyre.'
print 'eks: 4 = IV(5 - 1), 7 = VII(5 + 1 + 1) , 9 = IX (10 - 1), 45 = XLV(50 - 10 + 5)'
roman_number = raw_input("Skriv inn rommertall med bokstaver mellom I og M: ")


def roman_to_int(romIn):
	runBool = True #runBool blir satt til True hvis input-verdien er gyldig (Hvordan vite om input verdien ER gyldig?)
	romIn = romIn.upper() #Setter alle bokstavenen til uppercase.
	value_list = [] #Liste til bokstavenes(romertallenes) tall-verdi.
	char_list = []
	sum = 0
	for char in romIn: #Check om input-verdi er gyldig
		if char == 'I'or char == 'V' or char == 'X' or char == 'L' or char == 'C' or char == 'D' or char == 'M':
			char_list.append(char)
		else:
			runBool = False
	print char_list
	if runBool == True:
		for char in romIn: #Legger bokstavenes tall-verdi i value_list.
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
		
		for i, item in enumerate(value_list): #Ser etter negative verdier og legger sammen i sum variabel.
			print "index: %s, item: %s" %(i, item)
			try:
				if item < value_list[i+1]:
					sum -= item
				else:
					sum += item
			except:
                                sum += item
                                print "Done"
		return sum
	else:
		return "Not valid number"

print roman_to_int(roman_number)


"""Titall til Romertall"""
number_in_raw = raw_input("skriv in et tall: ")

def int_to_roman(number_in_string):
	number_in = int(number_in_string)
	result = []
	while number_in > 0:	
		if number_in >= 1000:
			number_in -= 1000
			result.append("M")
			
		elif number_in >= 900:
			number_in -= 900
			result.append("CM")
			
		elif number_in >= 500:
			number_in -= 500
			result.append("D")
			
		elif number_in >= 400:
			number_in -= 400
			result.append("CD")
			
		elif number_in >= 100:
			number_in -= 100
			result.append("C")
			
		elif number_in >= 90:
			number_in -= 90
			result.append("XC")
			
		elif number_in >= 50:
			number_in -= 50
			result.append("L")
			
		elif number_in >= 40:
			number_in -= 40
			result.append("XL")		
			
		elif number_in >= 10:
			number_in -= 10
			result.append("X")
			
		elif number_in >= 9:
			number_in -= 9
			result.append("IX")
			
		elif number_in >= 5:
			number_in -= 5
			result.append("V")
			
		elif number_in >= 4:
			number_in -= 4
			result.append("IV")
			
		elif number_in >= 1:
			number_in -= 1
			result.append("I")
			
	return "".join(result)

print int_to_roman(number_in_raw)

raw_input("")

























