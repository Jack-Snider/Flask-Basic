from flask import Flask
import random

app = Flask( __name__ )


topics = [
    { 'id':1, 'title' : 'html', 'body' : 'html is ...' },
    { 'id':2, 'title' : 'css', 'body' : 'css is ...' },
    { 'id':3, 'title' : 'javascript', 'body' : 'javascript is ...' }
]

@app.route( '/' )
def index():
    # return type should be String
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href = "/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''
        <!doctype html>
        <html>
            <body>
                <h1><a href = "/">WEB</a></p></h1>
                <ol>
                    {liTags}
                </ol>
                <h2>Welcome</h2>
                Hello, Web
            </body>
        </html>
    '''

@app.route( '/create' )
def create():
    return 'Create'

# if you want to add a parameter in route
# you have to add parameter in funtion as well
@app.route( '/read/<id>/' )
def read( id ):
    print( id )
    return 'Read ' + id

# stop server : Ctrl + c
# debug = True : when you fix the code, it reflects to the server autometically
app.run( port=5001 , debug = True )