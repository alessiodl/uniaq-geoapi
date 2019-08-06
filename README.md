# UniAQ GeoAPI
GeoAPI per l'interrogazione di un database PostGIS sui dati agroambientali dell'Università degli Studi dell'Aquila.
Utilizza JWT per l'autenticazione degli utenti attraverso token temporizzato.

<img src="postman_testing.png" alt="postman testing"/>

## End point delle API

### http://hostname/api/login
<ul>
    <li>PARAMETRI: <strong>username</strong>, <strong>password</strong></li>
    <li>RITORNA: JSON Object (token)</li>
    <li>ESEMPIO: http://hostname/api/login?username=your_username&password=your_password</li>
</ul>

### http://hostname/api/punti
<ul>
    <li>PARAMETRI: <strong>token</strong></li>
    <li>VALORI AMMESSI: tutti i Comuni abruzzesi (es: Villamagna)</li>
    <li>RITORNA: GeoJSON Feature Collection</li>
    <li>ESEMPIO: http://hostname/api/punti?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9</li>
</ul>

### http://hostname/api/comuni
<ul>
    <li>PARAMETRI: <strong>token</strong>, <strong>nomeComune</strong></li>
    <li>VALORI AMMESSI: tutti i Comuni abruzzesi (es: Villamagna)</li>
    <li>RITORNA: GeoJSON Feature Collection</li>
    <li>ESEMPIO: http://hostname/api/comuni?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9&nomeComune=Villamagna</li>
</ul>

### http://hostname/api/dati/microbiologici
<ul>
    <li>PARAMETRI: <strong>token</strong>, <strong>tipoDati</strong></li>
    <li>VALORI AMMESSI: <i>biodiversita_funzionale</i>, <i>biodiversita_genetica</i></li>
    <li>RITORNA: JSON Object Array</li>
    <li>ESEMPIO: http://hostname/api/dati/microbiologici?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9&tipoDati=biodiversita_funzionale</li>
</ul>

### http://hostname/api/dati/vinificazione
<ul>
    <li>PARAMETRI: <strong>token</strong>, <strong>tipoDati</strong></li>
    <li>VALORI AMMESSI: <i>microvinificazione</i>, <i>maturazione_tecnologica</i></li>
    <li>RITORNA: JSON Object Array</li>
    <li>ESEMPIO: http://hostname/api/dati/vinificazione?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9&tipoDati=microvinificazione</li>
</ul>


