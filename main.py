#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import logging
from google.appengine.ext import ndb
from google.appengine.api import users
import comealong_datastore as data_comealong
import user_datastore as data_user
import json
import datetime

# import gdata.contacts.data
# import gdata.contacts.client

# self.gd_client = gdata.contacts.client.ContactsClient(source='smith-jterm-test-audrey')

JINJA_ENVIRONMENT = jinja2.Environment (
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True # safety measure. prevents sql injection
)

header_template = JINJA_ENVIRONMENT.get_template('templates/header.html')
footer_template = JINJA_ENVIRONMENT.get_template('templates/footer.html')

diningHalls = [
    {'name': 'Tyler',
    'votes': 0},
    {'name': 'Cutter-Ziskind',
    'votes': 0},
    {'name': 'Chapin',
    'votes': 0},
]

friendsList = [
    {'name': 'Angela'},
    {'name': 'Audrey'},
]

tempUsername = "The boss"

class SendHandler(webapp2.RequestHandler):
    def post(self):
        userID = users.get_current_user()
        data = json.loads(self.request.body)
        sender = tempUsername
        listofReceiversID = data['listofFriends'] #change this later
        diningHallSelected = data['diningHallSelected']
        stringDateSelected = data['dateSelected']
        stringTimeSelected = data['timeSelected']


        dateSelected = datetime.datetime.strptime(stringDateSelected, '%m/%d/%Y').date()
        timeSelected = datetime.datetime.strptime(stringTimeSelected, '%H:%M%p').time()

        new_entry = data_comealong.Notification(
            senderID = userID,
            listofReceiversID = listofReceiversID,
            diningHallSelected = diningHallSelected,
            dateSelected = dateSelected,
            timeSelected = timeSelected,
        )
        new_entry.put()


# class NotifyHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write(header_template.render())
#         friendsListTemplate = JINJA_ENVIRONMENT.get_template('templates/notify.html')
#         self.response.write(friendsListTemplate.render({'friendsList': friendsList}))
#         self.response.write(footer_template.render())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        # 173038463819-kfdrevei3tn96onbqdgo3qqmm5iqi546.apps.googleusercontent.com
        if user:
            self.response.write(header_template.render())
            bodyTemplate = JINJA_ENVIRONMENT.get_template('templates/body.html')
            self.response.write(bodyTemplate.render({'diningHalls': diningHalls, 'friendsList': friendsList}))
            self.response.write('<button href="%s">LOGOUT</button>' % users.create_logout_url('/'))
            self.response.write(footer_template.render())
        else:
            self.redirect(users.create_login_url('/'))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    #('/notify', NotifyHandler),
    ('/send', SendHandler),
], debug=True)
