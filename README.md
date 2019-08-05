# UniAQ GeoAPI
GeoAPI per l'interrogazione di un database PostGIS sui dati agroambientali dell'Università degli Studi dell'Aquila.
Utilizza JWT per l'autenticazione degli utenti attraverso token temporizzato.

## End point

### Rilascio del token di autorizzazione:
http://hostname/api/login?username=your_username&password=your_password

### Punti di campionamento:
http://hostname/api/punti?token=your_token

### Comuni:
http://hostname/api/comuni?token=nome_comune

es: "Villamagna"


