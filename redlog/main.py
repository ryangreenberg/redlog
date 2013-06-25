#!/usr/bin/env python
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
      self.response.write('Hello world!')

class ApiHandler(webapp2.RequestHandler):
    def get(self, username):
      self.response.write('GET %s' % username)
    
    def post(self, username):
      self.response.write('POST %s' % username)

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  webapp2.Route(r'/v1/<username>/read', handler=ApiHandler, name='api-read')
], debug=True)
