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
admin_table = db.admin_data

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api/points', methods = ['GET','POST'])
def people():
    if request.method == 'POST':
        data = request.get_json()
        return str(people_table.insert({'location': [data['lat'],data['lng'] ], 'priority': data['priority'], 'note': data['note'], 'status':0,'time':str(datetime.datetime.now())}))
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
        data = request.get_json()
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
        data = request.get_json()
        return str(vehicles_table.update({'_id': ObjectId(id)}, {'name': data['name'], 'size': data['size'], 'quantity': data['quantity']}))

@app.route('/api/start', methods = ['PUT'])
def vehicles_up(id):
    data = request.get_json()
    return str(admin_table.update({'name': 'start'}, {'location': [data['lat'],data['lat']]}))


@app.route('/api/routes', methods = ['GET'])
def get_routes_wrapper():
    start_entry = admin_table.find_one({'name':'start'})
    start = Point(start_entry['location'][0],start_entry['location'][1])
    vs = []
    for vehicles in vehicles_table.find():
        for i in range(0, vehicles['quantity']):
            vs.append(vehicles['size'])

    points = []
    for person in people_table.find({'status':0}):
        person['time'] = str(person['time'])
        person['_id'] =  str(person['_id'])
        points.append(Point(person['location'][0],person['location'][1]).get_serialisable())

    return json.dumps(get_routes(start,points,vs))
