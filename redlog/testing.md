A simple object (in application/json) to send to test the POST verb:

    {"user": "npdoty", "read": "guid-of-an-ATOM-feed-item-12345678", "timestamp": 22233334444, "client-app": "MyBrowser"}

Recommend using http-console (a quick npm install), changing to the appropriate path, using .j to set the Content Type and then get/post.

For automated testing, install (all in python2.7, I suggest): nose, gaenose, unittest2, WebTest, autonose, yanc. And run:

    autonose -x--with-gae -x--with-yanc

... will automatically run tests when code or tests are changed, with nicely-colored output.