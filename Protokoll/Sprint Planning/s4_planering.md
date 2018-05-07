# Sprint 4 Planering
v 19-22 | 26 mars - 13 april
**Utställningsdag:** 24 maj (hela dagen)
**Deadline:** 27 maj 23.55
**RS-möte:** Inget RS-möte

## Närvarande
* Milo Bengtsson (protokoll)
* Hanna Fellwing
* Lisa Wasslöv
* Victor Dahl

## Dagordning
1. Genomför sprint 3 review enl mall
2. Gå igenom detta möte i enlighet med nedanstående punkter
3. Gå igenom resultat av användbarhetsanalys
 
## Product backlog
Till deadline för retrospektmöte 4 ska slutinlämning av projektet ske. Under sprint 4 ska projektet förfinas utifrån den version som fanns efter sprint 3. Som minst så ska följande ha uppnåtts:
	* Problem som noterats tidigare ska ha åtgärdats och vissa av de krav som prioriterats som ”bör”/”should” ska ha implementerats.
	* Regressionstester ska ha genomförts för föraändringar som skett och ny
	implementation ska ha testats minst en gång.
	* Som minst ska en andra omgång av granskningar och tester som faller under
	individuell fördjupning ha genomförts. För analyser så ska en kompletterande rapport ha gjort som adresserar hur problem som pekats ut i den första analysen åtgärdats.
	
## Sprintmål
1. Produkt
2. Testning 1-2 st
3. Analys x1
4. Granskning x2
5. Dokumentation (alla)

## Sprint backlog
En lista över uppgifter som är nödvändiga för att leverera ovannämnda *product backlog items*. Varje uppgift i sprintbackloggen är ofta uppskattningar.

> `d:` = dependency/ies

```
1. Produkt
	1.1 Django
	1.2 Grafisk design (Milo)
	1.3 JavaScript (Hanna)
2. Testning (d: 1)
	2.1 Regressionstester
		Regressionstester ska ha genomförts för förändringar som skett och ny
		implementation ska ha testats minst en gång.
	2.2 Black-box 
		Problem som noterats tidigare ska ha åtgärdats och vissa av de krav som
		prioriterats som ”bör”/”should” ska ha implementerats.
	2.3 Usability testing (d: 1; Lisa)
		Måste inkludera minst tre personer utanför gruppen. 
3. Analys
	3.1 Användbarhetsanalys (d: 1; Hanna)
4. Granskning
	4.1 Dokumentgranskning (Victor)
	4.2 Kodgranskning (Milo)
5. Dokumentation
Alla dokument och filer ska ses över så att de är i enlighet med de krav och riktlinjer som definierats.
	5.1 Användbarhetsanalys (d: 1, 2; Hanna)
		En kompletterande rapport ha gjort som adresserar hur problem som pekats ut i den första analysen åtgärdats.
	5.2 Användbarhetstestning (d: 1, 2; Lisa)
		Kalendern och alla de saker som påpekades på testdagen (CSS).
	5.3 Designdokument (Hanna & Milo)
		MVC-modellen, high-fidelity wireframes, stilguide (typsnitt, etc.).
	5.4 Dokumentgranskningsdokument (Victor)
	5.5 Dokument (d: 5; Victor)
		Se över samtliga dokument för att se att alla ser likadana ut 
	5.6 Kodfiler (d: 1; Milo)
		Se till att alla kodfiler är tillräckligt kommenterade och har visuell consistency vad gäller kommentarer, filnamn och formatering.
	5.7 Kodgranskningsdokument (d: 1; Milo)
	5.8 Projektplan (Lisa)
	5.9 Socialt kontrakt (Milo)
	5.10 Verifierings- och valideringsdokument (d: 2; Lisa)
		I princip färdigt, med undantag för testrapporter.
```

