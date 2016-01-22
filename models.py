import webapp2
import logging
from google.appengine.ext import ndb

class Notification(ndb.Model):
    sender = ndb.StringProperty()
    listofReceivers = ndb.StringProperty(repeated=True)
    diningHallSelected = ndb.StringProperty()
    dateSelected = ndb.DateProperty()
    timeSelected = ndb.TimeProperty()


class User(ndb.Model):
    username = ndb.StringProperty()
    listofFriends = ndb.StringProperty(repeated=True)
