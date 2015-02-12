# -*- coding: latin-1 -*-
"""Romertall til Titall
Funksjonen tar inn et romertall mellom I og M og gir ut et tall i titallssystemet(desimalltall)"""

"""
def char_check(romIn_check ):
	for char in romIn: #Check om input-verdi er gyldig
			if not char == 'I' or char == 'V' or char == 'X' or char == 'L' or char == 'C' or char == 'D' or char == 'M':
				print char
			else:
				return False
"""
def roman_to_int(romIn):
	runBool = True #runBool blir satt til True hvis input-verdien er gyldig.
	romIn = romIn.upper() #Setter alle bokstavenen til uppercase.
	value_list = [] #Liste til bokstavenes(romertallenes) tall-verdi.
	sum = 0
	print romIn
	print runBool
	for char in romIn: #Check om input-verdi er gyldig
		if char == 'I' or char == 'V' or char == 'X' or char == 'L' or char == 'C' or char == 'D' or char == 'M':
			pass
		else:
			runBool = False
	print runBool	
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



"""Titall til Romertall
Funksjonen tall et desimalt tall og konverterer det til et tall med romerske symbol(romertall).
"""

def int_to_roman(number_in_string): #Funksjon som skal gjøre titall om til romertall. 
	number_in = int(number_in_string)
	result = []
	#Løkke som sjekker flere statements. Går gjennom input-tallet, sjekker verdien og sammenlikner verdien med et romertall. 
	#Hvis en verdi stemmer konverteres titallet til et romertall, og restverdien sjekkes igjen. 
	#Løkken fortsetter helt til det ikke er noen restverdi igjen. 
	while number_in > 0:	
		
		if number_in >= 1000: #Det desimale tallet konverteres til riktig symbol i det romerske tallsystemet. 

			number_in -= 1000
			result.append("M") #Romersk symbol. 
			
		elif number_in >= 900: #Elif står for else/if. 
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
			
	return "".join(result) #Setter resultatene sammen. I stedet for at reslutatet blir slik: 'M' 'D' 'C' 'L' 'X' 'V' 'I' blir det slik: MDCLXVI

"""Addisjon av romertall"""

def roman_plus_roman(rom_num1, rom_num2):
	runBool = True
	for char in rom_num1: #Check om input-verdi er gyldig
		if char == 'I' or char == 'V' or char == 'X' or char == 'L' or char == 'C' or char == 'D' or char == 'M':
			pass
		else:
			runBool = False
	for char in rom_num2: #Check om input-verdi er gyldig
		if char == 'I' or char == 'V' or char == 'X' or char == 'L' or char == 'C' or char == 'D' or char == 'M':
			pass
		else:
			runBool = False
	
	if runBool == True:
		rom_num1 = convert(rom_num1)
		rom_num2 = convert(rom_num2)
		rom_num_temp = rom_num1 + rom_num2
		rom_num_result = []
		rom_num_list = "MDCLXVI"
		for char in rom_num_list:
			for item in rom_num_temp:
				if item == char: 
					rom_num_result.append(item)
		
		return(revert("".join(rom_num_result)))
	else:
		return "not valid input"
def convert(rom_num):
	
	rom_num = rom_num.replace("CM", "DCCCC")
	rom_num = rom_num.replace("CD", "CCCC")
	rom_num = rom_num.replace("XC", "LXXXX")
	rom_num = rom_num.replace("XL", "XXXX")
	rom_num = rom_num.replace("IX", "VIIII")
	rom_num = rom_num.replace("IV", "IIII")
	return rom_num
	
def revert(rom_num):
    
	rom_num = rom_num.replace("IIIII", "V")
	rom_num = rom_num.replace("IIII", "IV")
	rom_num = rom_num.replace("VIIIII", "X")
	rom_num = rom_num.replace("VIIII", "IX")
	rom_num = rom_num.replace("VV", "X")
	rom_num = rom_num.replace("XXXXX", "L")
	rom_num = rom_num.replace("XXXX", "XL")
	rom_num = rom_num.replace("LXXXXX", "C")
	rom_num = rom_num.replace("LXXXX", "XC")
	rom_num = rom_num.replace("CCCCC", "D")
	rom_num = rom_num.replace("CCCC", "CD")
	rom_num = rom_num.replace("DCCCCC", "M")
	rom_num = rom_num.replace("DCCCC", "CM")
	rom_num = rom_num.replace("DD", "M")
	
	return rom_num


#Kode-blokk til Demo i console
print 'Bokstav med høyest verdi settes til venstre. Deretter settes tall etter høyest verdi mot høyre.'
print 'I stedet for desimal rangering (1,2,3,4,5 osv) brukes romersk gradering (1000, 500, 100, 50, 10 osv).'
print 'Hver bokstav kan ha et negativt tall på venstre side. Dvs at det negative tallet trekkes fra det postive tallet som er stilt til høyre.'
print 'eks: 4 = IV(5 - 1), 7 = VII(5 + 1 + 1) , 9 = IX (10 - 1), 45 = XLV(50 - 10 + 5)'
roman_number = raw_input("Skriv inn rommertall med bokstaver mellom I og M: ")
print roman_to_int(roman_number)

number_in_raw = raw_input("Write a number: ")# Her skrives et ønsket titall inn. 
print int_to_roman(number_in_raw) #Resultetet (de romerske symbolene) blir printet. 

rom1 = raw_input("input a valid roman numeral: ")
rom2 = raw_input("input a valid roman numeral: ")

print roman_plus_roman(rom1, rom2)

raw_input("")
