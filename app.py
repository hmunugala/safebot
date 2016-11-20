# -*- coding: utf-8 -*-

import os
from flask import Flask, request, Response
from slackclient import SlackClient
from twilio import twiml
from twilio.rest import TwilioRestClient
# import db from extensions

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET', None)
TWILIO_NUMBER = u'+13132142564'#os.environ.get('TWILIO_NUMBER', None)
USER_NUMBER = u'+17347300455'#os.environ.get('USER_NUMBER', None)
app = Flask(__name__)
slack_client = SlackClient(os.environ.get('SLACK_TOKEN', None))
twilio_client = TwilioRestClient()

import random
import random
myList = ['Your dad jokes here', 'even more dad jokes,']
random.choice(myList)


@app.route('/twilio', methods=['POST'])
def twilio_post():
    response = twiml.Response()
    if  request.form['From'] == USER_NUMBER:
        # body = request.form['Body']
        message = 'mm,m' #used to keep logs
        slack_client.api_call("chat.postMessage", channel="#dadbot",
                              text=message, username='dadbot',
                              icon_emoji=':robot_face:')

        # connect to db and retrieve data
        # ur = db.cursor()
        # cur.execute('DELETE FROM Photo WHERE picid IN ' +
        #         '(SELECT picid FROM Contain WHERE albumid = {})'.format(albumid))
        # rows = cur.fetchall()
        # col = rows[0]['key']

        twilio_client.messages.create(to=USER_NUMBER, from_=TWILIO_NUMBER,
                                      body=message)

    return Response(response.toxml(), mimetype="text/xml"), 200

# @app.route('/slack', methods=['POST'])
# def slack_post():
#     if request.form['token'] == u'5PWG5cmtNM2B5dfT1okfFOjW': #SLACK_WEBHOOK_SECRET:
#         channel = request.form['channel_name']
#         username = request.form['user_name']
#         response_message = username + " in " +  channel + " says: " + random.choice(myList)
#         twilio_client.messages.create(to=USER_NUMBER, from_=TWILIO_NUMBER,
#                                       body=response_message)
#     return Response(), 200

@app.route('/', methods=['GET'])
def test():
   return Response('It works!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
