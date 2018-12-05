from flask import (Flask, jsonify, request, Blueprint,
                  url_for,render_template,url_for, redirect)
import os
from httplib2 import Http
from oauth2client import file, client, tools
import oauth2client
import httplib2
from apiclient import discovery
from TODOLISTAPP.config import Config

def buildCalendarTaskEvent(taskitem):
    emailTemplate = {
                "summary": taskitem['task'],
                "location": "",
                "description": taskitem['description'],
                "start": {
                    "dateTime": taskitem['date']+"T09:00:00-07:00"
                    },
                    "end": {
                    "dateTime": taskitem['date']+"T17:00:00-07:00"
                },
                "reminders": {
                    "useDefault": "False",
                    "overrides": [
                    {"method": "email", "minutes": 1440},
                    {"method": "popup", "minutes": 10}
                    ]
                }
            }
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    event = service.events().insert(calendarId='primary', body=emailTemplate).execute()
    link = event.get('htmlLink')
    return link

    
def get_credentials():
    home_dir = os.path.expanduser('~') 
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'calendar-python-quickstart.json')


    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(Config.CLIENT_SECRET_FILE, Config.SCOPES)
        flow.user_agent = Config.APPLICATION_NAME
        try:
            import argparse
            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        except ImportError:
            flags = None
        if flags:
            credentials = tools.run_flow(flow, store, flags)
    return credentials