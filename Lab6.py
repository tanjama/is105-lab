Lab 6 

Oppgave 1

a) HTTP Get meldingen ble sendt ut etter 3.171428000 sekunder, og vi mottok HTTP Get Ok etter 3.189186000 sekunder. Det vil si at det tok 0.017758 sekunder fra da HTTP Get meldingen ble sendt ut til vi mottok HTTP GET Ok meldingen.

b)
Get = Den ber om en represtasjon av en spesefik resurs. forspørselen som bruker GET skal bare motta data, og ikke ha noen andre effekter.
Connection = Den konverterer forsespørselen om tilkobling til en åpenbar/gjennomsiktig TCP/IP tunnel. målet med dette er for å legge til rette for SSL kryptert kommunkasjon(HTTPS) gjennom en ukrypter HTTP server.
Host = Det er siden vi henter informasjon fra eller den siden vi er på i dette tilfelle er det http://www-net.cs.umass.edu/
Accept = Accept førespørselen brukes til å spesifisere hvilke mediatyper som er akseptable for responsen fra hosten. Accept forespørselen kan også inneholde parametere som setter en standard for kvaliteten på innholdet.
Origin = Denne headeren kommer fra brukersiden, og beskriver hvilke sikkherhetskontekster som gjorde at brukeren startet en http forespørsel. Serversiden kan bruke origin headeren for å forsikre seg om at brukerens nettleser kan stoles på.
Accept Encoding = Accept Encoding forespørsel-header feltet er lik som Accept, men begrenser innholdet i koden som er akseptert for en tilbakemelding.  Når en server tester om koden er akseptabel i forhold til Accept Encoding bruker man følgene regler : 1. Hvis koden er listet i Accept Encoding feltet er dette akseptabelt, men hvis qvalue = 0 er dette ikke akseptabelt. 2. Symbolet «*» i et Accept Encoding felt matcher alle tilgjengelige koder og må ikke være listet i header feltet. 3. Hvis flere koder er akseptable, blir den koden som har høyest verdi fra qvalue 1+ valgt. 4. «Identity» innholds koden er alltid akseptabel, hvis den ikke spesifikt inneholder «identity;q=0», eller fordi feltet inkluderer «*q=0». Hvis Accept Encoding feltets verdi er tom er bare selve «identity» akseptabel. 
Accept Language = Accept Language forespørsel-header feltet er lik som Accept, men begrenser språkene som er foretrukket som en respons av forespørselen. 
 