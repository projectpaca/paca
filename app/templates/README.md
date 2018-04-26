# README: /templates

## Ownership
The group member in charge of the app which the template relates to is ultimately the owner; however, Milo Bengtsson is responsible for the overall structure of the template code.


## Status


## Purpose
This folder contains the extendable base layout files, base.html and unauth_base.html, as well as those templates that extend them. The root level of this folder is supposed to only contain the two former files, along with this document, and several folders containing each app's template.

## To Do
[] Try to rename /registration to /userauth. This doesn't work by just renaming it though, as Django automatically looks for templates in /templates/registration (i.e. by default). This has to be overwritten. 
[] Move dashboard.html to its own folder (/dashboard). I tried for a minute, and it didn't work (you have to configure /app so that it looks in /templates and then in /dashboard).