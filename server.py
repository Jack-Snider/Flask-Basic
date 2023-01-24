from flask import Flask
import random

app = Flask( __name__ )

@app.route( '/' )
def index():

    # return type should be String
    return 'Welcome'

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