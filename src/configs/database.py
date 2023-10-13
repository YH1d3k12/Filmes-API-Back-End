from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Configs:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False