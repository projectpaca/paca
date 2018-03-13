# Mötesprotokoll 7/3

## Närvarande

* Milo Bengtsson (protokoll)
* Hanna Fellwing
* Lisa Wasslöv
* Victor Dahl

## To Do
* Milo Bengtsson:
	* Stäng Meeting Notes Templates
	* Deadlines på Slack
	* Daily check-in på Slack
	* Skriv över anteckningar kring ansvarsområden och bemanning till projektplan
* Hanna Fellwing:
	* Skriver på projektplan, baserat på våra anteckningar kring planering
* Lisa Wasslöv:
	* Fokuserar på konkurrentanalys
	* Kravanalys, men denna är beroende av nästa veckomöte (sitemap, definition av funktioner, o.s.v.)
* Victor Dahl:
	* Gantt-schema
	* Kravanalys och övrig ifyllnad av projektplan



## Efter lunch
* Ansvarsområden
* S1 Planering
* Projektplan

  
## Anteckningar
* Vi implementerar dagliga Sprint check-ins på Slack (förutom på dagar som vi har möten)
* Beslut om att använda Excel för att ta fram Gantt-schema (översiktlig), och använda YouTrack för mer specifik data. Excel kan customizas, medan YouTrack är väldigt statiskt och svårförståeligt. 
* Språk:
	* Dokumentation: svenska
	* Kod: engelska
	* Applikationen (för användaren): svenska primärt, med en engelsk översättning i mån av tid
* Skapade [wiki på GitHub](https://github.com/projectpaca/paca/wiki) där användbar information om projektet kommer stå. Än så länge finns förstasidan och en tom sida om applikationens visuella identitet. Vidare finns det en sidebar med länkar till alla docs.
* Vi skjuter upp att bestämma om eventuella mötesroller (t.ex. hattar) tills dessa börjar, men vi tänker preliminärt att det åtminstone krävs en ledare (personen som kallat mötet eller behöver mötet mest) och en sekreterare. 
* Vi har planerat sprint 1:
	* #todo
* Nedanstående anteckningar har bestämts
* Vi har påbörjat de delar av projektplanen som går (utan dependencies). Målet är att fylla på följande delar allteftersom:
	* Projektplan
		2.1 Syfte
		2.2 Ordlista
		2.3 Referenser
	* Översikt av projekt
		3.1 Syfte
		3.2 Omfattning
		3.3 Mål
	* Produkt
		4.1 Produktbeskrivning
		4.2 Målgrupp
	* Process
		5.1 Utvecklingsprocess
		5.2 Bemanning och ansvarsområden
	* Planering
		6.1 Grovplan
		6.2 Gantt-schema
	* Riskanalys
		7.1 Identifierade risker
		7.2 Riskdiagram

### Ansvarsområden

#### Project Management
* Projektledare: Lisa Wasslöv
* Projektdokumentation: Milo Bengtsson
* Fyller på allteftersom


#### Back- och front-end

##### Back-end
Dokumentation som gäller för back-end är: designdokument (systemdiagram, databas, GUI, server, klient, osv.), ER-diagram/relationsmodellen, fildiagram, 

###### Python
* Huvudansvarig: Victor Dahl
* Sidekick: Lisa Wasslöv

###### Databas
* Huvudansvarig: Lisa Wasslöv
* Sidekick: Victor Dahl

##### Front-end
Milo Bengtsson och Hanna Fellwing är ansvariga för detta område. Eftersom front-end blir mer aktuellt senare, skjuter vi upp detaljerad planering av detta. Vissa delar av front-end har många dependencies.

###### HTML (markup)

###### CSS 

###### JavaScript
* Huvudansvarig: Hanna Fellwing
* Sidekick: Milo Bengtsson

###### Grafisk design (illustrationer, wireframes, etc.)


#### Individuella fördjupningar
Vi bestämde oss för att granska det som vi *inte* har primärt hållit på med.

* Dokumentgranskning
	* Viktor Dahl
* Kodgranskning
	* Milo Bengtsson
* Användbarhetstestning och användbarhetsanalys
	* Lisa Wasslöv
	* Hanna Fellwing

**Fler?**
  
### Sprint 1 (V10-12)

### Deadlines och viktiga datum
Handledning varje tisdag kl 10
Projektplan + kravdokument i första färdiga version: 23 mars kl 12:00
Inlämning av materiel till RS-möte: fredag 23 mars 12.00
Retrospect-möte 27 mars

#### Product backlog

* Projektplan ska finnas i en första färdig version.
* Kravdokument ska finnas i en första färdig version. Alla krav är dock kanske inte definierade i detalj ännu. Kravdokumentet kommer sannolikt att förändras men en första uppsättning funktionella och icke-funktionella krav ska finnas.
* Det ska kunna genomföras en demo av produkten med fungerande kod. Inga krav behöver vara färdigimplementerade och testade formellt men det ska finnas exekverbar kod eller en statisk webbsida som minst.


### Sprint 2 (V13-15)

#### Deadlines och viktiga datum

* Handledning varje tisdag kl 10
* Deadline för nedanstående mål: 12 april
* Inlämning av materiel till RS-möte: torsdag 12 april 12.00
* Retrospect-möte 17 april (i sprint 3)

  
#### Product backlog 

* En första version av verifiering- och validerings-dokumentet. 
* Ett designdokument i en första version.
* Det ska ha genomförts kravbaserade tester enligt verifiering- och valideringsdokumentet och dessa ska ha dokumenterats i minst en testrapport.
* Minst en kodgranskning och en dokumentgranskning ska ha genomförts (delar av individuell fördjupning).


### Sprint 3 (V16-18)

#### Deadlines och viktiga datum
Deadline 3 maj 12:00
Affischer 6 maj 23:55
Inlämning av materiel inför RS-möte: torsdag 3 maj 12.00
Retrospect-möte 8 maj 

#### Product backlog
* Det finns en första version av produkten som är en helhet.
* Alla krav prioriterade som ”ska”/”must” (Eklund 2010 kap. 10) är implementerade och testade enligt verifiering- och validerings-dokument.
* En annan grupp ska ha testat projektet och överlämnat en rapport
* Användbarhetsanalyser, användbarhetstester och white-box-testning (delar av individuell fördjupning) ska ha genomförts minst en gång om någon gör dessa.


  

### Sprint 4 (V19-22)

#### Product backlog

#### Deadlines och viktiga datum
*Utställningsdag 24 maj*
Deadline 27 maj

#### Product backlog
* Problem som noterats tidigare ska ha åtgärdats och vissa av de krav som prioriterats som ”bör”/”should” ska ha implementerats.
* Regressionstester + ny implementation ska ha testats minst en gång
* Minst en andra omgång av granskningar och tester som faller under individuell fördjupning. För analyser så ska en kompletterande rapport ha gjort som adresserar hur problem som pekats ut i den första analysen åtgärdats.