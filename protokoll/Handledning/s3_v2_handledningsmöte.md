DA336A VT18
Grupp 5

# Handledningsmöte (24/4 -18)

## Närvarande
* Milo Bengtsson (protokoll)
* Hanna Fellwing
* Lisa Wasslöv
* Victor Dahl


Förra veckan präglades till en början av rätt stor förvirring kring Django och hur vi skulle planera denna sprint. Genom att ta det gemensamma beslutet att *samtliga* gruppmedlemmar ska sätta sig in i Django, har vi observerat en rad positiva effekter:
* Vi tipsar varandra om lärorika tutorials och guider på webben.
* Vi har fått bättre grepp om vad vi behöver (och *inte* behöver) göra samt hur vi gör det.
* Det har uppmanat till parprogrammering, vilket har gjort att problem och hinder i koden har blivit mer hanterbara samt lättare och snabbare att lösa.

Efter ett möte igår (23/4) bestämde sig gruppen för att dela upp webbapplikationen i tydligt definierade appar och hädanefter hänvisa till produkten som en webbplats/site. Detta eftersom ramverket Django, som vårt back-end bygger på, är uppbyggt av flera appar. Dessa appar är mappar inom projektkatalogen, som var och en innehåller egna konfigureringsfiler skrivna i Python. Detta är för att underlätta utveckling av en app i taget, eller flera appar parallellt, eftersom det gör att alla gruppens medlemmar kan arbeta med en app utan att våra commits riskerar att kollidera. Med andra ord kan var och en arbeta lokalt och därefter committa till GitHub tämligen ostört och oproblematiskt. Vem som ansvarar för varje app anges i den README-fil som ska finnas i varje app, som utöver ägarskap även ska ange annan relevant information (t.ex arbetsanteckningar).

Planeringen i övrigt har varit väsentligen mindre specifik än förra sprinten. Det är förståeligt på ett sätt, eftersom vi inte på samma sätt har tydliga leverabler. Med det menar vi att vi inte ska bli färdiga med att skriva fyra dokument, som var och en har obligatoriska delar. Istället handlar det om mycket större mål (samtliga *Must*-krav ska implementeras), vilka kan vara väldigt svåra att estimera. Därför har ingen riktig planering gjorts i YouTrack, vilket vi dock borde göra. Vi har dock definierat de leverabler som ska uppfyllas till deadlinen, samt påbörjat att bryta ner dem enligt WBS:

1. Demo med samtliga Must-krav implementerade
    1. Back-end
        1. Django Research
        2. Diskutera ordningen som kraven kommer hanteras
        3. Informera testare när krav är redo för test
    2. Front-end
        1. CSS Research
        2. JavaScript Research
        3. Django templating (HTML)
2. Testning
    1. Samtliga Must-krav testade och dokumenterade enligt VoV-dokumentet
    2. Minst en användbarhetsanalys 
    3. Minst ett användbarhetstest (Hanna & Lisa)
    4. Minst en white-box-testning
    5. Testning som utförts av en annan grupp, som ska ha lämnat testrapport på testerna som kördes (efter deadline)
3. Affisch
4. Dokumentation 
    1. VoV-dokument
    2. Designdokument
    3. Projektplan

___


## Veckan som gått
Först presenteras varje gruppmedlems loggade tid, samt de issues som loggats, under den föregående veckan. Därefter sammanfattas det genom att jämföra personens loggade tid med förväntad tid (18h).

### Milo Bengtsson (26h40m)
* PACA-82 Demo 2 (6h)
* PACA-88 Django (9h)
* PACA-53 HTML - Skapa struktur (2h40m)
* PACA-86 Omarbetning av dokument efter RS2 (1h30m)
* PACA-87 Planeringsmöte 19/4 (30m)
* PACA-81 RS – Granskning av andra gruppers dokumentation inför RS2 (2h)
* PACA-84 Retrospektmöte 2 17/4 (2h30m)
* PACA-83 Sprint planning 3 (2h30m)

Milo Bengtsson har arbetat 148 % av förväntad tid under S3 V1.

### Victor Dahl (24h)
* PACA-58 CRUD Python (3h30m)
* PACA-88 Django (15h45m)
* PACA-87 Planeringsmöte 19/4 (45m)
* PACA-84 Retrospektmöte 2 17/4 (2h30m)
* PACA-83 Sprint planning 3 (1h30m)

Victor Dahl har arbetat 133% av förväntad tid under S3 V1.

### Hanna Fellwing (18h15m)
* PACA-31 Back-end research (2h)
* PACA-85 DOC - Användbarhetsanalys (1h)
* PACA-40 DOC - Designdokument/Grovjobb diagram (1h)
* PACA-57 JavaScript (7h)
* PACA-86 Omarbetning av dokument efter RS2 (1h30m)
* PACA-87 Planeringsmöte 19/4 (45m)
* PACA-84 Retrospektmöte 2 17/4 (2h30m)
* PACA-83 Sprint planning 3 (2h30m)

Hanna Fellwing har arbetat 101% av förväntad tid under S3 V1.

### Lisa Wasslöv (19h)
* PACA-31 Back-end research (11h15m)
* PACA-87 Planeringsmöte 19/4 (45m)
* PACA-81 RS – Granskning av andra gruppers dokumentation inför RS2 (2h)
* PACA-84 Retrospektmöte 2 17/4 (2h30m)
* PACA-83 Sprint planning 3 (2h30m)

Lisa Wasslöv har arbetat 106% av förväntad tid under S3 V1. 


## Hela sprinten
Antal rapporterade timmar under sprinten än så länge (i procent av 55h)
* Milo Bengtsson: 26h40m (48 %)
* Victor Dahl: 24h (44 %)
* Hanna Fellwing: 18h15m (33 %)
* Lisa Wasslöv: 19h (35 %)

Gruppens totalt loggade timmar under S3: 87h55m (40 %) av 220h



## Planerat arbete kommande vecka
Victor kommer åka på semester på onsdag, så det är crunching time tills dess!

### Milo Bengtsson
Fokus på webbplatsen

### Victor Dahl
Fokus på webbplatsen

### Hanna Fellwing
Fokus på testning

### Lisa Wasslöv
Fokus på testning


## Övriga punkter

### Dokumentation
* Mycket dokumentation gör att vi går mer in i vattenfallsmodellen, men det är inget vi riktigt kan hjälpa eftersom dokumentation är obligatoriskt. 
* Vi känner dock inte att vi har haft användning för all dokumentation.
* Dokumentationen hade kunnat vara mycket kortare
    - Dokumentgranskningsdokumentet hade kunnat innehålla två bilagor: dokumentmall (som implementerar alla riktlinjer) och checklista för granskning. Texten i själva dokumentet hade kunnat vara väsentligen kortare, och bygga på mer referenser än att skriva egen text.
    - Kodgranskningsdokumentet hade kunnat vara en sida av referenser bara, istället för flera sidor av "Rätt vs Fel sätt att skriva kod".

### Demo
* Vi insåg vår tidsbrist i back-end, och svarade genom att omfördela gruppens resurser så att alla mer eller mindre jobbade med Django. 
