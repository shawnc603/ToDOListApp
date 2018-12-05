from flask import (Flask, jsonify, request, Blueprint,
                  url_for,render_template, redirect)
from TODOLISTAPP import mongo
from TODOLISTAPP.tasks.utils import getTask
from TODOLISTAPP.sms.utils import buildSMSTaskEvent
from TODOLISTAPP.calendar.utils import buildCalendarTaskEvent
from TODOLISTAPP.search.utils import insertES
from bson import ObjectId

tasks = Blueprint('tasks', __name__)

@tasks.route('/displayTasks', methods=['GET'])
def displayTasks():
    return render_template('display_tasks.html', title='To Do List App')

@tasks.route('/getUserTasks/<userid>', methods=['GET'])
def getUserTasks(userid):
    taskCollection = mongo.db.tasks 
    output = []
    for item in taskCollection.find({'userid' : userid}):
        output.append({'task' : item['task'], 'description' : item['description'], 
                                'date' : item['date'],'priority' : item['priority']})
    return jsonify(output)

@tasks.route('/getTasks', methods=['GET'])
def getTasks():
    taskCollection = mongo.db.tasks 
    output = []
    for item in taskCollection.find():
        output.append({'_Id' : str(item['_id']), 'task' : item['task'], 'description' : item['description'], 
                            'date' : item['date'],'priority' : item['priority']})
    return jsonify(output)

@tasks.route('/registerTask', methods=['POST','GET'])
def registerTask():
    if request.method == 'GET':
        return render_template('add_tasks.html', title='To Do List App')
    # try:
    #      datetime.datetime.strptime(request.json['date'], '%Y-%m-%d')
    # except ValueError:
    #      return "Incorrect data format, should be YYYY-MM-DD"
    output = []
    item = request.json
    UserId= str(item['userid'])
    if not UserId:
        return "UserId not found cannot insert task"
    taskCollection = mongo.db.tasks 
    output.append({'task' : item['task'], 'description' : item['description'], 
                        'date' : item['date'], 'priority' : item['priority'], 'userid' : UserId})
    task_Id = taskCollection.insert(output)
    #taskItem = getTask(task_Id)
    if request.json['priority'] == "1":
        link = buildCalendarTaskEvent(request.json)
        buildSMSTaskEvent(request.json, link)
        #insertES('contents','todolist') 
        pass     
    if task_Id:
        return getTasks()
    else:
        return jsonify({'result' : 'error'})  

@tasks.route('/updateTask', methods=['POST'])
def UpdateTask():
    taskCollection = mongo.db.tasks 
    ItemId = request.json['_Id']
    record = taskCollection.find_one({'_id' : ObjectId(ItemId)})
    record['task'] = request.json['task']
    record['description'] = request.json['description']
    record['date'] = request.json['date']
    record['priority'] = request.json['priority']
    taskCollection.save(record)
    return getTasks()

@tasks.route('/deleteTask', methods=['POST'])
def deleteTask():
    taskCollection = mongo.db.tasks 
    ItemId = request.json['_Id']
    record = taskCollection.find_one({'_id' : ObjectId(ItemId)})
    taskCollection.remove(record)
    return getTasks()