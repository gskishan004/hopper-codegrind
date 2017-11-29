#MONGOLAB SERVER DETAILS 
server = 'ds123896.mlab.com:23896/hopperdb'
port = 23896
db_name = 'hopperdb'
username = 'gskishan004'
password = 'malb4321'

from flask import Flask, session, redirect, url_for, escape, request
from datetime import datetime
from pymongo import MongoClient
import hashlib

app = Flask(__name__)

#DEFINE URL FOR MONGODB SERVER
uri = "mongodb://"+username+":"+password+"@"+server
client = MongoClient(uri)

#GET DATABASE AND TABLE NAME
db=client.cmbwsapi
usersCollection = db.users
ridesCollection = db.rides

#INDEX PAGE
@app.route('/')
def index():
	return "Hopper! \n get hopping..."

# #REGISTER ENDPOINT
# @app.route('/register', methods=['POST'])
# def register():
# 	psid = request.form['psid']
# 	pwd = request.form['password']
# 	# hashing the password
# 	m = hashlib.md5()
# 	m.update(pwd.encode('utf-8'))
# 	pwd = m.hexdigest()
# 	#name = request.form['name']
# 	#building = request.form['building']
# 	managerName = request.form['managerName']
# 	managerContact = request.form['managerContact']
# 	user = {
# 		'psid' : [psid],
# 		'pwd' : [pwd],
# 		 #'name' : [name],
# 		 #'building' : [building],
# 		'managerName' : [managerName],
# 		'managerContact' : [managerContact]
# 	}
# 	result=usersCollection.insert_one(user)
# 	return 'true'

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
			data = str(data)
			data = data.replace('[','')
			data = data.replace(']','')
			data = data.replace("'",'"')
			data = data.replace(')','')
			data = data.replace('ObjectId(','')
			return str(data)
		else:
			return "false"
	except:
		return "false"

# #LOGS FOR LATE STAY 
# @app.route('/latestay', methods=['POST'])
# def lateStay():
# 	psid = request.form['psid']
# 	reason = request.form['reason']
# 	date = request.form['date']
# 	travellingTo = request.form['travellingTo']
# 	travellingBy = request.form['travellingBy']
# 	latestay = {
# 		'psid' : [psid],
# 		'reason' : [reason],
# 		'date' : [date],
# 		'travellingTo' : [travellingTo],
# 		'travellingBy' : [travellingBy]
# 	}
# 	result=lateStayCollection.insert_one(latestay)
# 	return 'true'

#MAIN
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)