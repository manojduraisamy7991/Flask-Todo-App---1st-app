from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY']= "cb1d50f17bf924580068eaff422d9beaeedbf4a9"
app.config['MONGO_URI'] = "mongodb+srv://patib91326:nPzT8U7FCKZaHYfH@cluster0.bd8lxx7.mongodb.net/employees?retryWrites=true&w=majority"

# setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db
from application import routes