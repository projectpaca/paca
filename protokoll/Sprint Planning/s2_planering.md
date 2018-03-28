# Sprint 2 Planering
v 13-15 | 26 mars - 13 april
**Deadline:** 12 april 12.00
**RS-möte:** 17 april 

## Närvarande
* Milo Bengtsson
* Hanna Fellwing
* Lisa Wasslöv
* Victor Dahl

## Dagordning
1. Genomför sprint 1 review enl mall (/protokoll/Sprint Review/s1_review)
2. Gå igenom detta möte i enlighet med nedanstående punkter

## Anteckningar
* Ramverk
	* Django (Python)
	* Eventuellt Bootstrap. Milo känner att det är bättre att göra det från grunden, för att dels lära sig mer men även för att säkerställa en användbar och tillgänglig kod. 
	* JS-bibliotek, såsom React, jQuery. Hanna går på drop in-webb.

## Viktiga datum och deadlines
* 4 april | Handledning (OBS! Onsdag)
* 6 april | Självgranskning Designdokument
* 10 april | Handledning (OBS! Tisdag)
* 12 april | Deadline
	* Demo
	* VoV-dokument
	* Designdokument
	* Minst en testrapport
	* Minst en kodgranskning + kodgranskningsdokument
	* Minst en dokumentgranskning + dokumentgranskningsdokument
* 13 april | Självgranskning Testdokument

### V1
* Mån: S2 Planering 4h x 4
* Tis: Planering forts 2h x 4
* Ons: Drop in-hjälp Dokumentation 2h x 1 (Victor) + Drop in-hjälp Webb 2h x 1 (Hanna)
* Tor: 
* Fre:

**Preliminärt antal timmar:** 6h x 4 (exkl ons) + 2h x 2 (Victor & Hanna)

### V2
* Mån:
* Tis:
* Ons: Handledning 30 min x 4 + Veckomöte 2,5h x 4 (ev längre, då 13.15-17 är drop in webb och doc)
* Tor: 
* Fre: Självgranskning designdokument (Hanna & Milo) 2h x 2 

**Preliminärt antal timmar:** 3h x 4 + 2h för Hanna & Milo (exkl ev längre ons)

### V3
* Mån:
* Tis: Handledning 30 min x 4 + Veckomöte 2,5h x 4
* Ons: Drop in-hjälp webb 2h x ?
* Tor: INLÄMNING SPRINT 2 kl 12
* Fre: SJälvgranskning Testdokument 2h x ? [S2 eller S3?]

**Preliminärt antal timmar:** 3h x 4 (exkl frågetecken)
 
## Product backlog
Till deadline den 12 april kl 12 ska följande som minst ha uppnåtts:
	1. Det ska finnas en version av produkten med en delmängd av de specificerade kraven ur kravdokumentet implementerade.
	2. Det ska finnas en första version av verifiering- och validerings-dokumentet. 
	3. Det ska finnas ett designdokument i en första version.
	4. Det ska ha genomförts kravbaserade tester enligt verifiering- och validerings- dokumentet och dessa ska ha dokumenterats i minst en testrapport.
		* Beroende av verifierings- och valideringsdokumentet.
	5. Minst en kodgranskning och en dokumentgranskning ska ha genomförts (delar av individuell fördjupning).
		* Kodgranskning beroende av att kodgranskningsdokumentet är färdigt
	

## Sprint backlog
En lista över uppgifter som är nödvändiga för att leverera ovannämnda *product backlog items*. Varje uppgift i sprintbackloggen är ofta uppskattningar.

> `d:` = dependency/ies

1. Demo
2. Dokument
	1. Kodgranskningsdokument 10h
	2. Designdokument 17h
	3. VoV-dokument 11h
	4. Testrapport (d: 4.1) 
	5. Dokumentgranskningsdokument 5h
3. Dokumentgranskning
	1. Minst en kodgranskning (d: 1, 2.1) 8h
	2. Minst en dokumentgranskning (d: 2.5) 8h
4. Tester
	1. Flera kravbaserade tester enligt (d: 3.1) 
	
### Sprintmål

#### Front-end
* Färgtema 
* Design System
* Börja med HTML- och CSS-strukturen 
* Logga

#### Back-end
* Databas
	* Vi har en exempeldatabas som Victor kodade på en timme, vilket vi måste vidareutveckla så långt som vi rimligtvis kan ta det.
	* På databasnivå bör vi registrera när passet börjar och sedan hur lång arbetstiden är. Vi undviker på så sätt krångel vid midnatt och ändring till sommar- eller vintertid. I UI:t syns dock sluttiden (starttiden + varaktighet).
