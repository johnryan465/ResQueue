from flask import Flask, request
from pymongo import MongoClient
from bson import ObjectId
from util import Point
from libroute import libroute
import datetime
import json
import requests


client = MongoClient("***REMOVED***")
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
        url = "***REMOVED***" + str(data['lat']) + "/"+ str(data['lng'])+ "/alerts.json"
        response = requests.request("GET", url)
        rep = json.loads(response.text)
        severity = 1000000
        if 'alerts' in rep:
            for alert in rep['alerts']:
                severity = min(severity,alert['severity_cd'])
        return str(people_table.insert({'location': [data['lat'],data['lng'] ], 'priority': data['priority'], 'note': data['note'], 'status':0,'time':str(datetime.datetime.now()),'severity':severity}))
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
    print(start_entry)
    start = Point(start_entry['location'][0],start_entry['location'][1])
    vs = []
    for vehicles in vehicles_table.find():
        for i in range(0, int(vehicles['quantity'])):
            vs.append(int(vehicles['size']))

    points = []
    for person in people_table.find():
        person['time'] = str(person['time'])
        person['_id'] =  str(person['_id'])
        points.append(Point(person['location'][0],person['location'][1]))
    print(1)
    return json.dumps(libroute.get_routes(start,points,vs).get_list())
