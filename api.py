import os
from flask import Flask, jsonify, request, make_response
import json
import jwt
import datetime
from functools import wraps
import geopandas as gpd
import pandas as pd
from osgeo import gdal
import psycopg2
import fiona

# APP
app = Flask(__name__)
app.config.from_pyfile(os.path.join('config', 'api.conf'), silent=False)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message' : 'Nessun token fornito!'}), 403
        else:
            try:
                data = jwt.decode(token, app.config.get('SECRET_KEY'))
            except:
                return jsonify({'message' : 'Token non valido!'}), 403
            return f(*args, **kwargs)
    return decorated

# DB CONNECTION
db_name = app.config.get('DATABASE')
db_user = app.config.get('DB_USER')
db_pass = app.config.get('DB_PASS')
db_host = app.config.get('DB_HOST')
con = psycopg2.connect(database=db_name, user=db_user, password=db_pass, host=db_host)

# ROUTES
@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == app.config.get('USERNAME') and password == app.config.get('PASSWORD'):
        token = jwt.encode({'user' : username, 'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=60)}, app.config.get('SECRET_KEY'))
        return jsonify({'token' : token.decode('UTF-8')})
    else:
        return make_response('Impossibile verificare!', 401, {'WWW-Authenticate':'Basic realm="Login Required"'})

@app.route('/punti')
@token_required
def punti():
    # return jsonify({'message' : 'Contenuto visibile solo agli utenti autorizzati'})
    sql = "SELECT * FROM punti_campionamento;"
    gdf = gpd.GeoDataFrame.from_postgis(sql,con,geom_col="geom")
    punti_campionamento = json.loads(gdf.to_json())
    return jsonify(punti_campionamento)
    
@app.route('/comuni')
@token_required
def comuni():
    nome = request.args.get('nome')
    if nome:
        sql = "SELECT * FROM comuni_abruzzo WHERE nome = '"+nome+"';"
    else:
        sql = "SELECT * FROM comuni_abruzzo;"
    gdf = gpd.GeoDataFrame.from_postgis(sql,con,geom_col="geom")
    comuni_abruzzo = json.loads(gdf.to_json())
    return jsonify(comuni_abruzzo)

@app.route('/dati/microbiologici')
@token_required
def dati_microbiologici():
    indici = request.args.get('indici')
    if indici:
        if indici in ['biodiversita_funzionale','biodiversita_genetica']:
            table = 'indici_'+indici
            sql = 'SELECT * FROM '+table+';'
            df = pd.read_sql_query(sql,con)
            valori = json.loads(df.to_json(orient='records'))
            return jsonify(valori)
        else:
            return jsonify({"message" : "indici sconosciuti!"})
    else:
        return jsonify({"message" : "occorre specificare gli indici desiderati!"})

@app.route('/dati/vinificazione')
@token_required
def dati_vinificazione():
    parametri = request.args.get('parametri')
    if parametri:
        if parametri in ['maturazione_tecnologica','microvinificazione']:
            table = 'parametri_'+parametri
            sql = 'SELECT * FROM '+table+';'
            df = pd.read_sql_query(sql,con)
            valori = json.loads(df.to_json(orient='records'))
            return jsonify(valori)
        else:
            return jsonify({"message" : "parametri sconosciuti!"})
    else:
        return jsonify({"message" : "occorre specificare parametri desiderati!"})

# app.run(host='127.0.0.1', debug=True)
app.run(host='0.0.0.0', debug=True)