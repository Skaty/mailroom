'''
Entrypoint of the application
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Load appropriate objects
app = Flask(__name__, instance_relative_config=True)

# Load defaults first and override with instance
app.config.from_object('mailroom.config')
app.config.from_json('mailroom.cfg', silent=True)

# Load database
db = SQLAlchemy(app)

from mailroom.mod_api.controllers import mod_api

app.register_blueprint(mod_api)
