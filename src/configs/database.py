from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Configs:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False