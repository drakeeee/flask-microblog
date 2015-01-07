from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Adam'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title = 'Home',
                           user=user,
                           posts=posts)


#def index():
#    user = {'nickname':'Miguel'}
#    return '''
#<html>
#  <head>
#    <title>Home Page</title>
#  <head>
#  <body>
#    <h1>Hello, ''' + user['nickname'] + '''</h1>
#  </body>
#</html>
#'''

@app.route('/hw')
def hw():
    return "Hello, World!"
