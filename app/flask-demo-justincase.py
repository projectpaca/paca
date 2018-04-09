from flask import Flask, request, render_template, url_for

app = Flask(__name__)

try:
    import psycopg2
except:
    #import pip
    pip.main(['install','psycopg2'])
    import psycopg2

source_server = "pgserver.mah.se"
databas = "paca_database"
user = "ah8723"
passw = "m9q6w3ek"
connect = ""


