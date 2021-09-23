from flask import Flask

app = Flask(__name__)

@app.route( '/' )
def hello():
    return "Hello world!"

@app.route( '/dojo' )
def dojo():
    return "Dojo!"

@app.route( '/say/<string:word>' )
def say(word):
    #print( word.title() )
    return "Hi " + word.title() +"!"

""" The app commented bekow was updated to specify int and string as arguments
@app.route( '/repeat/<num>/<word>' )       
def repeat( num, word ): #, word):
    num = int(num)
    result = ""
    for i in range(0, int(num) ):
        result = result + word +"<br>"
    return  result 
"""

@app.route( '/repeat/<int:num>/<string:word>' )       
def repeat( num, word ): #, word):
    result = ""
    for i in range(0, int(num) ):
        result = result + word +"<br>"
    return  result 


if __name__ == "__main__":
    app.run( debug = True)