Med andra ord saknas dependencies för 1, 4, 5.3, 5.4, 5.5, 5.7, 5.8	och 5.9. Kodfiler (5.5) kan man säga har 1. Produkt som dependency, men det är inget krav på att kodgranskningen måste ske på den färdiga produkten, så även kodgranskningsmötet kan genomföras rätt tidigt i sprinten.

### Att ta hänsyn till i planeringen
* Victor kommer ha hund!
* Lisa
	- Förberedelse av examensmiddag på kvällen av utställningsdagen
	- Examensmiddag dagen efter utställningsdagen (fredag) 
	- Jobb på sista helgen.
	- Måste utföra usability testing innan V3 torsdag.
* Hanna
	- Förberedelse av examensmiddag på kvällen av utställningsdagen
	- Examensmiddag dagen efter utställningsdagen (fredag)

## Issues
I följande sektion applicerar vi *work breakdown structure* (WBS) för att dela upp sprint backloggen till mindre och fler issues. Detta för att underlätta översikt och uppskattning av tidsåtgång. 

Utgå från 

```
1. Produkt
	1.1 /dashboard
	1.2 /admin
	1.3 /userauth
	1.4 /fullcalendar
	1.5 /account
	1.6 /news
	1.2 CSS (Milo)
	1.3 JavaScript (Hanna)
2. Testning
	2.1 White-box
	2.2 Black-box 
	2.3 Usability testing (Lisa)
3. Analys
	3.1 Användbarhetsanalys (Hanna)
4. Granskning
	4.1 Dokumentgranskning (Victor) 2hx2 + 1h
	4.2 Kodgranskning (Milo) 2hx2 + 2h
5. Dokumentation
	5.1 Användbarhetsanalys (Hanna) 
	5.2 Användbarhetstestning (Lisa)
	5.3 Designdokument (Hanna & Milo) 
	5.4 Dokumentgranskningsdokument (Victor)
	5.5 Dokument (Victor)
	5.6 Kodfiler (Milo) 2h
	5.7 Kodgranskningsdokument (Milo) 2h
	5.8 Projektplan 
	5.9 Socialt kontrakt (Milo) 30m
	5.10 Verifierings- och valideringsdokument (Lisa)
```

	
## Schemalagda aktiviteter

### V1
Victor, Hanna: /fullcalendar
Övriga: dokumentation
* Mån: Sprint Review, Sprint Planning
* Tis: RS3 (10-12)
* Ons: Drop-in Dokumentation (Lisa & Hanna)
* Tor: 
* Fre:

**Preliminärt antal timmar:** 

### V2
Lisa: /accounts
* Mån: Dokumentgranskning och kodgranskning (11h)
* Tis: Handledning (10-10.30)
* Ons: Drop-in Dokumentation & Webb (13-15)
* Tor: Drop-in Webb & Dokumentation (10-12)
* Fre: 

**Preliminärt antal timmar:** 

### V3
* Mån:
* Tis: Handledning (10-10.30)
* Ons: Drop-in Webb & Dokumentation (13-15)
* Tor: UTSTÄLLNINGSDAG
* Fre: Drop-in Webb & Dokumentation (10-12)
* Lör: Slutspurt hemma hos Victor (fr.o.m. 17)
* Sön: Slutinlämning 23:55


**Preliminärt antal timmar:** 

### V4
Sprinten sträcker sig egentligen en vecka till, men det är bara för RS4.


---

## To do från användbarhetsanalysen
* När användaren är inne på någon sida, ska den aktiva sidan markeras i sidomenyn
* Ikonen "i" är tvetydlig. "i" står för "information".
* Färgvariation i kalender – vad baserar vi färgsättning 
* Färg + mönster för att differentiera mellan typer av pass
* Länkar bör stylas
* "Nyheter och notiser"
* 404 Error: "Oh, no! There is a probllama"
* Kompetenser vs Meritet vs Kompetenser och meriter
* Ändra i profil.png: "Kompetenser" -> "Avdelningar" i listan
* Skjuter upp diskussion om Kompetenser vs Avdelning till ett senare skede, eftersom det inte är en prioritering. 