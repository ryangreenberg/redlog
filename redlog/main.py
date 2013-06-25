#!/usr/bin/env python
import webapp2
from webob import Response
import json
import models
from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
    def get(self):
      self.response.write('Hello world!')

class ApiHandler(webapp2.RequestHandler):
    def get(self, username):
      self.response.write('GET %s' % username)
      
      if 'If-Modified-Since' in self.request.headers:
        since_header = self.request.headers['If-Modified-Since']
        since = datetime.datetime.fromtimestamp( email.utils.mktime_tz(email.utils.parsedate_tz( since_header )), pytz.utc )
        # TODO: only return results that have timestamps after `since`

      resp_str = "This is a list of things that %s has read" % username
      resp = Response(status=200, content_type='application/json')
      resp.body = resp_str
      return resp
    
    def post(self, username):
      response = Response(content_type='application/json')
      user = users.User(username)

      if self.request.content_type == 'application/json':
        update = json.loads(self.request.body)
        
        if update.read and type(update.read) == type([]):
          pass
        elif update.read and type(update.read) == type(''):
          log = models.Log()
          log.user = user
          log.identifier = update.read
          log.put()
        else:
          pass  # error condition, doesn't include a reading update
      else:
        response.status = 415 # unsupported media type, we only take 'application/json' around here
        response.body = json.dumps({'error':'Only application/json is supported in posting updates.'})

      return response

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  webapp2.Route(r'/v1/<username>/read', handler=ApiHandler, name='api-read')  # handles both get and post to the main endpoint
], debug=True)
