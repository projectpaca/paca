# Självgranskning Designdokument (6/4 -18)

## Systemdiagram
* Block och streck som ibland sammankopplas med pilar...
* Illustrerar arkitekturen på systemet
* IA-studenter skapar i regel klient-server-diagram
* Bör kompletteras med en mer detaljerad vy:
	* Klassdiagram enligt UML
	* Komponentdiagram
		1 del som handlar om GUI
		2 som handlar om logik
		3 blabla och alla är kopplade på något vis blabal

## Användningsfallsdiagram
* UML-standard ska följas
* Streckgubbar
* T.ex.
	* En användare ska kunna (streckgubbe)
		* Logga in (en användningsfallsbeskrivning)
		* Ta upp vapen (-"-)
		* xxxxx (-"-)

### Vanliga fel i användningsfallsdiagram
* Menyträd/flödesschema
	* Person -> loggar in -> väljer svårighet -> 
* Preconditions ska *inte* vara med i diagrammet, utan anges i användningsfallsbeskrivningar. Extend och include går bra att ha med dock!

## Användargränssnitt
* Helt okej att ha handskissade ritningar om tiden inte räcker till, eftersom det är just en första skiss av användargränssnittet. 
	* Dessa blir då **version 1** av skisserna till gränssnittet
	* I den senare versionen skall de dock digitaliseras till riktiga wireframes
* Var noga med att skriv ingående beskrivning om varje skiss/wireframe; utgå inte från att läsaren har någon blekaste aning om vad hen ser
* Alla vyer är inte nödvändiga, utan ge relevanta exempel
* **Om målet är att webbapplikationen ska vara responsiv, ha en bild av hur den ser ut i en annan enhet än en dator**

## Diagram/skiss
* Våra handledare ska ge exempel på vilken typ av diagram det gäller
* Databaser kräver ER-diagram