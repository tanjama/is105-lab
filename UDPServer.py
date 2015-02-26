# -*- coding: utf-8 -*-

from socket import * 
# Importerer socket modulen, som gjør at vi kan opprette sockets.

serverPort = 12000 
# Definerer variabelen serverPort til 12000.

serverSocket = socket(AF_INET, SOCK_DGRAM) 
# Oppretter en socket kalt serverSocket. AF_INET indikerer IPv4.
# SOCK_DGRAM viser at det er en UDP socket, i stede for en TCP socket.
                                           
serverSocket.bind(("", serverPort)) 
# Binder port nummer 12000 til socketen, slik at alt som blir 
# sendt til port 12000, blir sendt til denne socketen.

                                    
print "The server is ready to receive" 
# Printer at serveren fungerer som den skal.

def message_to_upper(message_in): 
    message_ut = []               
    for char in message_in:
        message_ut.append(chr(bitXor(ord(char))))
		
    return message_ut
# Her er vår funksjon for å gjøre meldingen om til upper case.
# Denne manipulerer bokstavene i 8-bit strenger i stede for
# å bruke .upper() funksjonen.

def bitXor(x):
    return x^32
# Funksjon for å utføre en bitwise xOR funksjon, for å flippe
# Den sjette bit'en og la oss gjøre om til upper case.
    #-----------------------------------------------------------------#

def roman_to_int(romIn):
    runBool = True #runBool blir satt til True hvis input-verdien er gyldig.
    romIn = romIn.upper() #Setter alle bokstavenen til uppercase.
    value_list = [] #Liste til bokstavenes(romertallenes) tall-verdi.
    sum = 0
    # print runBool
    for char in romIn: #Check om input-verdi er gyldig
        if char == 'I' or char == 'V' or char == 'X' or char == 'L' or char == 'C' or char == 'D' or char == 'M':
            pass
        else:
            runBool = False
    # print runBool	
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
        # print value_list
        
        for i, item in enumerate(value_list): #Ser etter negative verdier og legger sammen i sum variabel.
            # print "index: %s, item: %s" %(i, item)
            try:
                if item < value_list[i+1]:
                    sum -= item
                else:
                    sum += item
            except:
                sum += item
            # print "Done"
        return sum
    else:
        return "Not valid number"

    #-----------------------------------------------------------------#

def int_to_roman(number_in_string): #Funksjon som skal gjøre titall om til romertall. 
    run = True
    try:
        number_in = int(number_in_string)
    except:
        run = False
    result = []
    #Løkke som sjekker flere statements. Går gjennom input-tallet, sjekker verdien og sammenlikner verdien med et romertall. 
    #Hvis en verdi stemmer konverteres titallet til et romertall, og restverdien sjekkes igjen. 
    #Løkken fortsetter helt til det ikke er noen restverdi igjen. 
    if run == True:
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
    else:
        print "no valid input"

    #-----------------------------------------------------------------#

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
    
    rom_num = rom_num.replace("DD", "M")
    rom_num = rom_num.replace("DCCCCC", "M")
    rom_num = rom_num.replace("DCCCC", "CM")
    rom_num = rom_num.replace("CCCCC", "D")
    rom_num = rom_num.replace("CCCC", "CD")
    rom_num = rom_num.replace("LXXXXX", "C")
    rom_num = rom_num.replace("LXXXX", "XC")
    rom_num = rom_num.replace("XXXXX", "L")
    rom_num = rom_num.replace("XXXX", "XL")
    rom_num = rom_num.replace("VV", "X")
    rom_num = rom_num.replace("VIIIII", "X")
    rom_num = rom_num.replace("VIIII", "IX")
    rom_num = rom_num.replace("IIIII", "V")
    rom_num = rom_num.replace("IIII", "IV")

    return rom_num

def roman_addition(rom_num1, rom_num2):
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
    
    print rom_num1
    print rom_num2
    
    