* Python
	* Grundläggande systemstöd för all information beträffande CRUD
	* *Inte* radera viktiga tupler (undantag arbetspass)
	* Funktionaliteten som byggs ska kunna nås via ett webbinterface (och därefter tar front-end-teamet över)
	

## Issues
I följande sektion applicerar vi *work breakdown structure* (WBS) för att dela upp sprint backloggen till mindre och fler issues. Detta för att underlätta översikt och uppskattning av tidsåtgång. 

1. Demo

	1.1 Back-end (d: 2.1) (totalt: ) (Lisa & Victor) 
	
		1.1.1 Python (subtotal: 32h)
		
			1.1.1.1 Kravidentifikation (d: /protokoll/veckomöten/s1_v2_veckomöte.md) 4h x 2
			
			1.1.1.2 CRUD på användare 8h x 2
			
			1.1.1.3 CRUD på pass 4h x 2 
			
		1.1.2 Databas (subtotal: 8h)
		
			1.1.2.1 Vidareutveckling av databas 2h x 4 (Lisa & Victor x 2)
			
	1.2 Front-end (d: 2.2)  (total: 41 h)
	
		1.2.1 Skapa statisk HTML-struktur (inkl placeholders för Python-kod) (Hanna & Milo) 4h x 2
		
		1.2.2 Kravidentifikation CSS (d: kravdokument) (Hanna & Milo) 2h x 2
		
		1.2.3 Kravidentifikation JavaScript (d: kravdokument) (Hanna & Milo) 2h x 2
		
		1.2.4 CSS research (Milo) 5h x 1
		
		1.2.5 JavaScript research (Hanna) 10h x 1
		
		1.2.6 CSS-kodning (Milo) 4h x 1 
		
		1.2.7 JavaScript-kodning (Hanna) 6h x 1 
		
2. Dokument

	2.1 Kodgranskningsdokument (totalt: 12h)
	
		2.1.1 Inledning 1h x 1 (Milo)
		
		2.1.2 Kodgranskning 1h x 1 (Milo)
		
		2.1.3 Riktlinjer för kod 3h x 1 (Milo)
		
			2.1.3.1 Brainstorming inför Python 2h x 2 (Victor & Milo) 
			
		2.1.4 Checklista för granskningsmöte 1h x 1 (Milo)
		
	2.2 Designdokument (totalt: 17h)
	
		2.2.1 Inledning (Syfte, Ordlista, Referenser) 1h x 1 (Milo)
		
		2.2.2 Systemdiagram 
		
			2.2.1.1 Grovjobb (handritade diagram och innehåll) 4h x 1 (Hanna)
			
		2.2.3 Användningsfallsdiagram 3h x 2 (Hanna & Milo)
		
		2.2.4 Användargränssnitt (d: wireframes) 2h x 2 (Hanna & Milo)
		
		2.2.5 ER-diagram/skiss 2h x 2 (Victor/Lisa)
		
		2.2.6 Digitalisering av diagram 3h x 1 (Milo)
		
	2.3 VoV-dokument (totalt: 11h)
	
		2.3.1 Inledning 1h x 1 (Hanna)
		
		2.3.2 Testprocess (d: projektplan, kravdokument, individuella fördjupningar) 2h x 2 (Victor & Lisa)
		
		2.3.3 Testning 2h x 2 (Victor & Lisa)
		
		2.3.4 Testfall 2h x 2 (Victor & Lisa)
		
			2.4.1 Spårningsmatris 
			
	2.5 Dokumentgranskningsdokument (totalt: 5h)
	
		2.5.1 Inledning 1h x 1 (Victor)
		
		2.5.2 Process 2h x 1 (Victor)
		
		2.5.3 Riktlinjer för dokument 1h x 1 (Milo)
		
		2.5.4 Checklista för granskningsmöte 1h x 1 (Victor)
		
3. Dokumentgranskning (totalt: 16h)

	3.1 Minst en kodgranskning (d: 2,5 1, 2.1) 2h x 4 
	
	3.2 Minst en dokumentgranskning (d: 2.5) 2h x 4 
	
4. Tester

	4.1 Flera kravbaserade tester enligt VoV-dokument (d: 3.1) 
	
	4.1 Testrapport (d: 4.1) 
	
