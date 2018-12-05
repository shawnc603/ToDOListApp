from flask import (Flask, jsonify, request, Blueprint,
                  url_for,render_template, redirect)
import os, base64, re, logging, json
from elasticsearch import Elasticsearch
from TODOLISTAPP.config import Config

def connectES():
    # Log transport details (optional):
    logging.basicConfig(level=logging.INFO)

    auth = re.search('https\:\/\/(.*)\@', Config.ELSEARCH_URL).group(1).split(':')
    host = Config.ELSEARCH_URL.replace('https://%s:%s@' % (auth[0], auth[1]), '')

    es_header = [{
    'host': host,
    'port': 443,
    'use_ssl': True,
    'http_auth': (auth[0],auth[1])
    }]

    es = Elasticsearch(es_header)
    if es.ping():
        return es

def createES(index):
    es = connectES()
    if es.indices.exists(index):
        es.indices.delete(index=index)
    res = es.indices.create(index=index, body=request.json)
    return jsonify(res)

def insertES(index_val,doctype_val):
    es = connectES()
    id = request.json['id']
    result = es.index(index=index_val, doc_type=doctype_val, id=id, body=request.json)
    return jsonify(result)

def searchES(index_val,keyword):
    es = connectES()
    search_object = {"query": {"match": {'task':keyword}}}
    return  jsonify(es.search(index=index_val, body=json.dumps(search_object)))           

def getES(index_val,doctype_val,id):
    es = connectES()
    return jsonify(es.get(index=index_val, doc_type=doctype_val, id=id)) 

def deleteES(index_val,doctype_val,id):
    es = connectES()
    return jsonify(es.delete(index=index_val, doc_type=doctype_val, id=id))

