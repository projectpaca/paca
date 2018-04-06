# Självgranskning Kravdokument (6/4 -18)

* Separera MoSCoW från krav-ID, eftersom förändringar i prioritering kräver omformulering och att man ändrar ID:t där man hänvisat till det


## Funktionella krav
* För att öka läsbarheten av kraven, kanske implementera en mer semantisk förkortning i början. <id> <kravnamn> <prioritering>
	* INL.F.AK-1 Användaren ska kunna logga in på webbapplikationen | Must
	* PRF.F.AK-2
	* KAL.F.AK-3
* Kolla igenom alla användarkrav för att se till att de alla är formulerade ur *användarens* perspektiv. T.ex. bör det inte stå att användaren ska kunna "logga in på hemsidan i ett formulär med användarnamn och lösenord", utan snarare "Användaren ska kunna logga in på webbapplikationen". Det är i *systemkraven* som vi talar om:
		* Användarens identifieras med e-postadress
		* Användaren ska kunna ange telefonnummer (som kopplas till AK kring kontaktuppgifter och SMS-aviseringar)
* Systemkraven *måste* vara testbara!

## Kvalitativa krav
* **Begränsningar:** Kompabilitet med en eller flera plattformar (kräver att vi definierar vilken version vi använder av t.ex. samtliga programspråk)
* Tillgänglighet
* Tooltips och andra hjälpmedel för att underlätta nya användare och de med funktionsvariation
* "Lätt att förstå" måste definieras så att det blir testbart, t.ex. genom att be testpersoner att poängsätta upplevelsen och ha kravet att 70% ska poängsätta högre än 80% (eller något).
