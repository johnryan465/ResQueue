from flask import Flask, request
from pymongo import MongoClient
from bson import ObjectId
from util import Point
import datetime
import json
client = MongoClient("mongodb://resqueue:xhCZluztAHMaBa5bhpyBOdizbbdZ9MpzIB86XFFW4heqazNsXud9544V64ASltl7WtTZlRj1vFpgpprKkBVMJA==@resqueue.documents.azure.com:10255/?ssl=true&replicaSet=globaldb")
db = client.resqueue

people_table = db.people
vehicles_table = db.vehicles
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api/points', methods = ['GET','POST'])
def people():
    if request.method == 'POST':
        data = request.form
        return str(people_table.insert({'location': [data['latitude'],data['longitude'] ], 'priority': data['priority'], 'note': data['note'], 'status':0,'time':str(datetime.datetime.now())}))
    if request.method == 'GET':
        l = []
        for person in people_table.find():
            person['time'] = str(person['time'])
            person['_id'] =  str(person['_id'])
            person['location'] = Point(person['location'][0],person['location'][1]).get_serialisable()
            l.append(person)
        return json.dumps(l)

@app.route('/api/vehicles', methods = ['GET','POST'])
def new_veh():
    if request.method == 'POST':
        data = request.form
        return str(vehicles_table.insert({'name': data['name'], 'size': data['size'], 'quantity': data['quantity']}))
    if request.method == 'GET':
        l = []
        for vehicles in vehicles_table.find():
            vehicles['_id'] =  str(vehicles['_id'])
            l.append(vehicles)
        return json.dumps(l)

@app.route('/api/vehicles/<id>', methods = ['GET','PUT'])
def vehicles(id):
    if request.method == 'GET':
        vehicle = vehicles_table.find_one({'_id':ObjectId(id)})
        vehicle['_id'] =  str(vehicle['_id'])
        return json.dumps(vehicle)

    if request.method == 'PUT':
        data = request.form
        return str(vehicles_db.update({'_id': ObjectId(id)}, {'name': data['name'], 'size': data['size'], 'quantity': data['quantity']}))
