# UniAQ GeoAPI
GeoAPI per l'interrogazione di un database PostGIS sui dati agroambientali dell'Università degli Studi dell'Aquila.
Utilizza JWT per l'autenticazione degli utenti attraverso token temporizzato.

## End point delle API

### http://hostname/api/login
PARAMETRI: <strong>username</strong>, <strong>password</strong></br>
RITORNA: JSON Object (token)</br>
ESEMPIO: http://hostname/api/login?username=your_username&password=your_password

### http://hostname/api/punti
PARAMETRI: <strong>token</strong></br>
VALORI AMMESSI: tutti i Comuni abruzzesi (es: Villamagna)</br>
RITORNA: GeoJSON Feature Collection</br>
ESEMPIO: http://hostname/api/punti?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCIsImV4cCI6MTU2NTA4Njg2N30.KmsvJwNEevpNnzGMV0nvCMyMUVPwe6Hk7wU4WEKxMR0

### http://hostname/api/comuni
PARAMETRI: <strong>token</strong>, <strong>nomeComune</strong></br>
VALORI AMMESSI: tutti i Comuni abruzzesi (es: Villamagna)</br>
RITORNA: GeoJSON Feature Collection</br>
ESEMPIO: http://hostname/api/comuni?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCIsImV4cCI6MTU2NTA4Njg2N30.KmsvJwNEevpNnzGMV0nvCMyMUVPwe6Hk7wU4WEKxMR0&nomeComune=Villamagna

### Dati microbiologici (ritorna un array di oggetti JSON)
http://hostname/api/dati/microbiologici?token=your_token&tipoDati=biodiversita_funzionale</br>
valori ammessi per <i>tipoDati</i>: <strong>biodiversita_funzionale</strong>, <strong>biodiversita_genetica</strong>

### Dati vinificazione (ritorna un array di oggetti JSON)
http://hostname/api/dati/vinificazione?token=your_token&tipoDati=microvinificazione</br>
valori ammessi per <i>tipoDati</i>: <strong>microvinificazione</strong>, <strong>maturazione_tecnologica</strong>


