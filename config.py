__author__ = 'yangziling'
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url':'https://www.google.com/accounts/o8/id'},
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'QQ', 'url': 'https://www.myopenid.com' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
]

userlist = [
    {'nickname':'Susan', 'email':'susan@123.com'},
    {'nickname':'John', 'email':'john@123.com'}
]

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']
