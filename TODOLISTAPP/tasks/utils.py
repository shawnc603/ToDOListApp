from flask import (Flask, jsonify, request, Blueprint,
                  url_for,render_template,url_for, redirect)
import smtplib
from TODOLISTAPP import mongo
from TODOLISTAPP.config import Config

def getTask(dbid):
     taskCollection = mongo.db.tasks 
     output = []
     item = taskCollection.find_one({'_id': dbid})
     output.append({'_Id' : str(item['_id']), 'task' : item['task'], 'description' : item['description'], 'date' : item['date'],'priority' : item['priority']})
     return jsonify(output)


