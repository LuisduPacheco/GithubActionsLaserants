from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
passDB = "ADMINu5"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://root:{passDB}@localhost/book_inventory_management"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from app import routes