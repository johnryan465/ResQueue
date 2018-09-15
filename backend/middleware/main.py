from flask import Flask, request
from pymongo import MongoClient
import datetime
import json
client = MongoClient("mongodb://resqueue:xhCZluztAHMaBa5bhpyBOdizbbdZ9MpzIB86XFFW4heqazNsXud9544V64ASltl7WtTZlRj1vFpgpprKkBVMJA==@resqueue.documents.azure.com:10255/?ssl=true&replicaSet=globaldb")
db = client.resqueue    #Select the database


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
        return people_table.insert({'location': [data['lat'],data['long'] ], 'priority': data['priority'], 'note': data['note'], 'status':0,'time':str(datetime.datetime.now())})
    if request.method == 'GET':
        l = []
        for person in people_table.find():
            l.append(str(person))
        return json.dumps(l)
@app.route('/api/vehicles', methods = ['GET','PUT','POST'])
def vehicles():
    if request.method == 'POST':
        data = request.form
        return vehicles_table.insert({'name': data['name'], 'size': data['size'], 'quantity': data['quantity']})
    if request.method == 'GET':
        return vehicles_table.find()
    if request.method == 'PUT':
        data = request.form
        return vehicles_db.update({'_id': ObjectId(data[id])}, {'name': data['name'], 'size': data['size'], 'quantity': data['quantity']})


def get_routes():
    vehicles_sizes = []
