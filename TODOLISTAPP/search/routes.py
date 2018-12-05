from flask import (Flask, jsonify, request, Blueprint,
                  url_for,render_template,url_for, redirect)
import os, base64, re, logging, json
from elasticsearch import Elasticsearch
from TODOLISTAPP.search.utils import connectES, createES, insertES, getES, deleteES, searchES


search = Blueprint('search', __name__)

@search.route('/searchTasks')
def searchTasks():
    return render_template('search_tasks.html', title='To Do List App')

@search.route('/createES/<string:index>', methods=['POST'])
def createES(index):
    res = createES(index)
    return jsonify(res)

@search.route('/insertES/<string:index_val>/<string:doctype_val>', methods=['POST'])
def insertES(index_val,doctype_val):
    res=  insertES(index_val,doctype_val)
    return jsonify(res)

@search.route('/searchES/<string:index_val>/<string:keyword>', methods=['GET'])
def searchES(index_val,keyword):
    res = searchES(index_val,keyword)
    return  jsonify(res)           

@search.route('/getES/<string:index_val>/<string:doctype_val>/<string:id>', methods=['GET'])
def getES(index_val,doctype_val,id):
    res = getES(index_val,doctype_val,id)
    return jsonify(res) 

@search.route('/deleteES/<string:index_val>/<string:doctype_val>/<string:id>', methods=['GET'])
def deleteES(index_val,doctype_val,id):
    res = deleteES(index_val,doctype_val,id)
    return jsonify(res)