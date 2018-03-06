# Kravdokument

## METADATA
På varje sida (förutom första) ska följande information inkluderas:
* Sidhuvud
	* Vänster
		* Kravdokument
		* Paca
	* Höger
		* Version nr
		* Grupp 5
* Sidfot
	* Sidnummer (centrerat)
	
## TITELSIDA

# Paca
### Grupp 5

# Kravdokument
## V. XX
### dd/mm -18

___
	

## DOKUMENTHISTORIK

| Datum     | Version | Beskrivning             | Författare     |
|:---------:|:-------:| ----------------------- | -------------- |
| dd/mm -18 | XX      |                         | xxxxxxxxxxxxxx |

```
Fler rader läggs till efterhand som det behövs. Utifrån beskrivningen ska det gå att förstå vad personen gjorde för typ av ändring. Så bara en text som säger ”ändring” räcker inte. Texten behöver exempelvis säga ”Lagt till beskrivning av risk Sjukdom” eller ”Förtydligat beskrivning av produktbeskrivningen.”```  

```
Det kan finnas flera författare. Endast de som faktiskt är aktiva med att skriva texten listas som författare. Om man är två som sitter och jobbar tillsammans och en skriver men man hela tiden aktivt diskuterar det som skrivs så kan bägge personerna stå som författare. Om man har ett möte i hela gruppen där man diskuterar saker, en person tar anteckningar och skriver sedan rent detta i dokumentet så står endast denna person som författare.
```

___

## INNEHÅLLSFÖRTECKNING

[[_TOC_]]

`TOC-statement fungerar i GitHub Wiki, men ingen annanstans`

1. Dokumenthistorik
2. Kravdokument
	2.1 Syfte
	2.2 Ordlista
	2.3 Referenser
3. Produktbeskrivning
	3.1 Målgrupp
	3.2 Intressenter
4. Funktionella krav
	4.1 [Kategori 1]
	4.2 [Kategori 2]
5. Kvalitativa krav
	5.1 [Kategori 1]
	5.2 [Kategori 2]
	
___

### Syfte
```
Text som beskriver syftet med dokumentet (inte projektet). Här beskrivs vad dokumentet innehåller och hur det relaterar till projektet. Det kan också beskrivas vad som inte står här om det förtydligar vad syftet är eller inte är.
```

### Ordlista

| Ord           | Förklaring    | 
| ------------- |---------------|
|               |               |

```
Ta upp förkortningar och uttryck som används i dokumentet och som kanske inte är självklara för en läsare som inte är insatt i projektet. Tänk också på att ta upp begrepp som skulle vara svåra att förstå för en läsare som skulle kunna vara en presumtiv kund eller referensperson i form av exempelvis slutanvändare. Ordlistan ska ordnas i bokstavsordning.
```



### Referenser

```
Använd ett referenssystem och utforma referenser konsekvent enligt detta för alla dokument. Exempel på referenssystem enligt IEEE som är vanligt i tekniska dokument: http://libguides.murdoch.edu.au/c.php?g=246207&p=1640218.
```

___

## Produktbeskrivning
```
Text som utförligt beskriver produkten. Ur denna text ska man kunna förstå de krav som senare finns och sammanhanget för dessa. Produktbeskrivningen ska vara mer utförlig än den produktbeskrivning som finns i projektplanen
```

### Målgrupp
```
Text som utförligt beskriver målgruppen och hur denna påverkar produkten. Texten ska vara mer utförlig än den som finns i projektplanen.
```

### Intressenter
```
Text som beskriver vilka intressenter som finns i projektet. Tänk på projektet som om ni vore ett mindre företag så utlämna inte en presumtiv kund och slutanvändare samt externa intressenter.
```

___

## Funktionella krav
```
Dessa ska struktureras i logiska grupper. Koncepten användarkrav (user requirements) och systemkrav (system requirements) ska användas (Somerville 2010, kap. 4). Text som introducerar de funktionella kraven i stort, hur de prioriteras och identifieras samt hur indelningen i kategorier är gjord.
```
```
De funktionella kraven ska prioriteras med MoSCoW-modellen som grund (Eklund 2010 kap. 10). Ni måste själva beskriva här hur denna modell fungerar och vad de olika prioriteringarna innebär. Det räcker inte att endast ge en referens till modellen i Eklund. Ni kan också behöva göra justeringar utifrån hur modellen presenteras i Eklund för att prioriteringsmodellen ska passa ert projekt.
```
```
Fler kategorier än vad som finns nedan behövs sannolikt. Varje krav ska förses med en unik identifierare. Identifierare på formatet ett bokstavsprefix i formen av en mnemonik och ett löpnummer rekommenderas. Mnemoniks bör spegla kategori eller användarkrav så man enkelt identifierar krav som på något sätt är direkt relaterade.  Krav ska vara testbart formulerade.
```

### `[Kategori 1]` (*mall*)

#### Namn på kravgrupp utifrån användarkrav
Text för övergripande användarkrav

Nedan följer de systemkrav som bryter ner användarkravet ovan.
**[id] Namn på krav [prioritering]**
Kravtext. En eller två meningar.
*Eventuell motivering i kursiv text.*

#### [fler kravgrupper]

### `[Kategori 2]` (*mall*)

#### Kravgrupp med olika krav 
Inkl id, prioritering, kravtext samt ev. motivering

#### Kravgrupp
Inkl id, prioritering, kravtext samt ev. motivering

### osv.

### [Kategori 2]

### [Kategori 3]

___

## Kvalitativa krav
```
Dessa ska grupperas i logiska grupper beroende på typ av krav (fler kategorier än nedan behövs sannolikt). Som minst ska begränsningar som finns dokumenterade. Begränsningar kan exempelvis  vara vilka programspråk som används, vilka operativsystem produkten fungerar med, tekniker som måste användas för att skapa produkten. Varje krav ska förses med en unik identifierare. Identifierare på formatet ett bokstavsprefix i formen av en mnemonik och ett löpnummer rekommenderas. Krav ska vara testbart formulerade. Text som introducerar de kvalitativa/icke-funktionella kraven i stort, hur de identifieras, hur indelningen i kategorier är gjord samt eventuellt hur prioritering är gjord.
```

### `[Kategori 1]` (*mall*)
Text för beskrivning av kategorin.

**[id] Namn på krav [prioritering, ej nödvändigt men kan göras]**
Kravtext. En eller två meningar.
*Eventuell motivering i kursiv text.*

**[id] Namn på krav [prioritering, ej nödvändigt men kan göras]**
Kravtext. En eller två meningar.
*Eventuell motivering i kursiv text.*

### [Kategori 2]

### [Kategori 3]