def convert(rom_num):
    
    rom_num = rom_num.replace("CM", "DCCCC")
    rom_num = rom_num.replace("CD", "CCCC")
    rom_num = rom_num.replace("XC", "LXXXX")
    rom_num = rom_num.replace("XL", "XXXX")
    rom_num = rom_num.replace("IX", "VIIII")
    rom_num = rom_num.replace("IV", "IIII")
    
    return rom_num
    
def revert(rom_num):
    
    rom_num = rom_num.replace("DD", "M")
    rom_num = rom_num.replace("DCCCCC", "M")
    rom_num = rom_num.replace("DCCCC", "CM")
    rom_num = rom_num.replace("CCCCC", "D")
    rom_num = rom_num.replace("CCCC", "CD")
    rom_num = rom_num.replace("LL", "C")
    rom_num = rom_num.replace("LXXXXX", "C")
    rom_num = rom_num.replace("LXXXX", "XC")
    rom_num = rom_num.replace("XXXXX", "L")
    rom_num = rom_num.replace("XXXX", "XL")
    rom_num = rom_num.replace("VV", "X")
    rom_num = rom_num.replace("VIIIII", "X")
    rom_num = rom_num.replace("VIIII", "IX")
    rom_num = rom_num.replace("IIIII", "V")
    rom_num = rom_num.replace("IIII", "IV")
    
    return rom_num

    #-----------------------------------------------------------------#

while 1: 
# Lar serveren kjøre på ubestemt tid, frem til den avsluttes manuelt.

    message, clientAddress = serverSocket.recvfrom(2048) 
    # Når det mottas en melding, settes denne inn i variabelen message,
    # avsenders addresse settes i clientAddress, og brukes som 
    # returaddresse.
    
    print "The original message: " + message 
    # Printer meldingen som mottas, slik den er i lower case.
    
    print ("Binary representation of the original message: " + 
    ' '.join(format(ord(x), 'b') for x in message)) 
    # Printer alle bokstavene i meldingen sendt i lower case, presentert 
    # som binærtall.
    
    modifiedMessage = ''.join(message_to_upper(message)) 
    # Vår egen måte å konvertere melding fra lower til upper case.
    
    # modifiedMessage = message.decode("utf-8").upper() 
    # Kodeeksempelets måte å gjøre meldingen om til upper case.
    # Her må også dekodes, for å kunne gjør om non-ascii til upper case.
    
    print ("Binary representation of the modified message: " + 
    ' '.join(format(ord(x), 'b') for x in modifiedMessage)) 
    # Printer alle bokstavene i den modifiserte meldingen i upper
    # case, presentert som binærtall.
    
    serverSocket.sendto(modifiedMessage.encode("utf-8"), clientAddress)
    # Fester returaddresse (clientAddress) til pakken med den
    # modifiserte meldingen i upper case, og sender den tilbake i lower.
    
    #------------------------------------------------------------------#
    
    print "------------------------------------------------------------"
    
    romanIn, clientAddress = serverSocket.recvfrom(2048)
    
    print "Roman number to convert: " + romanIn
    
    intFromRoman = roman_to_int(romanIn)
    
    print "Integer value of the roman number: " + str(intFromRoman)
    
    serverSocket.sendto(str(intFromRoman), clientAddress)
    
    #------------------------------------------------------------------#
    
    print "------------------------------------------------------------"
    
    intIn, clientAddress = serverSocket.recvfrom(2048)
    
    print "Integer value to convert: " + intIn
    
    romanFromInt = int_to_roman(intIn)
    
    print "Roman number of the integer value: " + romanFromInt 
    
    serverSocket.sendto(str(romanFromInt), clientAddress)
    
    #------------------------------------------------------------------#
    
    print "------------------------------------------------------------"
    
    rom_num1, clientAddress = serverSocket.recvfrom(2048)
    
    rom_num2, clientAddress = serverSocket.recvfrom(2048)
    
    print "Roman numbers to be added: " + rom_num1 + " + " + rom_num2
    
    romanAdd = roman_addition(rom_num1, rom_num2)
    
    print "Result of roman addition: " + romanAdd
    
    serverSocket.sendto(str(romanAdd), clientAddress)
    
    print "------------------------------------------------------------"
