from flask import Flask
import random

app = Flask( __name__ )

@app.route( '/' )
def index():

    # return type should be String
    return 'random : <strong>' + str( random.random() ) + '</strong>'

# stop server : Ctrl + c
# debug = True : when you fix the code, it reflects to the server autometically
app.run( port=5001 , debug = True )