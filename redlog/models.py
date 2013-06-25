from google.appengine.ext import db

class Log(db.Model):
  user = db.UserProperty(required=True)
  date_added = db.DateTimeProperty(auto_now_add=True)
  identifier = db.StringProperty(required=True)
  date_read = db.DateTimeProperty()
  client = db.StringProperty()
  device = db.StringProperty()