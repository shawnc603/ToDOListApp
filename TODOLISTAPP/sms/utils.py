import smtplib
from TODOLISTAPP.config import Config

def buildSMSTaskEvent(taskitem, link):
    carriers = {
        'att':    '@mms.att.net',
        'tmobile':' @tmomail.net',
        'verizon':  '@vtext.com',
        'sprint':   '@page.nextel.com'
    }
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = Config.SMS_PHONE_NUM+'{}'.format(carriers['att'])
    auth = (Config.SMS_USERNAME, Config.SMS_PASSWORD)

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP(Config.SMTP,Config.SMTP_PORT)
    server.starttls()
    server.login(auth[0], auth[1])
    
    url, eid = link.split("=")
    url ="""www.google.com/calendar/event?eid="""+str(eid)
    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], to_number, url)
    return 'sent sms'