'''
http://127.0.0.1:7008/input_sensor?temperature=30&humidity=79
http://localhost:5000/inputData?mode=save&temp=34.4&humd=56.3&ppmch4=1.3&ppmco=2.2
'''

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify

# objek flask
app = Flask(__name__)

# api-key
app.secret_key = "djfljdfljfnkjsfhjfshjkfjfjfhjdhfdjhdfu"

# koneksi ke database
userpass = "mysql+pymysql://user:pass"
basedir = "@127.0.0.1"
dbname = "/iot_monibot"

app.config["SQLALCHEMY_DATABASE_URI"] = userpass + basedir + dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Monibot(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_temp = db.Column(db.Float, nullable=False)
    data_humd = db.Column(db.Float, nullable=False)
    data_ppmch4 = db.Column(db.Float, nullable=False)
    data_ppmco = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False,
                          server_default=db.func.current_timestamp())

    def __init__(self, data_temp, data_humd, data_ppmch4, data_ppmco):
        self.data_temp = data_temp
        self.data_humd = data_humd
        self.data_ppmch4 = data_ppmch4
        self.data_ppmco = data_ppmco