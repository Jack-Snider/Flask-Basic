from flask import Flask
import random

# create Flask object for server
app = Flask( __name__ )


topics = [
    { 'id':1, 'title' : 'html', 'body' : 'html is ...' },
    { 'id':2, 'title' : 'css', 'body' : 'css is ...' },
    { 'id':3, 'title' : 'javascript', 'body' : 'javascript is ...' }
]


def template( contents, content ):

     return f'''
        <!doctype html>
        <html>
            <body>
                <h1><a href = "/">WEB</a></p></h1>
                <ol>
                    {contents}
                </ol>
                {content}
                <ul>
                <li><a href = "/create/">create</a></li>
                </ul>
            </body>
        </html>
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href = "/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

# index page
@app.route( '/' )
def index():
    # return type should be String
    return template( getContents(), '<h2>Weclome</h2>Hello, Web' )


# if you want to add a parameter in route
# you have to add parameter in funtion as well
@app.route( '/read/<int:id>/' )
def read( id ):

    title = ''
    body = ''

    for topic in topics:
        if id == topic[ "id" ]:
            title = topic[ 'title' ]
            body = topic[ 'body' ]
            break

    return template( getContents(), f'<h2>{title}</h2>{body}' )

@app.route( '/create/' )
def create():
    content = \
    '''
        <form action = "/create/" method = "POST">
            <p><input type = "text" name = "title" placeholder = "title"></p>
            <p><textarea name = "body" placeholder = "body"></textarea></p>
            <p><input type = "submit" value = "create"></p>
        <form>
    '''
    return template( getContents(), content )


# stop server : Ctrl + c
# debug = True : when you fix the code, it reflects to the server autometically
app.run( port=5001 , debug = True )