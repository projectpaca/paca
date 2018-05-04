# Gruppmöte 27/4

## Närvarande
* Milo Bengtsson
* Lisa Wasslöv


## To Do
* Spika typsnittet för logga


## Been Done
* YouTrack
    - Stängde "PACA-31 Back-end research" eftersom vi flyttade över till “PACA-93 KOD – Django: Research”. 
    - Stängde "PACA-53 HTML – Skapa struktur" för att vi nu går in på mer specifika grejer. Strukturen är ju färdig!
* Fixar heading-hierarkin så att det viktigaste på varje sida är H1 (dvs titel på sidan – inte loggan)
* Beslutade om att omprioriterar implementationen av prioritering i **emergency_contacts** till ett *Could*-krav (hela funktionen är ett *Should*-krav; den ligger kvar, men själva prion tas bort så länge)

## Innehåll i /accounts

### Struktur
För att underlätta arbetet med alla templates, följer här en nedskalad outline av innehållet i en profil-template.

```html
{% extends "base.html" %}

{% block content %}
    <nav class="container-nav">
        ...
    </nav> <!-- /.container-nav -->

    <header class="container-header">
        <div class="container-header-title">
            ...
        </div>
    </header> <!-- /.container-header --> 

    <section id="profile-section" class="container-section">
        ...
    </section>
{% endblock %}
```

### Innehåll
Nedan följer en outline av vad varje profilsida ska innehålla.

#### Profile (sammanfattande sidan)

* [X] Nav
* [ ] Header
    - [X] Div med namn och anställningstyp
    - [ ] Bild + två knappar ("ändra" och "ta bort)
<<<<<<< HEAD
* [ ] Section
    - [X] Telefonnummer
    - [X] E-postadress
    - [ ] Anställnings-ID
=======
* [] Section
    - [X] Telefonnummer
    - [X] E-postadress
    - [] Anställnings-ID
>>>>>>> userauth2
    - [X] Anställningsform
    - [X] Kompetenser
    - [X] Närmaste anhöriga

#### Anställning

#### Kompetenser
* [X] Nav
<<<<<<< HEAD
* [ ] Header
* [ ] Section
    - [ ] Avdelning
    - [ ] Språk
    - [ ] Certifikat
    - [ ] Annan relevant utbildning
    - [ ] Körkort

#### Kontakt
* [X] Nav
* [ ] Header
* [ ] Section
    - [ ] ...
=======
* [] Header
* [] Section
    - [] Avdelning
    - [] Språk
    - [] Certifikat
    - [] Annan relevant utbildning
    - [] Körkort

#### Kontakt
* [X] Nav
* [] Header
* [] Section
    - []
>>>>>>> userauth2

## Models
De databastabeller som vi behöver är:
* CustomUser
    - Standard (default): first_name, last_name, username, email, password
    - Identifiers
    pnr
    - Employment
        + empid
        + emp_type
```python
EMP_TYPE_CHOICES = (
    ('full time', 'heltid'),
    ('part time', 'deltid'),
    ('hourly paid', 'timanställning')
    ('probationary', 'provanställning')
)
```
*
    - Contact
        + phone
        + street
        + postcode
        + city
* EmergencyContacts
    - Vi skiter i prioriteringen just nu i alla fall.
    - M:1 med attributen:
        + empid_f
        + name
        + relationship
        + phone
* UserLanguages
    - M:1 med attributen:
        + empid_f
        + language


