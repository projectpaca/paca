# Projektförslag 1 (19/1)

En webbapplikation för schemabokning, där målgruppen primärt gäller anställda som bokas löpande (bemanning). 

OBS!
Bilderna ska lämnas in som en pdf-fil enligt mallen som utgörs av filen da336a_projektforslag_mall_vt18.pptx. Filen som lämnas in ska ha filnamn enligt formeln da336a_projektforslag_grupp_xx.pdf där xx motsvarar gruppens nummer. Inlämning sker via tilldelad plats på It’s Learning

• Varje presentationsbild ska innehålla information om gruppnummer.

## Tänkta funktioner
* Micro interactions, såsom “Wohoo! OB!” när ens pass går sent inpå kvällen.
* Kunna exportera statisk schemafil eller prenumerera på schemat i ens egna kalender.
* Inloggning, med olika funktioner och begränsningar beroende på om det är en chef/arbetsgivare eller anställd som är inloggad.
* Attribut för anställda
	* Kompetens
	* Vanligt arbetsområde (så att chefen kanske inte väljer någon som aldrig jobbat i gällande avdelning förut)
	* Begränsningar, såsom körkort.
* Begränsningar och permissions
	* Arbetsgivare vs anställd
	* Inte kunna jobba för mycket
* Funktionen “Boka pass” godkänns automatiskt, medan passbokningar med speciella omständigheter (“Jag kan inte komma in förrän efter två timmar”) eller begränsningar (har inte körkort, men distanserna är korta nog för att kunna cykla) måste godkännas manuellt av chefen.
	* Vad händer när någons bokning måste godkännas? Pausas möjligheten att boka för alla andra?

## Beskrivning av de huvudsaklig funktionerna
Paca är ett bokningssystem som underlättar bokning av personal eller bokning av extrapass, riktat till företag med timanställda. Som anställd kan du meddela när du kan jobba, eller boka upp tillgängliga pass, och som chef kan du lägga ut tillgängliga pass eller boka anställda som anmält att dom kan jobba under den tidsintervallen du söker. En önskad, men inte prioriterad, funktionalitet är att anställda självständigt, med minimal inblandning av schemaansvarig, ska kunna byta pass. Paca är bokningssystemet som inte är bundet till ett specifikt företag, utan en tjänst företag kan ansluta sig till oavsett antal anställda.

## Inspiration: Netwic
Netwic är den webbtjänst som IKEA använder för schemabokning av sina anställda i sina varuhus. Vi valde att titta på den för att ge oss själva en bild av vad som krävs av en sådan applikation – men kanske ännu mer för att ta reda på vad vi inte ska göra.

Se Netwics inspirationsmapp för bilder.

### Nackdelar
* Loggan i navigeringens vänstra hörn är inte klickbar (och leder således inte till startsidan, vilket är det förväntade resultatet)
* Enbart exportering till PDF
* I schemat finns det tre kryssalternativ för tre tider på dygnet, vilka finns i en orange nav ovanpå schemat. Eftersom det inte är en sticky nav, så hänger den inte med när man scrollar ned – och således måste användaren förlita sig på minnet för att veta vilken tid på dygnet som varje kryssalternativ representerar.
* Kryssrutorna representerar endast tid på dygnet, och indikerar inte huruvida det finns pass lediga på dessa tider eller inte.
* Den vertikala layouten i schemat är under all kritik. Se “Consistency and standards” i Nielsens heuristik för förklaring till varför det är fördelaktigt att designa efter rådande industristandarder vad gäller UI.
* Efter att “fler sökalternativ” expanderats så spegelvänds pilen bredvid texten §(förväntat beteende), vilket indikerar för användaren att denne bör klicka på pilen igen för att stänga menyn igen. Problemet ligger i att texten inte ändras när menyn expanderas, så användaren får tämligen motsägande budskap av pilen respektive “fler sökalternativ”. Ett bättre alternativ vore att skriva “Avancerade sökalternativ” eller ändra texten till “Färre sökalternativ” vid expansion.
	
	
## Målgrupp
Paca inriktar sig mot företag med timanställda som jobbar i pass/med flextider. Användarna bör ha grundläggande datakunskaper och en vilja att använda datorsystem. Paca är för såväl små som stora företag. 

## Tekniska krav
Kunskaper i HTML & CSS, Python samt JavaScript. 

## Rekrytering
* Alla medlemmar ska vara intresserade av användbarhet och tillgänglighet på webben.
* Alla medlemmar ska ha förståelse och kunskaper inom HTML, CSS och Python.
* Alla gruppmedlemmar ska vara villiga att mötas upp (fysiskt) minst en gång i veckan. 
* En person ska sitta på kunskaper inom JavaScript och kunna skriva och förstå kod i JavaScript.
* Minst en person med kunskaper inom illustration och design. 
* ALLA medlemmar måste vara goa och glada och villiga att arbeta och fika ;)

## Utmaningar
* Kunskaper inom JavaScript och illustration är en utmaning för oss då vi i den ordinarie gruppen inte, iallafall inte i någon större utsträckning, kan detta. 
* En annan utmaning är vår design. Då vi vill ge användaren valmöjligheter och själva bestämma och styra sin användning (user control and freedom), men samtidigt inte för mycket frihet då det det vara enkelt att använda. Så begränsningar (constrains) är nödvändiga. 
* OM ingen med kunskaper inom JavaScript eller illustration är intresserade av att medverka i Paca behöver vi i gruppen själva sätta oss in i dessa områdena, vilket kommer kräva tid. 



