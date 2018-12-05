from flask import (Flask, jsonify, request, Blueprint,url_for,render_template,
                   url_for, redirect, json, jsonify, make_response)
import bcrypt
from TODOLISTAPP import mongo

authentication = Blueprint('authentication', __name__)

@authentication.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='To Do List App')
    users = mongo.db.users
    login_user = users.find_one({'username' : request.json['username']})

    if login_user:
        # salt = bcrypt.gensalt()
        # hashpass = bcrypt.hashpw(request.json['password'], salt)
        password = request.json['password']
        if password == login_user['password']:           
            return jsonify({'status' : '200', 'message' : 'success', 'userid' : str(login_user['_id'])})
    return jsonify({'status' : '409', 'message' : 'Invalid username/password combination'})


@authentication.route('/registerUser', methods=['POST', 'GET'])
def registerUser():
    if request.method == 'GET':
        return render_template('register_user.html', title='To Do List App')
    users = mongo.db.users
    existing_user = users.find_one({'username' : request.json['username']})

    if existing_user is None:
        # salt = bcrypt.gensalt()
        # hashpass = bcrypt.hashpw(request.json['password'], salt)
        Id = users.insert({'username' : request.json['username'], 'password' : request.json['password'] \
        , 'email' : request.json['email'] , 'phone' : request.json['phone'] , \
            'phonecarrier' : request.json['phonecarrier'] })
        return jsonify({'status' : '200', 'message' : 'success', 'userid' : str(Id)})
    return jsonify({'status' : '409', 'message' : 'Invalid username/password combination'})

@authentication.route('/logout', methods=['GET'])
def logout():
    resp =  make_response()
    resp.delete_cookie('userid')
    return render_template('login.html', title='To Do List App')