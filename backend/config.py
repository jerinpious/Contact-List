from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__) #initializing the flask app
CORS(app) #wrapping the app with cors to avoid any cors error that might happen when communicating with the frontend


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" # specifying the location for the sqlite to save in the local machine
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False #what this function essentially does is to track any modification made to the data for easy development we willput it false for now

db = SQLAlchemy(app) #this will make an instance of the database which give us access to the database

# this is an ORM which is object relational mapping which essentially help us to create a normal python class and it will translate into sql and then apply it to the database
