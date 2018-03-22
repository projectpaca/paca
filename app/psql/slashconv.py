print("\n___FRONTSLASH TO BACKSLASH___")
print("\nDetta program tar en sökväg och vänder '\\' till '/' så att sökvägen går att använda i PSQL")
print("\nLÖSER PROBLEMET 'PERMISSION DENIED' I WINDOWS när man försöker öppna en SQL-fil.\n\n")

while True:
        link = input("Länk att konvertera:")
        new = ""
        for char in link:
                if char == "\\":
                        new+=("/")
                else:
                        new+=(char)
        print("\n\nDIN LÄNK med VÄNDA SLASHES:\n",new,"\n")
