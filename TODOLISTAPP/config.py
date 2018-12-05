import os

class Config:
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    CLIENT_SECRET_FILE = 'credentials.json'
    APPLICATION_NAME = 'Add A task'
    POSTGRES_URL = 'postgres://hycbnzas:sbM69r5JJmctKn5fjoW5BYNliuwye8ab@elmer.db.elephantsql.com:5432/hycbnzas'
    CLOUDAMQP_URL = 'amqp://ggsflcmt:J0qsxQqtx7z2JxyUQVH0yDR3HV5w3ok_@toad.rmq.cloudamqp.com/ggsflcmt'
    ELSEARCH_URL = 'https://8wokztxis8:3dzoqyio7q@test-cluster-2917818223.us-west-2.bonsaisearch.net'
    MONGO_URI = 'mongodb://test:test123@ds133353.mlab.com:33353/mydatabase'
    MONGO_DBNAME = 'mydatabase'
    SMS_USERNAME = 'shawn.chaudhry.brandmuscle@gmail.com'
    SMS_PASSWORD = 'trade_one'
    SMS_PHONE_NUM ='5125655205'
    SMTP = 'smtp.gmail.com'
    SMTP_PORT =587
    CELERY_BROKER_URL = 'amqp://ggsflcmt:J0qsxQqtx7z2JxyUQVH0yDR3HV5w3ok_@toad.rmq.cloudamqp.com/ggsflcmt'
    CELERY_RESULT_BACKEND= 'amqp://ggsflcmt:J0qsxQqtx7z2JxyUQVH0yDR3HV5w3ok_@toad.rmq.cloudamqp.com/ggsflcmt'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'shawn.chaudhry.brandmuscle@gmail.com'
    MAIL_PASSWORD = 'trade_one'
    MAIL_DEFAULT_SENDER = 'shawn.chaudhry.brandmuscle@gmail.com'
