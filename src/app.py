import os
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from models import db

load_dotenv()

app = Flask(__name__)

app.config['DEBUG'] = True # Permite ver los errores
app.config['ENV'] = 'development' # Activa el servidor en modo desarrollo
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASEURI') # Leemos la url de conexion a la base de datos

db.init_app(app)
Migrate(app, db)

@app.route('/')
def main():
    return jsonify({ "status": "Server Up"}), 200

if __name__ == '__main__':
    app.run()