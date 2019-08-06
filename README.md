# UniAQ GeoAPI
GeoAPI per l'interrogazione di un database PostGIS sui dati agroambientali dell'Università degli Studi dell'Aquila.
Utilizza JWT per l'autenticazione degli utenti attraverso token temporizzato.

## End point delle API

### Rilascio del token di autorizzazione (ritorna un oggetto JSON):
http://hostname/api/login?username=your_username&password=your_password

### Punti di campionamento (ritorna una GeoJSON Feature Collection):
http://hostname/api/punti?token=your_token

### Comuni (ritorna una GeoJSON Feature Collection):
http://hostname/api/comuni?token=your_token&nomeComune=nome_comune
valori ammessi per <i>nomeComune</i>: tutti i Comuni abruzzesi
es: nomeComune = Villamagna

### Dati microbiologici (ritorna un array di oggetti JSON):
http://hostname/api/dati/microbiologici?token=your_token&tipoDati=biodiversita_funzionale
valori ammessi per <i>tipoDati</i>: "biodiversita_funzionale", "biodiversita_genetica"

### Dati vinificazione (ritorna un array di oggetti JSON):
http://hostname/api/dati/vinificazione?token=your_token&tipoDati=microvinificazione
valori ammessi per <i>tipoDati</i>: "microvinificazione", "maturazione_tecnologica"


