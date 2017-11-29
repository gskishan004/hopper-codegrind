#MONGOLAB SERVER DETAILS 
server = 'ds123896.mlab.com:23896/hopperdb'
port = 23896
db_name = 'hopperdb'
username = 'ishan'
password = 'ishan'

from flask import Flask, session, redirect, url_for, escape, request
from datetime import datetime
from pymongo import MongoClient
import hashlib

app = Flask(__name__)

#DEFINE URL FOR MONGODB SERVER
uri = "mongodb://"+username+":"+password+"@"+server
client = MongoClient(uri)

#GET DATABASE AND TABLE NAME
db=client.hopperdb
usersCollection = db.users
hopstarsCollection = db.hopstars
ridesCollection = db.riders

#INDEX PAGE
@app.route('/')
def index():
	return "Hopper! \n get hopping..."


#LOGIN ENDPOINT
@app.route('/login', methods=['POST'])
def login():
	psid = request.form['psid']
	pwd = request.form['password']
	m = hashlib.md5()
	m.update(pwd.encode('utf-8'))
	pwd = m.hexdigest()
	data= usersCollection.find_one({'psid': psid})
	try:
		if (data['pwd'][0] == pwd):
			return "true"
		else:
			return "false"
	except:
		return "false"

#REGISTER ENDPOINT
@app.route('/register', methods=['POST'])
def register():
	psid = request.form['psid']
	pwd = request.form['password']
	# hashing the password
	m = hashlib.md5()
	m.update(pwd.encode('utf-8'))
	pwd = m.hexdigest()
	#name = request.form['name']
	#building = request.form['building']
	user = {
		'psid' : [psid],
		'pwd' : [pwd]
	}
	result=usersCollection.insert_one(user)
	return 'true'

@app.route('/registerHopstar', methods=['POST'])
def registerHopstar():
	psid = request.form['psid']
	name = request.form['name']
	home = request.form['home']
	office = request.form['office']
	time = request.form['time']


	hopstar = {
		'psid' : [psid],
		'name' : [name],
		'home' : [home],
		'office' : [office],
		'time' : [time]
	}
	result=hopstarsCollection.insert_one(hopstar)
	return 'true'

@app.route('/registerRiders', methods=['POST'])
def registerRider():
	psid = request.form['hopstar']
	name = request.form['hopper']
	home = request.form['destiantion']
	office = request.form['time']


	rider = {
		'psid' : [psid],
		'name' : [name],
		'home' : [home],
		'office' : [office],
		'time' : [time]
	}
	result=ridersCollection.insert_one(rider)
	return 'true'



#MAIN
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)