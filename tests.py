__author__ = 'yangziling'
#!flask/bin/python

import os
import unittest
from datetime import datetime

from config import basedir
from app import app, db
from app.models import User

class TestCase(unittest.TestCase):
    def serUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_make_unique_nickname(self):
        u = User(nickname = 'john', email = 'john@example.com', about_me='John_about_me', last_seen=datetime.now())
        db.session.add(u)
        db.session.commit()
        nickname = User.make_unique_nickname('john')
        assert nickname != 'john'

        u = User(nickname=nickname, email='susan@example.com', about_me='about_me', last_seen=datetime.now())
        db.session.add(u)
        db.session.commit()
        nickname2 = User.make_unique_nickname('john')
        assert nickname2 != 'john'
        assert nickname2 != nickname

if __name__ == '__main__':
    unittest.main()

