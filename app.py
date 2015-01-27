__author__ = 'dcolussi'

# ---- Flask Hello World ---- #
# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# dynamic route
@app.route("/test")
def search():
    return "Hello"

# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"

# start the development server using the run() method
if __name__ == "__main__": app.run()
