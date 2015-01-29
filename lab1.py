# -*- coding: latin-1 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#         
#
#
import sys

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': "Kevin Benjamin Zeppo Adriaansen",
			'student2': "Stanley Ntiamoah",
            'student3': "Vegard Nerland",
            'student4': "Kenneth Rønning",
            'student5': "Tanja Malbasa",
            'student6': "Rachel Victoria Legreid",
            'student7': "Thomas Ørsnes",
            'student8': "Jostein Nilsen",
}

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
#  print"       \/_ "
#  print"  \,   /( ,/ "
#  print"   \\\' /// "
#  print"    \_ /_/ "
#  print"    (./ "
#  print"     '` " 
#
# Setter en simpel print for fugelen, kunne også ha brukt (""")
# 
def ascii_bird():
	print"       \/_"
	print"  \,   /( ,/ "
	print"   \\\' /// "
	print"    \_ /_/ "
	print"    (./ "
	print"     '` "
ascii_bird()

# 
#  Oppgave 2
#    bitAnd - x&y
#	 Implementer funksjonen som gjør en "bitwise" AND operasjon (erstatt pass)
#    Eksempel: bitAnd(6, 5) = 4
#		Forklaring: 6 binært er 110, mens 5 er 101. Hvis vi sammenligner bitvis
#					1 AND 1 gir 1, 1 AND 0 gir 0 og 0 AND 1 gir 0 => 100 binært
#					er 4 desimalt. Antagelse: posisjonsbasert tallsystem og 
#					den mest signifikante bit-en er lengst til venstre
a = 6
b = 5
def bitAnd(x, y):

	return x&y
print "oppgave 2 svar = %s " % bitAnd(a,b)

	#tar to tall i base 10 å gjør de om til en rekke med bool verdier i form av bin tall (base 2)
	#så sammen lignes verdiene i en sannhetstabell. 1 og 1 blir 1, 1 og 0 blir 0, 0 og 0 blir 0, 1 = True, 0 = False
	


    
#
# Lager variabler som settes inn i en viseflow funksjonen, returnerer og printer ut svaret
#
 
#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
a = 4
b = 5

def bitXor(x, y):

	return x^y
print "oppgave 3 svar = %s " % bitXor(a, b)
#
# Mye av det samme som over bare en anen viseflow funksjon
#
#
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
a = 5
b = 4

def bitOr(x, y):
	return x|y


print "oppgave 4 svar = %s" % bitOr(a, b)

#
# Samme som over igjen bare en annen viseflow-funksjon.
#

#  Oppgave 5
#
#  Tips:
#    For å finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: prøv med bokstaven 'å', f.eks.)
#	 Forklar resultatet ascii8Bin('å')
#	 Hvilke faktorer påvirker resultatet? Forklar.
#
def ascii8Bin(tegn):
    tegn = ord(tegn)
    return '{0:08b}'.format(tegn)

    print ascii8Bin('a')
# Grunnen til at vi ikke kan bruke "å" er på grunn av at ascii-biblioteket ikke er utvidet/definert til å ta i bruk norske tegn. 
# Resultatet av asciiBin8 8('å') er:
# Ascii sitt biblitoek påvirker resultatet. Det vil si at vi ikke kan ta i bruk udefinerte tegn for å få et fungerende resultat. 




#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#
def transferBin(string): 
	#string = "hei"
	l = list(string)
	#sprint 1
	
	for variabel in l:
	return	ascii8Bin(variabel)
		
print transferBin("Hei")

		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)
		print "Den binære representasjonen for %s" % c

#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
#  
def transferHex(string):
	l = list(string)
	for c in l:
	
		print Ascii8Bin(c)

#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen
def unicodeBin(character):
	pass 	

#
# Oppgave 9
# 	Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din 
#   datamaskin-node:
#
# 			Brand and model
# 			Hard drive capacity
# 			Amount of RAM
# 			Model and speed of CPU
# 			Display resolution and size
# 			Operating system
#	
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#
def printSysInfo():
	pass


def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	# Skriv her inn passende tester for tarnsferBin og transferHex funksjoner
	# fra oppgavene 6 og 7
	assert unicodeBin('å') == '11100101'
	# Dine egne tester
	return "Testene er fullført uten feil."


# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
print test()
		
