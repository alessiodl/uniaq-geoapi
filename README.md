# UniAQ GeoAPI
GeoAPI per l'interrogazione di un database PostGIS sui dati agroambientali dell'Università degli Studi dell'Aquila.
Utilizza JWT per l'autenticazione degli utenti attraverso token temporizzato.

## End point delle API

### http://hostname/api/login
<ul>
    <li>PARAMETRI: <strong>username</strong>, <strong>password</strong></li>
    <li>RITORNA: JSON Object (token)</li>
    <li>ESEMPIO: http://hostname/api/login?username=your_username&password=your_password</li>
</ul>

### http://hostname/api/punti
PARAMETRI: <strong>token</strong></br>
VALORI AMMESSI: tutti i Comuni abruzzesi (es: Villamagna)</br>
RITORNA: GeoJSON Feature Collection</br>
ESEMPIO: http://hostname/api/punti?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9

### http://hostname/api/comuni
PARAMETRI: <strong>token</strong>, <strong>nomeComune</strong></br>
VALORI AMMESSI: tutti i Comuni abruzzesi (es: Villamagna)</br>
RITORNA: GeoJSON Feature Collection</br>
ESEMPIO: http://hostname/api/comuni?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9&nomeComune=Villamagna

### http://hostname/api/dati/microbiologici
PARAMETRI: <strong>token</strong>, <strong>tipoDati</strong></br>
VALORI AMMESSI: <i>biodiversita_funzionale</i>, <i>biodiversita_genetica</i>
RITORNA: JSON Object Array</br>
ESEMPIO: http://hostname/api/dati/microbiologici?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9&tipoDati=biodiversita_funzionale

### http://hostname/api/dati/vinificazione
PARAMETRI: <strong>token</strong>, <strong>tipoDati</strong></br>
VALORI AMMESSI: <i>microvinificazione</i>, <i>maturazione_tecnologica</i>
RITORNA: JSON Object Array</br>
ESEMPIO: http://hostname/api/dati/vinificazione?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9&tipoDati=microvinificazione


