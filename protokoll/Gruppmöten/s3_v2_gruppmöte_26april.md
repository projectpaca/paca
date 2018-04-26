# Gruppmöte 26/4

## Närvarande
* Milo Bengtsson (protokoll)
* Hanna Fellwing
* Lisa Wasslöv

## Anteckningar

### Ansvarsområden
d = dependency

* /accounts
    - Prio: Hög
    - Ansvar: Lisa Wasslöv
    - d: /userauth
    - Innehåll
        + Profilsidan
        + Avdelningssidan
* /app
    - Ansvar: alla
* /dashboard
    - Prio: Medel
* /fullcalendar
    - Prio: Hög
    - Ansvar: 
* /news
    - Prio: Låg
* /sent_emails
    - Ingen prio (statisk)
    - Mailen som egentligen ska skickas till användaren i "Glömt lösenord" sparas som en fil i denna mapp.
* /static
    - Ingen prio (uppdateras allteftersom)
    - Ansvar: Milo
* /templates
    - Ingen prio (se respektive app)
    - Huvudansvar: Milo
    - Alla kommer att skapa templates, men Milo har huvudansvar för strukturen (i synnerhet på base.html och unauth_base.html)
* /userauth
    - Prio: Hög
    - Ansvar: Milo
    - Innehåll
        + users
        + avdelningar (groups)
        + user authentication
        + log in
        + log out
        + change password
        + reset password

### Avdelningar
* Avdelningar kommer vi implementera som det inbyggda fältet `groups` i user model.
* `django.contrib.auth.models.Group` är ett generellt sätt att kategorisera användare så att man kan tillämpa permissions (eller andra labels) till dessa användare. 
* En användare i en grupp får automatiskt de rättigheterna som definierats för den gruppen.
* Rättigheterna definieras genom att skicka över 


