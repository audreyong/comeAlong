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
import comealong_datastore as data_comealong

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

class SendHandler(webapp2.RequestHandler):
    def post(self):
        pass
        # data = JSON.loads(self.request.body)
        # listofFriends = data['listofFriends']
        # diningHallSelected = self.request.get('diningHallSelected')
        # dateSelected = self.request.get('dateSelected')
        # timeSelected = self.request.get('timeSelected')
        #
        # print(listofFriends)
        # print(diningHallSelected)
        # print(dateSelected)
        # print(timeSelected)


        # new_entry = data_comealong.Notify(
        #     listofFriends = listofFriends,
        #     diningHallSelected = diningHallSelected,
        #     dateSelected = dateSelected,
        #     timeSelected = timeSelected,
        # )
        # new_entry.put()

# class NotifyHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write(header_template.render())
#         friendsListTemplate = JINJA_ENVIRONMENT.get_template('templates/notify.html')
#         self.response.write(friendsListTemplate.render({'friendsList': friendsList}))
#         self.response.write(footer_template.render())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(header_template.render())
        bodyTemplate = JINJA_ENVIRONMENT.get_template('templates/body.html')
        self.response.write(bodyTemplate.render({'diningHalls': diningHalls, 'friendsList': friendsList}))
        self.response.write(footer_template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    #('/notify', NotifyHandler),
    ('/send', SendHandler),
], debug=True)
