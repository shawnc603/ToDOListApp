from flask import Flask, request, render_template, session, flash, redirect, url_for, jsonify
from celery import Celery
from flask_mail import Mail, Message
from TODOLISTAPP.config import Config
from TODOLISTAPP import mail, celery, app

@celery.task
def send_async_email():
        msg = Message()
        msg.subject = 'test email from celery'
        msg.recipients = 'shawnc603@gmail.com'
        msg.body = "testr"
        with app.app_context():
                mail.send(msg)