# Report

### csv module
Het programma maakt gebruik van de csv module om gegevens te lezen en schrijven naar CSV bestanden. Het formaat van deze bestanden zijn voor alle typen data in `constants.py` aangegeven zodat ze makkelijk hergebruikt kunnen worden. De `csv.writer()` en `csv.DictWriter()` methoden zijn gebruikt om nieuwe rijen data toe te voegen aan de CSV bestanden. De `csv.reader` methode is gebruikt om de CSV bestanden te lezen, om bijvoorbeeld de prijzen of houdbaarheidsdatums te vergelijken. Ook konden met deze methode rijen met data geisoleerd worden als ze aan bepaalde criteria voldeden, om vervolgends aangepast te worden, en daarna weer terug te plaatsen in het CSV bestand. Een voorbeeld hiervan is het optellen van 'count' als er een nieuw product wordt gekocht dat al in `inventory.csv` is.

### uuid module
De uuid module wordt in `buy.py` gebruikt om een uniek id te genereren voor elk nieuw product dat gekocht wordt. Dit id wordt meegenomen naar alle andere CSV bestanden waar het product terecht komt. Deze methode was makkelijker dan om elk product handmatig een id te geven die telkens met +1 toeneemt. Als dit system op grotere schaal gebruikt wordt zou je dan uiteindelijk te grote getallen krijgen voor de id's.

### rich module
De rich module is gebruikt in de `utils` folder om tabellen te genereren in de CLI. De tabellen worden gemaakt op basis van de formaten en CSV bestanden aangegeven in `constants.py`. Deze bestanden worden zodanig aangepast door de `output_table()` functie zodat ze duidelijk in een tabel weergeven worden. Het id van elk product wordt hier ook gebruikt om de stijlen van de rijen van de tabel te bepalen, zodat het beter te lezen is. CSV data is soms lastig om te lezen, de rich module helpt hier dus mee.