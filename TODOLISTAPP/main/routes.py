from flask import (Flask, jsonify, request, Blueprint,url_for,
                   render_template,redirect)

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('login.html', title='To Do List App')

@main.route('/main')
def home():
    return render_template('main.html', title='To Do List App')



