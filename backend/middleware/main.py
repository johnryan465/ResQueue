from flask import Flask
from tinydb import TinyDB, Query
import datetime
Point = Query()
points_db = TinyDB('points_db.json')
vehicles_db = TinyDB('vehicles_db.json')

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route('/api/points', methods = ['GET','POST'])
def points():
    if request.method == 'POST':
        data = request.form
        return points_db.insert({'lat': data['lat'], 'long': data['long'], 'priority': data['priority'], 'note': data['note'], 'status':0,'time':datetime.datetime.now()})
    if request.method == 'GET':
        return points_db.all()

@app.route('/api/vehicles', methods = ['GET','PUT','POST'])
def vehicles():
    if request.method == 'POST':
        data = request.form
        return vehicles_db.insert({'name': data['name'], 'size': data['size'], 'quantity': data['quantity']})
    if request.method == 'GET':
        return vehicles_db.all()
    if request.method == 'PUT':
        data = request.form
        return vehicles_db.update({'name': data['name'], 'size': data['size'], 'quantity': data['quantity']},doc_ids=[data[id]])


def get_routes():
    vehicles_sizes = []
