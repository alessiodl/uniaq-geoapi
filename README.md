# UniAQ GeoAPI
GeoAPI per l'interrogazione di un database PostGIS sui dati agroambientali dell'Università degli Studi dell'Aquila.
Utilizza JWT per l'autenticazione degli utenti attraverso token temporizzato.

## End point delle API

### Rilascio del token di autorizzazione:
http://hostname/api/login
#### Parametri attesi: username, password
#### Ritorna: oggetto JSON
esempio: <i>http://hostname/api/login?username=your_username&password=your_password</i>

### Punti di campionamento:
http://hostname/api/punti?token=your_token

### Comuni:
http://hostname/api/comuni?token=your_token&nome_comune

es: "Villamagna"

### Dati microbiologici:
http://hostname/api/dati/microbiologici?token=your_token&indici=biodiversita_funzionale

valori ammessi per <i>indici</i>: "biodiversita_funzionale", "biodiversita_genetica"

### Dati vinificazione:
http://hostname/api/dati/vinificazione?token=your_token&parametri=microvinificazione

valori ammessi per <i>parametri</i>: "microvinificazione", "maturazione_tecnologica"


