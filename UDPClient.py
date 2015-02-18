# -*- coding: latin-1  -*-


from socket import * # Importerer socket modulen, som gjør at vi kan opprette sockets.
serverName = "localhost" # Definerer navnet på serveren, f.eks IP-addresse eller i dette tilfellet 'localhost'.
serverPort = 12000 # Definerer variabelen serverPort til 12000.
clientSocket = socket(AF_INET, SOCK_DGRAM)  # Oppretter en socket kalt clientSocket. AF_INET indikerer at det brukes IPv4.
                                            # SOCK_DGRAM viser at det er en UDP socket, i stede for en TCP socket.
while 1: # Gjør slik at man kan sende flere setninger etter hverandre, uten at programmet slutter.
    message = raw_input("Input lowercase sentence:").decode("utf-8") # Gir en prompt til brukeren for å skrive inn
                                                                     # meldingen som skal sendes. Dekoder til utf8 for å kunne
                                                                     # behandle non-ascii tegn og bokstaver.
    clientSocket.sendto(message.encode("utf-8"), (serverName, serverPort)) # Metoden sendto() fester mottakers addresse til 
                                                                           # meldingen, og sender den til socketen clientSocket.
                                                                           # Enkoder til utf8 for å kunne behandle æøå osv.
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # Metoden recvfrom tar i mot pakken, og setter den i variabelen
                                                                 # modifiedMessage, og setter avsenders addresse i vaiabele
                                                                 # serverAddress.
    print modifiedMessage.decode("utf-8") # Til slutt printes meldingen som kommer i retur fra UDPServer, og dekodes i utf8
                                          # slik at også tegn utenom ASCII tabellen kommer med i UPPER case.
clientSocket.close()
