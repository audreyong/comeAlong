import webapp2
import logging
from google.appengine.ext import ndb

class Notification(ndb.Model):
    sender = ndb.StringProperty()
    listofReceivers = ndb.StringProperty(repeated=True)
    diningHallSelected = ndb.StringProperty()
    dateSelected = ndb.DateProperty()
    timeSelected = ndb.TimeProperty()

    # username = ndb.StringProperty()
    # listofFriends = ndb.StringProperty(repeated=True)
    # listofFriendsNotified = ndb.StringProperty(repeated=True)
    # diningHallSelected = ndb.StringProperty()
    # dateSelected = ndb.StringProperty() # can change the property to datetime
    # timeSelected = ndb.StringProperty()
