import unittest
import logging

from google.appengine.ext import db
from google.appengine.ext import testbed
from webtest import TestApp
import main

class SimpleGetTests(unittest.TestCase):
  def setUp(self):
    self.app = TestApp(main.app)
  
  def testSimplestGet(self):
    response = self.app.get('/')
    assert "Hello world" in response
  
  def testUserGet(self):
    response = self.app.get('/v1/username/read')
    assert "This is a list" in response
    assert response.content_type == "application/json"

class PostTests(unittest.TestCase):
  def setUp(self):
    self.app = TestApp(main.app)

  def testSinglePost(self):
    response = self.app.post_json('/v1/username/read', {"user": "npdoty", "read": "guid-of-an-ATOM-feed-item-12345678", "timestamp": 22233334444, "client-app": "MyBrowser"})
    assert response.status_code == 201
    
if __name__ == '__main__':
  unittest.main()