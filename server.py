from flask import Flask, request, redirect

import random

# create Flask object for server
app = Flask( __name__ )

nextId = 4

topics = [
    { 'id':1, 'title' : 'html', 'body' : 'html is ...' },
    { 'id':2, 'title' : 'css', 'body' : 'css is ...' },
    { 'id':3, 'title' : 'javascript', 'body' : 'javascript is ...' }
]


def template( contents, content, id = None ):
    contextUI = ''
    if id != None:
        contextUI = \
        f'''
            <li><a href = "/update/{id}/">update</a></li>
        '''    
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
                    {contextUI}
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

    return template( getContents(), f'<h2>{title}</h2>{body}', id )

@app.route( '/create/', methods = [ 'GET', 'POST' ] )
def create():
    print( f'request.method : {request.method}' )
    if request.method == 'GET':
        content = \
        '''
            <form action = "/create/" method = "POST">
                <p><input type = "text" name = "title" placeholder = "title"></p>
                <p><textarea name = "body" placeholder = "body"></textarea></p>
                <p><input type = "submit" value = "create"></p>
            <form>
        '''
        return template( getContents(), content )
    elif request.method == 'POST':
        global nextId
        title = request.form[ 'title' ]
        body = request.form[ 'body' ]
        newTopic = { 'id':nextId, 'title':title, 'body':body }
        topics.append( newTopic )
        url = '/read/' + str( nextId ) + '/'
        nextId = nextId + 1
        return redirect( url )
        
@app.route( '/update/<int:id>/', methods = [ 'GET', 'POST' ] )
def update( id ):
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if id == topic[ 'id' ]:
                title = topic[ 'title' ]
                body = topic[ 'body' ]
                break
        content = \
        f'''
            <form action = "/update/{id}/" method = "POST">
                <p><input type = "text" name = "title" placeholder = "title" value = "{title}"></p>
                <p><textarea name = "body" placeholder = "body">{body}</textarea></p>
                <p><input type = "submit" value = "update"></p>
            <form>
        '''
        return template( getContents(), content )

    elif request.method == 'POST':
        global nextId
        title = request.form[ 'title' ]
        body = request.form[ 'body' ]
        for topic in topics:
            if id == topic[ 'id' ]:
                topic[ 'title' ] = title
                topic[ 'body' ] = body
                break
        url = '/read/' + str( id ) + '/'
        return redirect( url )

# stop server : Ctrl + c
# debug = True : when you fix the code, it reflects to the server autometically
app.run( port=5001 , debug = True )