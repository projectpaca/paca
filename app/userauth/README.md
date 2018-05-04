# README: /userauth

## Ownership
Milo Bengtsson is responsible for /userauth.


## Status
* 25 april: first commit has been pushed to a branch (*userauth1*) in our GitHub repository.


## Purpose
The aim of this application is to:
* Extend the native user model in Django and specifying how our custom user model differs from it.
* Create new users
* Remove users
* Edit users
* User authentication
    - Log in
    - Log out
    - Change password (authenticated users)
    - Reset password (unauthenticated users)
* Specify which of these things are done in the admin page, in the authenticated website, and on the unauthenticated website.


## To Do
[] EmergencyContacts as M:1, and have `employee`(FK empid), `name`, `relationship`, `phone`, `phone_type`. We do NOT implement the prio column.
[] `language` has to be broken out to an individual table