
from flask import Flask, request, render_template, session, flash, redirect, url_for, jsonify, Blueprint, json
from flask_mail import Mail, Message
from celery import Celery
import urllib.request
import os, time, random
import pika
from TODOLISTAPP.config import Config
from TODOLISTAPP import mail
from TODOLISTAPP.queue.utils import send_async_email

queue = Blueprint('queue', __name__)

@queue.route('/publishQueue', methods=['POST'])
def publishQueue():
    #url = os.environ.get(Config.CLOUDAMQP_URL, 'amqp://ggsflcmt:J0qsxQqtx7z2JxyUQVH0yDR3HV5w3ok_@toad.rmq.cloudamqp.com/ggsflcmt)
    params = pika.URLParameters(Config.CLOUDAMQP_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue='testqueue') # Declare a queue
    channel.basic_publish(exchange='',routing_key='MyQueue',body=request.json['task'])  
    connection.close()
    return " Sent to Queue:"

@queue.route('/sendEmailQ', methods=['GET', 'POST'])
def sendEmailQ():
    if request.method == 'GET':
        return render_template('email.html', email=session.get('email', ''))
    if request.method == 'POST':
        #msg = Message()
        #msg.subject = 'test email from celery'
        #msg.recipients = request.json['email']
        #msg.body = "rrrrrrrrrrrrrrrrrrr"
        send_async_email.delay()

    # email = request.form['email']
    # session['email'] = email

    # send the email
    # msg = Message('Hello from Flask', recipients=[request.form['email']])
    # msg.body = 'This is a test email sent from a background Celery task.'
    # if request.form['submit'] == 'Send':
    #     # send right away
    #     send_async_email.delay(msg)
    #     #flash('Sending email to {0}'.format(email))
    # else:
    #     # send in one minute
    #     send_async_email.apply_async(args=[msg], countdown=60)
    #     flash('An email will be sent to {0} in one minute'.format(email))

    # return redirect(url_for('index'))
    return 'done!'