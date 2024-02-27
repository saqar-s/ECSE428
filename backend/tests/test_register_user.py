import unittest
import sys
sys.path.append('../')
from app import app, db 


class TestRegisterUser(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        
        # Create all database tables
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Remove all database tables
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Unit test 1: Success User Registration (Normal Flow)
    def test_register_new_user(self):
        data = {
            'name': 'rambod',
            'email': 'rambod@example.com',
            'password': 'password123',
            'age': 23
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Registration successful')


    # Unit test 2: Register with Already-Existed Email
    def test_register_exist_user(self):
        # first register a user
        data = {
            'name': 'rambod',
            'email': 'rambod@example.com',
            'password': 'password123',
            'age': 23
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 201)

        # re-register with the same email address
        data2 = {
            'name': 'rambod2',
            'email': 'rambod@example.com', # same email address
            'password': 'password12345',
            'age': 24
        }
        response = self.app.post('/register', json=data2)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Email already exists')


    # Unit test 3: User Registration with Empty name
    def test_register_empty_name_user(self):
        data = {
            'name': '', # empty name
            'email': 'rambod',
            'password': 'password123',
            'age': 23
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')


    # Unit test 4: User Registration with Empty email
    def test_register_empty_email_user(self):
        data = {
            'name': 'rambod',
            'email': '', # empty email
            'password': 'password123',
            'age': 23
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')


    # Unit test 5: User Registration with Empty password
    def test_register_empty_password_user(self):
        data = {
            'name': 'rambod',
            'email': 'rambod@gmail.com',
            'password': '', # empty password
            'age': 23
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')

    
    # Unit test 6: User Registration with Empty age
    def test_register_empty_age_user(self):
        data = {
            'name': 'rambod',
            'email': 'rambod@gmail.com',
            'password': 'password123',
            'age': '' # empty age
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')


    # Unit test 7: User Registration with invalid email
    def test_register_invalid_email_user(self):
        data = {
            'name': 'rambod',
            'email': 'rambodgmail.com', # invalid email
            'password': 'password123',
            'age': 23
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid email address')


    # Unit test 8: User Registration with invalid age
    def test_register_invalid_age_user(self):
        data = {
            'name': 'rambod',
            'email': 'rambod@gmail.com',
            'password': 'password123',
            'age': -23 # invalid age
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid age')

if __name__ == '__main__':
    unittest.main()