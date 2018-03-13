# S1: Veckomöte 2

## Deltagare
* Milo Bengtsson (protokoll)
* Victor Dahl
* Hanna Fellwing
* Lisa Wasslöv

## Agenda
* Funktionalitet & sitemap
* Demo scope

## Funktionalitet

### Måste
* Inloggning (A/S)
* Se profil (A/S)
* CRUD användare (S)
* Se/boka pass (A)
* CRUD pass (S)

### Bör
* Godkänna pass (S)
* CRUD avdelning (S)
* Tillgänglighet (A/S)
* Byta pass (A/S)
* Exportfunktioner (A/S)
	* Statiska filer
	* Prenumerationer
	* iCal, XLS osv.
* E-postaviseringar (A)

### Vill
* Kompetenser 
* Exportfunktion (A/S)
	* Grafisk view (veckoview)
* SMS-notiser (A)
* Skräddarsy export (t.ex. aviseringsinställningar) (A/S)


## Anteckningar

### Dashboard
* En widget med de senaste nyheterna, och med möjlighet att ha en sticky post.

### Profil
* Profilbild
	* Default: en av flera Al-placeholders
	* Funktion: edit
	* Cirkulär eller kvadratisk bild?
* SMS- och e-post-avisering
	* Bekräftelsemeddelande 
	* Övriga notiser
* Så lite som mycket below the fold, utan istället flikar (ovanför, vilket ser bra ut eftersom huvudnavigeringen är en sidomeny)

### Rangordning av anställda vid schemabokning (supervisor)
Vi vill dels ha en filterfunktion (t.ex. sök, vissa arbetstitlar) men även att man kan ordna efter anställningstid, namn, etc.

### Kunna se andra anställdas pass
Eventuellt att supervisor kan bestämma huruvida anställda ska kunna se andras pass, då det bara rör sig om ett enklare True/False i programmering. 

![exempel](https://dribbble.com/shots/3786988-Tasks-Edit-Meeting)

### Arbetskategorier och kompetens
* Skapa passkategorier, och gör anställda eligable för att jobba i dessa passkategorier

### Risker
* Markerar man sig som tillgänglig, avmarkerar man sig ju närmre passet man kommer (om man inte blivit bokad) eftersom andra planer ofta har kommit upp då. Ligger man i soffan på en fredagskväll och får reda på att man blivit bokad på lördag morgon... 

### Dummy Company
* Dagligvaruhandel/livsmedelsbutik
* Lima Livs
* Totalt 30 anställda 
	* 10 heltid med scheman
		* Heltidsanställda har ingen inloggning framtill vi kommer på hur vi bytar pass
	* 10 deltid med scheman 
	* 10 vid behov utan scheman
* Överlappande pass
* Peak-timmar som passen behöver 

### Passbokning
* Om en anställd har 8 h arbete i veckan, och chefen endast har bokat in 6 h – måste den anställda godkänna detta?

### Passbyte
* Vid sjukanmälning
* Vid önskning om passbyte
	* Markera som "vill byta", vilket dyker upp på dashboarden
	* Chefen kanske då ser det, och väljer att boka av den anställda pga att det finns tillräckligt med anställda så att de klarar sig
	
### Tillgänglighet
= jag *vill* jobba 

### Kommentarer 
Det ska finnas kommentarsfält i allt som en anställd kan boka (pass och tillgänglighet).

### Kalender
* Sidovy till höger där information om det pass som användaren klickar på visas:
	* Vad?
	* Start (hh:mm)
	* Slut (hh:mm(
	* Rast (min) 
	* Info
* Bokade vs obokade pass
	* Bokade pass har viss färg/opacitet, medan obokade pass skiljer sig från dessa markant.
	* Den översta raden i kalendern innehåller obokade pass, medan nedanstående rader är anställda med sina bokade pass
* Användare ser BLANK (obokade pass) och en rad under med sina egna pass/tillgänglighet
* Supervisor ser BLANK, och alla users under.
* Informationen om passet bör vara högst kortfattat i själva pass-boxen i kalendern, så att användare klarar av 
* Osäkerhet kring om det ska vara en kalender för A/S, eller om det ska vara två olika.

