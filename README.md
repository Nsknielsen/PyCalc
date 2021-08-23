**PyCalc**

Simpel lommeregner med GUI i Python.

**Anvendte biblioteker**

TKInter, Tkinter.font, re, functools.

**Ideer til renere kode**

- Kog de forskellige calculation functions ned til én for at undgå gentagelse i koden.

- Lav de resterende knapper med et loop ved at have en dictionary med par af knaptekst og funktion som: {"CE" : click_ce}. 
    -> Kræver enten 3 elementer i dictionary (text, function, rowspan) el. en variabel der undervejs i loopet sænkes under et if-tjeks grænse fordi "="-knappen er større i GUI end de andre.

