import os

DEBUG = True

# SQLAlchemy
db_uri = os.getenv('DATABASE_URL')
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False