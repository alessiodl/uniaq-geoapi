import os
from flask import Flask, jsonify, request, make_response, url_for
from flask_cors import CORS
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
app = Flask(__name__, static_folder="raster_data")
app.config.from_pyfile(os.path.join('config', 'api.conf'), silent=False)
CORS(app)

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
@app.route('/api/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == app.config.get('USERNAME') and password == app.config.get('PASSWORD'):
        token = jwt.encode({'user' : username, 'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=60)}, app.config.get('SECRET_KEY'))
        return jsonify({'token' : token.decode('UTF-8')})
    else:
        return make_response('Impossibile verificare!', 401, {'WWW-Authenticate':'Basic realm="Login Required"'})

@app.route('/api/punti')
@token_required
def punti():
    istat = request.args.get('istatComune')
    if istat:
        sql = "SELECT * FROM punti_campionamento WHERE cod_istat = '"+istat+"';"
    else: 
        sql = "SELECT * FROM punti_campionamento;"
    gdf = gpd.GeoDataFrame.from_postgis(sql,con,geom_col="geom")
    punti_campionamento = json.loads(gdf.to_json())
    return jsonify(punti_campionamento)
    
@app.route('/api/comuni')
@token_required
def comuni():
    istat = request.args.get('istatComune')
    if istat:
        sql = "SELECT * FROM comuni_abruzzo WHERE cod_istat = '"+istat+"';"
    else:
        sql = "SELECT * FROM comuni_abruzzo ORDER BY nome;"
    gdf = gpd.GeoDataFrame.from_postgis(sql,con,geom_col="geom")
    comuni_abruzzo = json.loads(gdf.to_json())
    return jsonify(comuni_abruzzo)

@app.route('/api/dati/microbiologici')
@token_required
def dati_microbiologici():
    tipo = request.args.get('tipoDati')
    istat = request.args.get('istatComune')
    if tipo:
        if tipo in ['biodiversita_funzionale','biodiversita_genetica']:
            table = 'indici_'+tipo
            sql = 'SELECT * FROM '+table+' WHERE "COD_ISTAT" = \''+istat+'\';'
            df = pd.read_sql_query(sql,con)
            valori = json.loads(df.to_json(orient='records'))
            return jsonify(valori)
        else:
            return jsonify({"message" : "dati non presenti!"})
    else:
        return jsonify({"message" : "occorre specificare i dati microbiologici desiderati!"})

@app.route('/api/dati/vinificazione')
@token_required
def dati_vinificazione():
    tipo = request.args.get('tipoDati')
    istat = request.args.get('istatComune')
    if tipo:
        if tipo in ['maturazione_tecnologica','microvinificazione']:
            table = 'parametri_'+tipo
            sql = 'SELECT * FROM '+table+' WHERE "COD_ISTAT" = \''+istat+'\';'
            df = pd.read_sql_query(sql,con)
            valori = json.loads(df.to_json(orient='records'))
            return jsonify(valori)
        else:
            return jsonify({"message" : "dati non presenti!"})
    else:
        return jsonify({"message" : "occorre specificare i dati di microvinificazione desiderati!"})

@app.route('/api/raster/dem')
def dem():
	image_url = url_for('static', filename='DEM_crop_wgs84.tif')
	return jsonify({"url":image_url, "min":155.378, "max":334.486, "description":"Digital Elevation Model","provider":"UNIVAQ_DISIM"})

@app.route('/api/raster/esposizione')
def esposizione():
	image_url = url_for('static', filename='Esposizioni_crop_wgs84.tif')
	return jsonify({"url":image_url, "min":7.20119, "max":352.786, "description":"Mappa della Esposizione","provider":"UNIVAQ_DISIM"})

@app.route('/api/raster/pendenza')
def pendenza():
	image_url = url_for('static', filename='Pendenza_crop_wgs84.tif')
	return jsonify({"url":image_url, "min":1.99969, "max":57.068,"description":"Mappa della Pendenza","provider":"UNIVAQ_DISIM"})

# app.run(host='127.0.0.1', debug=True)
app.run(host='0.0.0.0', debug=True)