import unittest
from unittest.mock import patch
import sys
sys.path.append('../')
from flask import Flask
from app import app, db 
from models import User
import account

class ModifySuccess(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        
        # Create all database tables
        with app.app_context():
            db.create_all()
            # Given a user exists
            test_user = User(name='Isabel', email='isabel@mail.ca', password='pass1234', age=22)
            db.session.add(test_user)
            db.session.commit()

    def tearDown(self):
        # Remove all database tables
        with app.app_context():
            db.session.remove()
            db.drop_all()


    def test_modify_success(self):
        #Testing succesfully updating age and name
        data = {
            'email': 'isabel@mail.ca',
            'name': 'Issy',
            'age': 23
        }
        response = self.app.put('/modify', json=data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Issy')
        self.assertEqual(data['age'], 23)

    def test_modify_user_DNE(self):
        data = {
            'email': 'nonexistent@mail.ca',
            'name': 'Issy',
            'age': 23
        }
        response = self.app.put('/modify', json=data)
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['message'], 'User does not exist')

    def test_modify_blank_name(self):
        #Testing modifying a name to nothing
        data = {
            'email': 'isabel@mail.ca',
            'name': '',
            'age': 23
        }
        response = self.app.put('/modify', json=data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Name cannot be blank')

    def test_modify_invalid_age(self):
        #Testing modifying an age to an invalid age
        data = {
            'email': 'isabel@mail.ca',
            'name': 'Issy',
            'age': -100
        }
        response = self.app.put('/modify', json=data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Invalid age')


if __name__ == '__main__':
    unittest.main()