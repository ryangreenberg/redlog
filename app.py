# From https://devcenter.heroku.com/articles/python
import os
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello():
  return 'redlog'

@app.route('/v1/<username>/read', methods=['GET'])
def show_read_items(username):
  if 'If-Modified-Since' in request.headers:
    since_header = request.headers['If-Modified-Since']
    since = datetime.datetime.fromtimestamp( email.utils.mktime_tz(email.utils.parsedate_tz( since_header )), pytz.utc )
    # TODO: only return results that have timestamps after `since`
  
  resp_str = "This is a list of things that %s has read" % username
  resp = Response(resp_str, status=200, mimetype='application/json')
  return resp

@app.route('/v1/<username>/read', methods=['POST'])
def add_read_item(username):
  if 'item' in request.form:
    resp_str = "Reading %s..." % request.form['item']
  else:
    resp_str = "Nothing to read."
  
  resp = Response(resp_str, status=200, mimetype='application/json')
  return resp

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)