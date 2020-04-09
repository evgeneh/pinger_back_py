from flask import Flask
from config import Configurate
from flask_marshmallow import Marshmallow

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Configurate)

db = SQLAlchemy(app)
ma = Marshmallow(app)