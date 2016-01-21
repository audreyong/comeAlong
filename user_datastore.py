import webapp2
import logging
from google.appengine.ext import ndb

class User(ndb.Model):
    username = ndb.StringProperty()
    listofFriends = ndb.StringProperty(repeated=True)

    # username = ndb.StringProperty()
    # tyler = ndb.IntegerProperty()
    # cutter_ziskind = ndb.IntegerProperty()
    # chapin = ndb.IntegerProperty()
