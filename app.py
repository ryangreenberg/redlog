# From https://devcenter.heroku.com/articles/python
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return 'redlog'

@app.route('/v1/<username>/read', methods=['GET'])
def show_read_items(username):
  return "This is a list of things that %s has read" % username

@app.route('/v1/<username>/read', methods=['POST'])
def add_read_item(username):
  return "Reading item"

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)