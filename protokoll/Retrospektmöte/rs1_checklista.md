# Checklista för granskning till Retrospektmöte 1
Detta dokument innehåller punkter att utgå ifrån vid granskning av de artefakter som lämnats av andra grupper inför retrospektmöte 1. Dessa punkter utgör ett minimikrav på vad som granskas. Det går utmärkt och granskande grupper uppmuntras att komma med synpunkter utöver det som tas upp nedan.

Den granskande gruppen ska lämna över en version (digital eller på papper) av varje dokument till de grupper man granskat och (en kopia) till handledare. De överlämnade dokumenten ska innehålla kommentarer där man gjort noteringar som innebär synpunkter utifrån punkterna i checklistan eller anda saker som man anser kan noteras. Detta kan handla om otydligt språk, missade saker gentemot mallarna, eller andra notiser som man tror kan hjälpa gruppen att förbättra sin dokumentation.

Även överlämnad kod ska granskas. I detta fall behöver granskande grupp inte lämna över kod-filerna med kommentarer utan kan skriva en kort sammanställning över synpunkter i ett separat dokument. För hänvisningar till exempel på synpunkter i koden så används filnamn och radnummer (även exempelvis funktionsnamn/metodnamn eller liknande kan användas för att identifiera var något finns).

Tänk på att ge konstruktiva synpunkter och feedback (kom ihåg vad vi talade om på föreläsning om gruppdynamik och projekthantering och vad som står i Eklund om feedback).

Vid granskningsmötet ges en kort sammanfattning av den granskande gruppens synpunkter. Varje sak man noterat i den skriftliga överlämningen tas inte upp muntligt. Skulle en mottagande grupp inte förstå någon kommentar så kontaktas den granskande gruppen för ett förtydligande.

Alla dokument och all kod som gruppen producerat ska lämnas över till granskande grupper. Om vissa saker lagts separat i egna dokument utanför de allmänt definierade (projektplan, kravdokument m.fl.) så lämnas också dessa dokument över (exempelvis separata riktlinjer eller protokoll som lagts utan för VoV-dokumentet). Dokumenten behöver inte vara finputsade om man befinner sig mitt i mellan två större versionsändringar. Lämna allt som ett snapshot till granskande grupper.

Ingen grupp behöver sluta arbeta med kod eller dokument i väntan på retrospektmötet. Det går utmärkt att arbeta vidare med både kod och dokument efter att man lämnat över versioner för granskning. Detta kan givetvis innebära att viss feedback blir något mindre aktuell men den feedback som ges är förmodligen ändå relevant på något plan. Den demo som gruppen visar på retrospektmöet måste inte heller vara från samma version av koden som den man lämnade för granskning.

## Checklista RS1

### Dokument generellt
* Finns försättsblad, sidhuvud och dokumenthistorik enligt projektguide och mallar? Observera att alla dokument, även de som gruppen skapat men som inte har direkta mallar, ska ha försättsblad, sidhuvud och dokumenthistorik.
* Innehåller dokument de punkter som finns i mallarna i övrigt?
* Finns det något ord, förkortning eller liknande i något dokument som ni anser borde finnas i en ordlista men som saknas där?
* Är språket i dokument väl formulerat utan stavfel och med korrekt grammatik och hela meningar?
* Är språket formulerat på ett objektivt och neutralt format? (Det vill säga har man undvikit formuleringar som innebär vi och jag.)
* Har alla dokument ett enhetligt utseende som signalerar att de härrör från samma projekt?
* Är dokumenthistoriken så tydlig att man kan följa vem som skrivit vad i ett dokument?

### Kodfiler
Vissa grupper kommer att titta på kodfiler i språk man kanske inte sett innan. Vissa saker skiljer sig åt mellan olika språk så som exempelvis hur man strukturerar kod över olika filer. Dessa saker kanske då är svårare att granska. Många saker är dock gemensamma och kan granskas oavsett bakgrund och vad som granskas.

Lämna gärna en instruktion till granskande grupp för hur de lättast startar en körbar version av er kod.

	* Är kodfiler logiskt strukturerade i form av indelning i kataloger och filer?
	* Används lämpliga filnamn?
	* Använder man lämpliga namn på variabler och funktioner/metoder så att dessa är beskrivande och ökar kodens läsbarhet?
	* Finns det lämpliga kommentarer till koden som förklarar syftet med funktioner/metoder?
	* Är kodens struktur i form av exempelvis indentering, block-indelning och blankrader utförd så att den stöder läsbarheten?
	* Är det möjligt att spåra vem som har skrivit vilken kod (eller i varje fall skrivit den övervägande delen av ett visst stycke kod)?

### Projektplan
* Är syfte, omfattning och mål tydligt formulerade och verkar rimliga? Kan ni förstå vad det är man vill göra i projektet och vad man vill uppnå?
* Har man beskrivit en rimlig utvecklingsprocess? Detta innebär att man inte beskrivit en så stor process att den verkar svår att uppfylla i era begränsade projekt (exempelvis sagt att man ska använda RUP eller XP rakt av) och inte heller att man sagt så lite om processen att det inte går att förstå hur gruppen avser arbeta. Beskrivningen ska vara utförligare och mer detaljerad än de riktlinjer för sprintarna som lagts fram i projektguiden.
* Är där något ansvarsområde som ni anser att gruppen glömt att definiera? Jämför med vad som beskrivs i produktbeskrivning och utvecklingsprocess.
* Är aktiviteter och milstolpar så väl beskrivna att ni förstår vad som avses ska ske under projekttiden och när? Stämmer dessa överens med beskrivning av produkt, process samt syfte och mål så att man kan se hur planeringen hjälper gruppen att nå dessa?
* Har gruppen missat att identifiera någon risk?
* Anser ni att riskbedömningar som gjorts är rimliga?
* Har alla risker en handlingsplan som beskriver hur man agerar om risken inträffar och hur man minskar att detta sker? Anser ni att dessa planer är rimliga eller effektiva?

### Kravdokument
* Förstår ni utifrån produktbeskrivningen vad man avser göra för produkt och hur denna är avsedd att fungera i stort?
* Är målgruppen så väl beskriven att ni anser att man kan dra slutsatser om hur denna påverkar designen av produkten.
* Anser ni att intressentlistan är komplett? Om inte vilka intressenter anser ni att man missat? Har man beskrivit hur olika intressenter påverkar projektet?
* Är kraven (både funktionella och kvalitativa krav) formulerade så att de är testbara?
* Har kraven hamnat i rätt kategori av funktionella och icke-funktionella/kvalitativa krav?
* Har alla krav en unik identifierare?
* Har alla funktionella krav fått en prioritering och förstår ni vad prioriteringen innebär?
* Har funktionella krav delats in i lämpliga kategorier? Förstår ni hur man gjort indelningen?
* Är funktionella krav strukturerade med mer övergripande användarkrav som brutits ner till mer detaljerade systemkrav?
* Är där något funktionellt krav som saknar motivering men som borde kunna förtydligas genom en sådan?
* Har icke-funktionella/kvalitativa krav hamnat i lämplig kategori och finns det en beskrivning av varje kategori?

### Övriga artefakter
För övriga dokument så ges inga mer detaljerade punkter för retrospektmöte 1. Om det finns inlämnade dokument utöver projektplan och kravdokument så granskas dessa utifrån de mallar som finns för dokumenten. Det går också bra att titta på checklistor för RS2 och RS3 för att få stöd för detta.

För dokument utan mallar (exempelvis färdiga checklistor för kodgranskning) så granskas dessa utifrån en allmän förståelse för innehållet.