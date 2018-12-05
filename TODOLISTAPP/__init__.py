from flask import Flask
from flask_pymongo import PyMongo
from celery import Celery
from TODOLISTAPP.config import Config
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail()
mongo = PyMongo()
celery = Celery()

def create_app(config_class=Config):
    app.config.from_object(Config)
    mongo.init_app(app)
    mail.init_app(app)
    celery = Celery(app.name, broker=Config.CELERY_BROKER_URL)
    celery.conf.update(app.config)
    from TODOLISTAPP.authentication.routes import authentication
    from TODOLISTAPP.calendar.routes import calendar
    from TODOLISTAPP.search.routes import search
    from TODOLISTAPP.sms.routes import sms
    from TODOLISTAPP.tasks.routes import tasks
    from TODOLISTAPP.main.routes import main
    from TODOLISTAPP.queue.routes import queue
    from TODOLISTAPP.scraping.routes import scraping

    app.register_blueprint(authentication)
    app.register_blueprint(calendar)
    app.register_blueprint(search)
    app.register_blueprint(sms)
    app.register_blueprint(tasks)
    app.register_blueprint(main)
    app.register_blueprint(queue)
    app.register_blueprint(scraping)

    return app









#{
#    "_Id": "5bc4ee8a330df507ac3ea4c7",
#    "date": "2018-10-15",
#    "description": "pay bills3",
#    "priority": "1",
#    "task": "pay bills3"
#}


# event = {
#   'summary': 'Google I/O 2015',
#   'location': '800 Howard St., San Francisco, CA 94103',
#   'description': 'A chance to hear more about Google\'s developer products.',
#   'start': {
#     'dateTime': '2018-10-28T09:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'end': {
#     'dateTime': '2018-10-28T17:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'attendees': [
#     {'email': 'lpage@example.com'},
#     {'email': 'sbrin@example.com'},
#   ],
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# }


# {
#    "summary": "My test event",
#    "location": "None",
#    "description": "test event",
#    "start": {
#      "dateTime": "2018-10-28T09:00:00-07:00"
#     },
#     "end": {
#       "dateTime": "2018-10-28T17:00:00-07:00"
#    },
#    "reminders": {
#      "useDefault": "False",
#      "overrides": [
#        {"method": "email", "minutes": 1440},
#        {"method": "popup", "minutes": 10}
#      ]
#    }
# }

# {
#   "message": "Hello how are you?"
# }


#{
#  "message":   "Hello how are you?",
#  "carrier":   "att",
#  "phonenum":  "5125655205"
#}


# request_body = {
#     "settings" : {
#         "number_of_shards": 1,
#         "number_of_replicas": 0
#     },
#     'mappings': {
#         'todolist': {
#             'properties': {
#                 '_id': {'index': 'not_analyzed', 'type': 'string'},
#                 'task': {'index': 'not_analyzed', 'type': 'string'},
#                 'description': {'index': 'not_analyzed', 'type': 'string'},
#                 'priority': {'index': 'not_analyzed', 'type': 'string'},
#                 'date': {'index': 'not_analyzed', 'type': 'string'},
#             }}}
# }