import webapp2
import logging
from google.appengine.ext import ndb

class Notify(ndb.Model):
    listofFriends = ndb.StringProperty()
    diningHallSelected = ndb.StringProperty()
    dateSelected = ndb.StringProperty() # can change the property to datetime
    timeSelected = ndb.StringProperty()
