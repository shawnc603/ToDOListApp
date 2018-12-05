from flask import (Flask, jsonify, request, Blueprint,
                  url_for,render_template, redirect)
import smtplib
from TODOLISTAPP.config import Config

sms = Blueprint('sms', __name__)

@sms.route('/smsHome')
def smsHome():
    return render_template('smshome.html', title='To Do List App')

@sms.route('/sendEmail', methods=['POST'])
def sendEmail():
    s = smtplib.SMTP(Config.SMTP, Config.SMTP_PORT)  
    s.starttls() 
    s.login(Config.SMS_USERNAME, Config.SMS_PASSWORD) 
    message = request.json['email_sms_message']
    receiver_email = request.json['recipient_email_phonenum']
    s.sendmail(Config.SMS_USERNAME, receiver_email, message) 
    s.quit() 
    return jsonify({'status' : '200', 'message' : 'success'})


@sms.route('/sendSMS', methods=['POST'])
def sendSMS():
    carriers = {
        'att':    '@mms.att.net',
        'tmobile':' @tmomail.net',
        'verizon':  '@vtext.com',
        'sprint':   '@page.nextel.com'
    }
    users = mongo.db.users
    existing_user = users.find_one({'userid' : request.json['userid']})
    
    to_number = request.json['recipient_email_phonenum']+'{}'.format(carriers[existing_user['phonecarrier']])
    auth = (Config.SMS_USERNAME, Config.SMS_PASSWORD)

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail(auth[0], to_number, request.json['email_sms_message'])
    return jsonify({'status' : '200', 'message' : 'success'})
