from flask import (Flask, jsonify, request, Blueprint, render_template)
import httplib2
import oauth2client
from oauth2client import client, tools
from apiclient import discovery
from TODOLISTAPP.calendar.utils import get_credentials


calendar = Blueprint('calendar', __name__)

@calendar.route('/insertCalendar', methods=['POST','GET'])
def insertCalendar():
    if request.method == 'GET':
        return render_template('add_tasks.html', title='To Do List App')
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    event =request.json
    event = service.events().insert(calendarId='primary', body=event).execute()
    return 'Event created: %s' % (event.get('htmlLink'))


