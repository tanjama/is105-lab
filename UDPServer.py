# -*- coding: utf-8 -*-
from socket import * # Importerer socket modulen, som gjør at vi kan opprette sockets.
serverPort = 12000 # Definerer variabelen serverPort til 12000.
serverSocket = socket(AF_INET, SOCK_DGRAM) # Oppretter en socket kalt serverSocket. AF_INET indikerer at det brukes IPv4.
                                           # SOCK_DGRAM viser at det er en UDP socket, i stede for en TCP socket.
serverSocket.bind(("", serverPort)) # Binder port nummer 12000 til socketen, slik at alt som blir sendt til port 12000,
                                    # blir sendt til denne socketen.
print "The server is ready to receive" # Printer at serveren fungerer som den skal.
while 1: # Lar serveren kjøre på ubestemt tid, frem til den avsluttes manuelt.
    message, clientAddress = serverSocket.recvfrom(2048) # Når det mottas en melding, settes denne inn i variabelen message,
                                                         # avsenders addresse settes i clientAddress, og brukes som returaddresse.
    print message # Printer meldingen som mottas, slik den er i lower case.
    print ' '.join(format(ord(x), 'b') for x in message) # Printer alle bokstavene i meldingen sendt i lower case, presentert 
                                                         # som binærtall.
    modifiedMessage = message.decode("utf-8").upper() # Tar imot meldingen i lower case, og gjør den om til upper case.
                                                      # Her må også dekodes, for å kunne gjør om non-ascii til upper case.
    print ' '.join(format(ord(x), 'b') for x in modifiedMessage) # Printer alle bokstavene i den modifiserte meldingen i upper
                                                                 # case, presentert som binærtall.
    serverSocket.sendto(modifiedMessage.encode("utf-8"), clientAddress) # Fester returaddresse (clientAddress) til pakken med
                                                                        # den modifiserte meldingen i upper case, og sender
                                                                        # den i retur.
